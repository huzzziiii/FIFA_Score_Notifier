from bs4 import BeautifulSoup
import urllib2

url = "https://www.sportinglife.com/football/live/vidiprinter"
    
file = urllib2.urlopen(url)
html = file.read()
file.close()


soup = BeautifulSoup(html, "lxml")

def scoreUpdate():
    highlight = soup.find('span', attrs = {'class' : "vidiline-highlight-score"})
    event = soup.find('span', attrs = {'class' : 'vidiline-highlight-event'})
    player = soup.find('span', attrs = {'class' : 'vidiline-player'})

    txt = event.text + highlight.text + player.text
    #print(txt)

    return txt
#--------------------
