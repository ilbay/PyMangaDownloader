import urllib2
import re
import datetime
from BeautifulSoup import BeautifulSoup
import time


class MangaManager:
        def __init__(self):
                self._mangalist = "http://www.mangareader.net/alphabetical"
                self._mangasite = "http://www.mangareader.net"
                self._mangaLink = None
                self._completed = False

        def searchManga(self, mangaName):
                mangaName = mangaName.replace(" ","").lower()

                mangaListPage = urllib2.urlopen(self._mangalist)
	        soup=BeautifulSoup(mangaListPage)
	        mangaGroupList = soup.findAll('ul',{'class':'series_alpha'})
                
                self._mangaLink = None

                for mangaGroup in mangaGroupList:
                        mangaList = mangaGroup.findAll("li")
                        for li in mangaList:
                                if li.a.text.replace(" ","").lower() == mangaName:
                                        self._mangaLink = li.a["href"]
                                        if li.span != None:
                                                self._completed = True
                                        return True

                return False
