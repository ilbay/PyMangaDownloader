# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyMangaDownloader.ui'
#
# Created: Tue Jul 16 04:27:48 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PyMangaDownloader(object):
    def setupUi(self, PyMangaDownloader):
        PyMangaDownloader.setObjectName(_fromUtf8("PyMangaDownloader"))
        PyMangaDownloader.resize(640, 480)
        self.mangaTableWidget = QtGui.QTableWidget(PyMangaDownloader)
        self.mangaTableWidget.setEnabled(True)
        self.mangaTableWidget.setColumnCount(3)
        self.mangaTableWidget.setObjectName(_fromUtf8("mangaTableWidget"))
        self.mangaTableWidget.setRowCount(0)
        self.mangaTableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.mangaTableWidget.horizontalHeader().setMinimumSectionSize(21)
        self.mangaTableWidget.horizontalHeader().setStretchLastSection(True)
        self.menubar = QtGui.QMenuBar(PyMangaDownloader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        PyMangaDownloader.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PyMangaDownloader)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PyMangaDownloader.setStatusBar(self.statusbar)
        self.actionNew_Manga = QtGui.QAction(PyMangaDownloader)
        self.actionNew_Manga.setObjectName(_fromUtf8("actionNew_Manga"))
        self.menuFile.addAction(self.actionNew_Manga)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PyMangaDownloader)
        QtCore.QMetaObject.connectSlotsByName(PyMangaDownloader)

    def retranslateUi(self, PyMangaDownloader):
        PyMangaDownloader.setWindowTitle(_translate("PyMangaDownloader", "MainWindow", None))
        self.menuFile.setTitle(_translate("PyMangaDownloader", "File", None))
        self.actionNew_Manga.setText(_translate("PyMangaDownloader", "New Manga", None))

