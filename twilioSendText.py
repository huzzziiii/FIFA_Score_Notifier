from twilio.rest import Client

def sendSMS(account_sid, auth_token, msg):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+16135019364", 
        from_="+16479579730",
        body=msg)
    
    print(message.sid)

