from PyQt4.QtGui import QMainWindow,QAction,QIcon
from PyQt4.QtCore import QStringList,QString
from Ui_PyMangaDownloader import Ui_PyMangaDownloader

class PyMangaDownloader(QMainWindow):
        def __init__(self):
                QMainWindow.__init__(self)
                
                self.ui = Ui_PyMangaDownloader()
                self.ui.setupUi(self)

                self.setCentralWidget(self.ui.mangaTableWidget)
                self.setWindowTitle("PyMangaDownloader")

                headerList = QStringList()
                headerList.append(QString("Manga"))
                headerList.append(QString("Issue"))
                headerList.append(QString("Status"))
                self.ui.mangaTableWidget.setHorizontalHeaderLabels(headerList)

                
                newMangaAction = QAction(QIcon("./icon/add.ico"),'New Manga', self)
                newMangaAction.setShortcut('Ctrl+N')

                removeMangaAction = QAction(QIcon("./icon/delete.ico"),'Remove Manga', self)
                removeMangaAction.setShortcut('Delete')

                preferencesAction = QAction(QIcon("./icon/preferences.ico"),'Preferences', self)                

                aboutAction = QAction(QIcon("./icon/about.ico"),'About', self)

                self.toolBar = self.addToolBar('ToolBar')
                self.toolBar.addAction(newMangaAction)
                self.toolBar.addAction(removeMangaAction)
                self.toolBar.addSeparator()
                self.toolBar.addAction(preferencesAction)
                self.toolBar.addSeparator()
                self.toolBar.addAction(aboutAction)
