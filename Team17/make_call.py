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
    log.info("called with call sid {}".format(call_obj.sid))

    return call_obj


def make_call(meeting_id):
    sbo = call(config.get('TWIML','sbo_twiml'),config.get('NUMS','sbo'))
    adv = call(config.get('TWIML','adv_twiml'),config.get('NUMS','adv'))

if __name__=="__main__":
    run()
