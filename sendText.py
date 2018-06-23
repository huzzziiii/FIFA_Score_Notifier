 # Import required libraries
import urllib      # URL functions
import urllib2     # URL functions
import sys
reload(sys)

#setting the system default encoding as utf-8 at the start of the script, so that all strings are encoded using that.
sys.setdefaultencoding('utf-8')
    
def textMsg(username, hash, number, sender, message):
    
    # Set flag to 1 to simulate sending
    # This saves your credits while you are
    # testing your code.
    # To send real message set this flag to 0
    test_flag = 1

    #-----------------------------------------
    # No need to edit anything below this line
    #-----------------------------------------

    values = {'test'    : test_flag,
              'uname'   : username,
              'hash'    : hash,
              'message' : message,
              'from'    : sender,
              'selectednums' : number }

    url = 'http://api.txtlocal.com/send/?'

    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata)

    try:
      response = urllib2.urlopen(req)
      response_url = response.geturl()
      if response_url==url:
        print 'SMS sent!'
    except urllib2.URLError, e:
      print 'Send failed!'
      print e.reason