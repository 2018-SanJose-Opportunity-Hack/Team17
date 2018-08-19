from Team17.util.imports import *

log = logger.getLogger(__name__)
config = file_config()

client = Client(config.get('CRED','account_sid'), config.get('CRED','auth_token'))

def send_sms(body, to_num, from_num='+16504762892'):
    message_obj = client.messages.create(
                                  body=body,
                                  from_=from_num,
                                  to=to_num
                              )
    log.info("message sent with message sid: {}".format(message_obj.sid))

    return message_obj


def call(twiml,to_num,from_num='+16504762892'):
    call_obj = client.calls.create(
                            url=twiml,
                            to=to_num,
                            from_=from_num
                        )
    log.info("called {} with call sid {}".format(to_num, call_obj.sid))

    return call_obj


def make_call(match_id):
    fetch = "select advisor_phone,sbo_phone from pcv_matches where match_sid={}".format(match_id)
    res = fetch_query(fetch)
    sbo_ph = ''.join(res[0][1].split('-'))
    adv_ph = ''.join(res[0][0].split('-'))
    if sbo_ph[0] != '+':
        sbo_ph = '+1'+sbo_ph
    if adv_ph[0] != '+':
        adv_ph = '+1'+adv_ph
    sbo = call(config.get('TWIML','sbo_twiml'),res[0][1])
    adv = call(config.get('TWIML','adv_twiml'),res[0][0])
    update = "update PCV_MATCHES set call_sid='{}' where match_sid={}".format(sbo.sid,match_id)
    if update_query(update):
        log.info('table updated with query {}'.format(update))
    else:
        log.error('table couldnot be updated')

if __name__=="__main__":
    run()
