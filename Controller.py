from MainWindow import MainWindow
from MangaManager import MangaManager
from PyQt4.QtCore import QObject,SIGNAL,SLOT
import threading

class Controller:
        def __init__(self):
                self.mainWindow = MainWindow()
                self.mangaManager = MangaManager()

        def show(self):
                self.mainWindow.show()

        def create(self):
                QObject.connect(self.mainWindow.newMangaDialog, SIGNAL("newMangaRequest"), self.newMangaRequest)
                QObject.connect(self.mainWindow.mangaDownloadDialog, SIGNAL("downloadAllChapters"), self.downloadAllChapters)

                QObject.connect(self.mangaManager,SIGNAL("downloadNewChapter"),self.informUserForNewDownloadingPage)
                QObject.connect(self.mangaManager,SIGNAL("chaptersPageSize"),self.mainWindow.initializeProgressBar)
                QObject.connect(self.mangaManager,SIGNAL("newPageDownloaded"),self.mainWindow.updateProgressBar)
                QObject.connect(self.mangaManager,SIGNAL("compressingDownloadedChapter"),self.informUserForCompressingDownloadedChapter)
                QObject.connect(self.mangaManager,SIGNAL("downloadingChapterDone"),self.informUserForDownloadedChapter)

        def newMangaRequest(self, mangaName):
                self.mainWindow.updateStatusBar("Looking for " + mangaName + "...")

                if self.mangaManager.searchManga(mangaName):
                        self.mainWindow.mangaDownloadDialog.show(self.mangaManager.getMangaName(),self.mangaManager.getMangaLink())
                else:
                        print "Manga cannot be found"

                self.mainWindow.updateStatusBar("")

        def informUserForNewDownloadingPage(self, chapterName):
                self.mainWindow.updateStatusBar("Downloading " + chapterName + "...")

        def informUserForCompressingDownloadedChapter(self, chapterName):
                self.mainWindow.updateStatusBar("Compressing " + chapterName + "...")

        def informUserForDownloadedChapter(self, chapterName):
                self.mainWindow.updateStatusBar("Finished")

        def downloadAllChapters(self):
                t = threading.Thread(target = self.mangaManager.downloadAll)
                t.daemon = True
                t.start()
