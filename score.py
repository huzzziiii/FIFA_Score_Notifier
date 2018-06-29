from bs4 import BeautifulSoup
import urllib2

url = "https://www.sportinglife.com/football/live/vidiprinter"
    
# return value from urlopen() gives access to the headers from the HTTP server

def scoreUpdate(teams):
    
    file = urllib2.urlopen(url)
    html = file.read()
    file.close()

    soup = BeautifulSoup(html, "lxml")
    msg = soup.find('span', attrs = {'class' : "vidiline-message"})
    highlight = soup.find('span', attrs = {'class' : "vidiline-highlight-score"})
    event = soup.find('span', attrs = {'class' : 'vidiline-highlight-event'})
    player = soup.find('span', attrs = {'class' : 'vidiline-player'})
    
    txt = event.text + highlight.text + player.text

#iterating over teams array and seeing if the current update is about the desired team
    for team in teams:
        if (team == highlight.text):
            return txt
        
    
    return 0
    return txt
