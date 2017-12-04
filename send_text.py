from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc7c6527d71af857207a258a1f0ffeb5e"
# Your Auth Token from twilio.com/console
auth_token  = "85b43dbae62be16d3831e23cdda59bb0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+385913653829",
    from_="+12568264529",
    body="Hello from the other side!")

print(message.sid)