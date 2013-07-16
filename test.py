import sys
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import QStringList, QString
from Ui_PyMangaDownloader import Ui_PyMangaDownloader
from PyMangaDownloader import PyMangaDownloader


def main():
        app = QApplication(sys.argv)

        mangaWindow = PyMangaDownloader()
        mangaWindow.show()

        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
