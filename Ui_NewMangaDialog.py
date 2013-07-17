# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewMangaDialog.ui'
#
# Created: Wed Jul 17 20:34:35 2013
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

class Ui_NewMangaDialog(object):
    def setupUi(self, NewMangaDialog):
        NewMangaDialog.setObjectName(_fromUtf8("NewMangaDialog"))
        NewMangaDialog.resize(231, 78)
        self.gridLayout = QtGui.QGridLayout(NewMangaDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(NewMangaDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.mangaLineEdit = QtGui.QLineEdit(self.splitter)
        self.mangaLineEdit.setObjectName(_fromUtf8("mangaLineEdit"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(NewMangaDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(NewMangaDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewMangaDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewMangaDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewMangaDialog)

    def retranslateUi(self, NewMangaDialog):
        NewMangaDialog.setWindowTitle(_translate("NewMangaDialog", "Dialog", None))
        self.label.setText(_translate("NewMangaDialog", "Manga:", None))

