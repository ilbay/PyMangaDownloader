import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import time
import os
import zipfile
from PyQt4.QtCore import QObject,SIGNAL,SLOT
import shutil

class MangaDownloadManager(QObject):
        def __init__(self):
                QObject.__init__(self)
                self._mangalist = "http://www.mangareader.net/alphabetical"
                self._mangasite = "http://www.mangareader.net"
                self._mangaLink = None
                self._completed = False
                self._mangaName = None

        def isCompleted(self):
                return self._completed

        def getMangaName(self):
                return self._mangaName

        def getMangaLink(self):
                return self._mangasite+self._mangaLink

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
                chaptersList = self.getChaptersAsList()
                for chapter in chaptersList:
                        self.download(chapter["url"], chapter["name"])

        def downloadLatestChapter(self):
                chaptersList = self.getChaptersAsList()
                chapter = chaptersList[len(chaptersList)-1]
                self.download(chapter["url"], chapter["name"])

        def download(self, url, folder):
                self.emit(SIGNAL("downloadNewChapter"),folder)

                if not os.path.isdir(folder):
                        os.mkdir(folder)

                downloadUrl = self._mangasite + url
                mangaChapterPage = urllib2.urlopen(downloadUrl)
                soup = BeautifulSoup(mangaChapterPage)

                pages = soup.findAll('select',{'id':'pageMenu'})[0].findAll("option")
                counter = 0
                numOfDownloadedPages = 0

                self.emit(SIGNAL("chaptersPageSize"),len(pages))

                for page in pages:
                        while True:
                                try:
                                        downloadUrl = self._mangasite + page["value"]
                                        mangaChapterPage = urllib2.urlopen(downloadUrl)
                                        soup = BeautifulSoup(mangaChapterPage)

                                        mangaPage = soup.findAll('img',{'id':'img'})
                                        mangaImage = mangaPage[0]["src"]

                                        urllib.urlretrieve(mangaImage, folder+"/Page"+str(page.text).zfill(4)+".jpg")
                                        counter = 0

                                        numOfDownloadedPages += 1
                                        self.emit(SIGNAL("newPageDownloaded"),numOfDownloadedPages)

                                        break
                                except IOError, e:
                                        if counter >= 10:
                                                break
                                        time.sleep(1)
                                        counter += 1

                self.emit(SIGNAL("compressingDownloadedChapter"),folder)

                cbzFile = zipfile.ZipFile(folder+".cbz", 'w')
                for i in range(len(pages)):
                        cbzFile.write(folder+"/Page"+str(i+1).zfill(4)+".jpg")
                cbzFile.close()

                shutil.rmtree(folder)

                self.emit(SIGNAL("downloadingChapterDone"),folder)

        def getChaptersAsList(self):
                downloadUrl = self._mangasite + self._mangaLink
                mangaChaptersPage = urllib2.urlopen(downloadUrl)
                soup = BeautifulSoup(mangaChaptersPage)

                mangaChaptersList = soup.findAll('table',{'id':'listing'})
                chaptersList = []

                if len(mangaChaptersList) > 0:
                        rows = mangaChaptersList[0].findAll("tr")
                        for row in rows:
                                if row.a != None:
                                        chaptersList.append({"url":row.a["href"], "name":row.td.text})

                return chaptersList
