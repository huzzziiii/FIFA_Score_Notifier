from twilio.rest import Client

def sendSMS(account_sid, auth_token, msg):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="",  
        from_="",
        body=msg)
    
    print(message.sid)

