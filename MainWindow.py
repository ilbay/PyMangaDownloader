from PyQt4.QtGui import QMainWindow,QAction,QIcon,QProgressBar, QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt4.QtCore import QStringList,QString
from Ui_MainWindow import Ui_MainWindow
from NewMangaDialog import NewMangaDialog
from MangaDownloadDialog import MangaDownloadDialog

class MainWindow(QMainWindow):
        def __init__(self):
                QMainWindow.__init__(self)
                
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)

                self.setCentralWidget(self.ui.mangaTableView)
                self.newMangaDialog = NewMangaDialog()
                self.mangaDownloadDialog = MangaDownloadDialog()

                self.mangaTableModel = QStandardItemModel(0, 3, self)
                self.mangaTableModel.setHorizontalHeaderItem(0, QStandardItem(QString("Manga")))
                self.mangaTableModel.setHorizontalHeaderItem(1, QStandardItem(QString("Latest Chapter")))
                self.mangaTableModel.setHorizontalHeaderItem(2, QStandardItem(QString("Status")))
                self.ui.mangaTableView.setModel(self.mangaTableModel)

                newMangaAction = QAction(QIcon("./icon/add.ico"),'New Manga', self)
                newMangaAction.setShortcut('Ctrl+N')
                newMangaAction.triggered.connect(self.newMangaDialog.show)

                removeMangaAction = QAction(QIcon("./icon/delete.ico"),'Remove Manga', self)
                removeMangaAction.setShortcut('Delete')

                preferencesAction = QAction(QIcon("./icon/preferences.ico"),'Preferences', self)                

                aboutAction = QAction(QIcon("./icon/about.ico"),'About', self)

                self.ui.toolBar.addAction(newMangaAction)
                self.ui.toolBar.addAction(removeMangaAction)
                self.ui.toolBar.addSeparator()
                self.ui.toolBar.addAction(preferencesAction)
                self.ui.toolBar.addSeparator()
                self.ui.toolBar.addAction(aboutAction)

                self.progressBar = QProgressBar(self.ui.statusbar)
                self.ui.statusbar.addPermanentWidget(self.progressBar)
                self.progressBar.hide()

        def initializeProgressBar(self, size):
                self.progressBar.setRange(0, size)
                self.progressBar.setValue(0)
                self.progressBar.show()

        def updateProgressBar(self, value):
                self.progressBar.setValue(value)

        def updateStatusBar(self, msg):
                self.ui.statusbar.showMessage(msg)

        def displayMangaList(self, mangaList):
                for i in range(len(mangaList)):
                        mangaRow = QStandardItem(QString(mangaList[i]["name"]))
                        latestChapterRow = QStandardItem(QString(mangaList[i]["latestChapter"]))
                        statusRow = QStandardItem(QString(mangaList[i]["status"]))
                        if i%2 == 1:
                                brush = QBrush(QColor(200, 200, 200))
                                mangaRow.setBackground(brush)
                                latestChapterRow.setBackground(brush)
                                statusRow.setBackground(brush)

                        self.mangaTableModel.setItem(i, 0, mangaRow)
                        self.mangaTableModel.setItem(i, 1, latestChapterRow)
                        self.mangaTableModel.setItem(i, 2, statusRow)
