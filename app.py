import score
import sendText
import twilioSendText
import config

latest_update = ""

DATA = {
    "hashkey": config.HASH_KEY,
    "account_sid": config.ACCOUNT_SID,
    "auth_token": config.AUTH_TOKEN,
    "numbers": config.NUMBER,
    "sender": config.SENDER,
    "uname" : config.USERNAME
    
}

num = DATA['numbers']
hashkey = DATA['hashkey']
account_sid = DATA['account_sid']
auth_token = DATA['auth_token']

sender = DATA['sender']
username = DATA['uname']
#print(num)

while True: 
    current_update = score.scoreUpdate()
    
    if current_update != latest_update:
        twilioSendText.sendSMS(account_sid, auth_token, current_update)
        print(current_update)
        
        latest_update = current_update
