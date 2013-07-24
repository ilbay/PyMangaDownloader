from MainWindow import MainWindow
from MangaDownloadManager import MangaDownloadManager
from MangaListManager import MangaListManager
from PyQt4.QtCore import QObject,SIGNAL,SLOT
import threading

class Controller:
        def __init__(self):
                self.mainWindow = MainWindow()
                self.mangaDownloadManager = MangaDownloadManager()
                self.mangaListManager = MangaListManager()

        def show(self):
                mangaList = self.mangaListManager.read()
                self.mainWindow.addMangaListToMangaTable(mangaList)
                self.mainWindow.show()

        def create(self):
                QObject.connect(self.mainWindow.newMangaDialog, SIGNAL("newMangaRequest"), self.newMangaRequest)
                QObject.connect(self.mainWindow.mangaDownloadDialog, SIGNAL("downloadAllChapters"), self.downloadAllChapters)
                QObject.connect(self.mainWindow.mangaDownloadDialog, SIGNAL("downloadLatestChapter"), self.downloadLatestChapter)

                QObject.connect(self.mangaDownloadManager,SIGNAL("downloadNewChapter"),self.informUserForNewDownloadingPage)
                QObject.connect(self.mangaDownloadManager,SIGNAL("chaptersPageSize"),self.mainWindow.initializeProgressBar)
                QObject.connect(self.mangaDownloadManager,SIGNAL("newPageDownloaded"),self.mainWindow.updateProgressBar)
                QObject.connect(self.mangaDownloadManager,SIGNAL("compressingDownloadedChapter"),self.informUserForCompressingDownloadedChapter)
                QObject.connect(self.mangaDownloadManager,SIGNAL("downloadingChapterDone"),self.informUserForDownloadedChapter)

        def newMangaRequest(self, mangaName):
                self.mainWindow.updateStatusBar("Looking for " + mangaName + "...")

                if self.mangaDownloadManager.searchManga(mangaName):
                        self.mainWindow.mangaDownloadDialog.show(self.mangaDownloadManager.getMangaName(),self.mangaDownloadManager.getMangaLink())
                else:
                        print "Manga cannot be found"

                self.mainWindow.updateStatusBar("")

        def informUserForNewDownloadingPage(self, chapter):
                self.mainWindow.updateStatusBar("Downloading " + chapter["name"] + "...")
                self.mainWindow.updateMangaTable(chapter)

        def informUserForCompressingDownloadedChapter(self, chapterName):
                self.mainWindow.updateStatusBar("Compressing " + chapterName + "...")

        def informUserForDownloadedChapter(self, chapter):
                self.mainWindow.updateStatusBar("Finished")
                self.mainWindow.updateMangaTable(chapter)

        def downloadAllChapters(self):
                t = threading.Thread(target = self.mangaDownloadManager.downloadAll)
                t.daemon = True
                t.start()

        def downloadLatestChapter(self):
                t = threading.Thread(target = self.mangaDownloadManager.downloadLatestChapter)
                t.daemon = True
                t.start()
