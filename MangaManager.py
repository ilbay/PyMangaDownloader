import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import time
import os
import zipfile
from PyQt4.QtCore import QObject,SIGNAL,SLOT


class MangaManager:
        def __init__(self):
                self._mangalist = "http://www.mangareader.net/alphabetical"
                self._mangasite = "http://www.mangareader.net"
                self._mangaLink = None
                self._completed = False
                self._mangaName = None

        def isCompleted(self):
                return self._completed

        def getMangaName(self):
                return self._mangaName

        def searchManga(self, mangaName):
                self._mangaName = mangaName.replace(" ","").lower()

                mangaListPage = urllib2.urlopen(self._mangalist)
	        soup = BeautifulSoup(mangaListPage)
	        mangaGroupList = soup.findAll('ul',{'class':'series_alpha'})
                
                self._mangaLink = None

                for mangaGroup in mangaGroupList:
                        mangaList = mangaGroup.findAll("li")
                        for li in mangaList:
                                if li.a.text.replace(" ","").lower() == self._mangaName:
                                        self._mangaLink = li.a["href"]
                                        if li.span != None:
                                                self._completed = True
                                        return True

                return False

        def downloadAll(self):
                downloadUrl = self._mangasite + self._mangaLink
                mangaChaptersPage = urllib2.urlopen(downloadUrl)
                soup = BeautifulSoup(mangaChaptersPage)

                mangaChaptersList = soup.findAll('table',{'id':'listing'})

                if len(mangaChaptersList) > 0:
                        #mangaChaptersList = mangaChaptersList.pop()
                        rows = mangaChaptersList[0].findAll("tr")
                        for row in rows:
                                if row.a != None:
                                        if not os.path.isdir(row.td.text):
                                                os.mkdir(row.td.text)
                                        print row.td.text + " " + row.a["href"]
                                        self.download(row.a["href"], row.td.text)

        def download(self, url, folder):
                downloadUrl = self._mangasite + url
                mangaChapterPage = urllib2.urlopen(downloadUrl)
                soup = BeautifulSoup(mangaChapterPage)

                chapters = soup.findAll('select',{'id':'pageMenu'})[0].findAll("option")
                counter = 0

                for chapter in chapters:
                        while True:
                                try:
                                        downloadUrl = self._mangasite + chapter["value"]
                                        mangaChapterPage = urllib2.urlopen(downloadUrl)
                                        soup = BeautifulSoup(mangaChapterPage)

                                        mangaPage = soup.findAll('img',{'id':'img'})
                                        mangaImage = mangaPage[0]["src"]

                                        urllib.urlretrieve(mangaImage, folder+"/Page"+str(chapter.text).zfill(4)+".jpg")
                                        counter = 0
                                        break
                                except IOError, e:
                                        if counter >= 10:
                                                break
                                        time.sleep(1)
                                        counter += 1

                cbzFile = zipfile.ZipFile(folder+".cbz", 'w')
                for i in range(len(chapters)):
                        cbzFile.write(folder+"/Page"+str(i+1).zfill(4)+".jpg")
                cbzFile.close()
