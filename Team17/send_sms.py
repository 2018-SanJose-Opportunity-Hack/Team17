from twilio.rest import Client

account_sid = "ACba6fdcbb3d6f28ffee5e34cdb8af7e80"
auth_token = "f860188456e94a66f9165a7d36dcf670"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='You have a call scheduled on August 20 at 3:30 pm with Elon Musk',
                              from_='+16504762892',
                              to='+14089170842'
                          )

print(message.sid)