from PyQt4.QtGui import QDialog,QAction,QIcon,QMessageBox
from PyQt4.QtCore import QStringList,QString,QObject,SIGNAL,SLOT
from Ui_NewMangaDialog import Ui_NewMangaDialog

class NewMangaDialog(QDialog):
        def __init__(self):
                QDialog.__init__(self)

                self.ui = Ui_NewMangaDialog()
                self.ui.setupUi(self)

                QObject.connect(self, SIGNAL("accepted()"), self.mangaNameControl)
        def show(self):
                self.ui.mangaLineEdit.setText("")
                QDialog.show(self)
        def mangaNameControl(self):
                mangaName = str(self.ui.mangaLineEdit.text())
                if len(mangaName) > 0:
                        self.emit(SIGNAL("newMangaRequest"), mangaName)
                        self.close()
                else:
                        QMessageBox.information(self, QString("Warning"), QString("Manga name space cannot be empty."), QMessageBox.Ok)
