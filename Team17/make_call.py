from Team17.util.imports import *

log = logger.getLogger(__name__)
config = file_config()

account_sid = 'ACba6fdcbb3d6f28ffee5e34cdb8af7e80'
auth_token = 'f860188456e94a66f9165a7d36dcf670'
client = Client(config.get('CRED','account_sid'), config.get('CRED','auth_token'))

def call(twiml,to_num,from_num='+16504762892'):
    call_obj = client.calls.create(
                            url=twiml,
                            to=to_num,
                            from_=from_num
                        )
    log.info("called with sid {}".format(call_obj.sid))
    return call_obj

def run():
    sbo = call(config.get('TWIML','sbo_twiml'),config.get('NUMS','sbo'))
    sbo = call(config.get('TWIML','adv_twiml'),config.get('NUMS','adv'))

if __name__=="__main__":
    run()
