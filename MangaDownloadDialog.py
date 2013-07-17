from PyQt4.QtGui import QDialog,QAction,QIcon,QMessageBox
from PyQt4.QtCore import QStringList,QString,QObject,SIGNAL,SLOT
from Ui_MangaDownloadDialog import Ui_MangaDownloadDialog

class MangaDownloadDialog(QDialog):
        def __init__(self):
                QDialog.__init__(self)

                self.ui = Ui_MangaDownloadDialog()
                self.ui.setupUi(self)

                QObject.connect(self.ui.downloadAllChaptersButton, SIGNAL("clicked()"), self.downloadAllChapters)
                QObject.connect(self.ui.downloadLatestChapterButton, SIGNAL("clicked()"), self.downloadLatestChapter)

        def show(self, mangaName, mangaLink):
                self.ui.mangaNameLineEdit.setText(mangaName)
                self.ui.mangaLinkLineEdit.setText(mangaLink)
                self.setWindowTitle("Download "+mangaName)
                QDialog.show(self)

        def downloadAllChapters(self):
                self.close()
                self.emit(SIGNAL("downloadAllChapters"))

        def downloadLatestChapter(self):
                self.close()
                self.emit(SIGNAL("downloadLatestChapter"))
