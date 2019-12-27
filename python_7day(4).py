# +12512379669
# ACbc1876f8e434fd05b12c901a9c4e234e
# 55edceba8ef4acadd436604cd07bf65e

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACbc1876f8e434fd05b12c901a9c4e234e'
auth_token = '55edceba8ef4acadd436604cd07bf65e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="안녕 뭐해?",
                     from_='+12512379669',
                     to='+821027748460'
                 )

print(message.sid)