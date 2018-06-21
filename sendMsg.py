#!/usr/bin/env python

import urllib.request
import urllib.parse

def sendSMS(uname, hashCode, numbers, sender, message):
    data =  urllib.parse.urlencode({'username': uname, 'hash': hashCode, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("http://api.txtlocal.com/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

resp =  sendSMS('Huzzi', 'de97695e008b45284f2b36b5cf2d20a861818f06ca074066e7aa1d33b6135fc4', '16135019364',
    'Jims Autos', 'This is your message')
print (resp)
