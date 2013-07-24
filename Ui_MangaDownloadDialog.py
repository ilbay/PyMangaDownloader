# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MangaDownloadDialog.ui'
#
# Created: Wed Jul 24 18:42:21 2013
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

class Ui_MangaDownloadDialog(object):
    def setupUi(self, MangaDownloadDialog):
        MangaDownloadDialog.setObjectName(_fromUtf8("MangaDownloadDialog"))
        MangaDownloadDialog.resize(320, 240)
        self.gridLayout = QtGui.QGridLayout(MangaDownloadDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(MangaDownloadDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.mangaNameLineEdit = QtGui.QLineEdit(MangaDownloadDialog)
        self.mangaNameLineEdit.setEnabled(False)
        self.mangaNameLineEdit.setObjectName(_fromUtf8("mangaNameLineEdit"))
        self.horizontalLayout.addWidget(self.mangaNameLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(MangaDownloadDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.mangaLinkLineEdit = QtGui.QLineEdit(MangaDownloadDialog)
        self.mangaLinkLineEdit.setEnabled(False)
        self.mangaLinkLineEdit.setObjectName(_fromUtf8("mangaLinkLineEdit"))
        self.horizontalLayout_2.addWidget(self.mangaLinkLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.downloadAllChaptersButton = QtGui.QPushButton(MangaDownloadDialog)
        self.downloadAllChaptersButton.setObjectName(_fromUtf8("downloadAllChaptersButton"))
        self.verticalLayout.addWidget(self.downloadAllChaptersButton)
        self.downloadLatestChapterButton = QtGui.QPushButton(MangaDownloadDialog)
        self.downloadLatestChapterButton.setObjectName(_fromUtf8("downloadLatestChapterButton"))
        self.verticalLayout.addWidget(self.downloadLatestChapterButton)
        self.checkForNextIssueButton = QtGui.QPushButton(MangaDownloadDialog)
        self.checkForNextIssueButton.setObjectName(_fromUtf8("checkForNextIssueButton"))
        self.verticalLayout.addWidget(self.checkForNextIssueButton)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.retranslateUi(MangaDownloadDialog)
        QtCore.QMetaObject.connectSlotsByName(MangaDownloadDialog)

    def retranslateUi(self, MangaDownloadDialog):
        MangaDownloadDialog.setWindowTitle(_translate("MangaDownloadDialog", "Dialog", None))
        self.label.setText(_translate("MangaDownloadDialog", "Manga:", None))
        self.label_2.setText(_translate("MangaDownloadDialog", "Manga Link:", None))
        self.downloadAllChaptersButton.setText(_translate("MangaDownloadDialog", "Download All Chapters", None))
        self.downloadLatestChapterButton.setText(_translate("MangaDownloadDialog", "Download Latest Chapter", None))
        self.checkForNextIssueButton.setText(_translate("MangaDownloadDialog", "Just Check For Next Published Issue", None))

