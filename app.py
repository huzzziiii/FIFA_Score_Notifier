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
teams = ["Brazil", "Argentina", "England"]  #favorite teams
sender = DATA['sender']
username = DATA['uname']


while True: 
    current_update = score.scoreUpdate(teams)
   
#send a text only if the current update is about the desired teams

    if current_update!=0 and current_update != latest_update:
        twilioSendText.sendSMS(account_sid, auth_token, current_update)
        print(current_update)
        
        latest_update = current_update
