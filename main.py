from urllib.request import urlopen, urlretrieve
from time import time, sleep, ctime

from bs4 import BeautifulSoup

from balloontip import balloon_tip

starttime = time()
interval = 300.0
while True:
    url = "http://www.espncricinfo.com/series/8048/game/1136572/kings-xi-punjab-vs-chennai-super-kings-12th-match-indian-premier-league-2018"
    source_code = BeautifulSoup(urlopen(url).read(), "html.parser")
    t = source_code.title.string
    t = t.replace ("Match Summary","")
    t = t.replace ("ESPNCricinfo","")
    t = t.replace ("|","",2)
    print (ctime(), t)
    balloon_tip("CricScore", t)
    sleep(interval - ((time() - starttime) % interval))