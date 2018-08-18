from Team17.util.imports import *

log = logger.getLogger(__name__)
config = file_config()

account_sid = 'ACba6fdcbb3d6f28ffee5e34cdb8af7e80'
auth_token = 'f860188456e94a66f9165a7d36dcf670'
client = Client(config.get('CRED','account_sid'), config.get('CRED','auth_token'))

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=config.get('CRED','sbo'),
                        from_=config.get('CRED','twillionum')
                    )

log.info("called with sid {}".format(call.sid))
