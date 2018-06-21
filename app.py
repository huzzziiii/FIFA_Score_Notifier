import score
import sendText
import config

latest_update = ""

DATA = {
    "hashkey": config.HASH_KEY,
    "numbers": config.NUMBER,
    "sender": config.SENDER,
    "uname" : config.USERNAME
}

num = DATA['numbers']
hashkey = DATA['hashkey']
sender = DATA['sender']
username = DATA['uname']

#print(num)

while True: 
    previous_update = score.scoreUpdate()
    
    if previous_update != latest_update:
        sendText.textMsg(username,hashkey,num,sender,previous_update)
        print(previous_update)
        latest_update = previous_update
