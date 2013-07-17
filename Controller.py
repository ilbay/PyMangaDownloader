from MainWindow import MainWindow
from MangaManager import MangaManager
from PyQt4.QtCore import QObject,SIGNAL,SLOT

class Controller:
        def __init__(self):
                self.mainWindow = MainWindow()
                self.mangaManager = MangaManager()

        def show(self):
                self.mainWindow.show()

        def create(self):
                QObject.connect(self.mainWindow.newMangaDialog, SIGNAL("newMangaRequest"), self.newMangaRequest)

        def newMangaRequest(self, mangaName):
                if self.mangaManager.searchManga(mangaName):
                        self.mainWindow.mangaDownloadDialog.show(self.mangaManager.getMangaName(),self.mangaManager.getMangaLink())
                else:
                        print "Manga cannot be found"
