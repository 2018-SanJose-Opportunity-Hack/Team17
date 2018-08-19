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


def update_call_sid(sbo,match_id):
    update = "update PCV_MATCHES set call_sid='{}' where match_sid={}".format(sbo.sid,match_id)
    if update_query(update):
        log.info('table updated with query {}'.format(update))
    else:
        log.error('table couldnot be updated')
    while sbo.status != 'completed':
        time.sleep(60)
        sbo = client.calls(sbo.sid).fetch()
        log.info('status of the call: {}'.format(sbo.status))
    return sbo


def update_call_duration(sbo,match_id):
    update = "update PCV_MATCHES set call_duration='{}' where match_sid={}".format(sbo.duration,match_id)
    if update_query(update):
        log.info('table updated with query {}'.format(update))
    else:
        log.error('table couldnot be updated')


def make_call(match_id):
    fetch = "select advisor_phone,sbo_phone,advisor_name,sbo_name from pcv_matches where match_sid={}".format(match_id)
    res = fetch_query(fetch)
    sbo_ph = ''.join(res[0][1].split('-'))
    adv_ph = ''.join(res[0][0].split('-'))
    if sbo_ph[0] != '+':
        sbo_ph = '+1'+sbo_ph
    if adv_ph[0] != '+':
        adv_ph = '+1'+adv_ph
    sbo = call(config.get('TWIML','sbo_twiml'),res[0][1])
    adv = call(config.get('TWIML','adv_twiml'),res[0][0])
    # update columns
    sbo = update_call_sid(sbo,match_id)
    update_call_duration(sbo,match_id)
    # send message
    msg_body_sbo = "How did you like the call with {}? Please click here to rate your meeting {}"\
    .format(res[0][2], config.get('GOOGLE_FORM','url')+str(match_id))
    msg_body_adv = "How did you like the call with {}? Please click here to rate your meeting {}"\
    .format(res[0][3], config.get('GOOGLE_FORM','url')+str(match_id))
    sbo = send_sms(msg_body_sbo, sbo_ph)
    adv = send_sms(msg_body_adv, adv_ph)

if __name__=="__main__":
    run()
