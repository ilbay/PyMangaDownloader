from PyQt4.QtGui import QDialog,QAction,QIcon,QMessageBox
from PyQt4.QtCore import QStringList,QString,QObject,SIGNAL,SLOT
from Ui_MangaDownloadDialog import Ui_MangaDownloadDialog

class MangaDownloadDialog(QDialog):
        def __init__(self):
                QDialog.__init__(self)

                self.ui = Ui_MangaDownloadDialog()
                self.ui.setupUi(self)

        def show(self, mangaName, mangaLink):
                self.ui.mangaNameLineEdit.setText(mangaName)
                self.ui.mangaLinkLineEdit.setText(mangaLink)
                self.setWindowTitle("Download "+mangaName)
                QDialog.show(self)