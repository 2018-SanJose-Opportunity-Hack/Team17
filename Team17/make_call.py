# Your Account Sid and Auth Token from twilio.com/console
from hackathon.util.imports import *

account_sid = 'ACba6fdcbb3d6f28ffee5e34cdb8af7e80'
auth_token = 'f860188456e94a66f9165a7d36dcf670'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+14089170842',
                        from_='+16504762892'
                    )

print(call.sid)
