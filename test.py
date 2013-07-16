import sys
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import QStringList, QString
from Ui_PyMangaDownloader import Ui_PyMangaDownloader

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_PyMangaDownloader()
ui.setupUi(window)

window.setCentralWidget(ui.mangaTableWidget)

list = QStringList()
list.append(QString("Manga"))
list.append(QString("Issue"))
list.append(QString("Status"))

ui.mangaTableWidget.setHorizontalHeaderLabels(list)

window.show()
sys.exit(app.exec_())

