import sys
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import QStringList, QString
from MainWindow import MainWindow
from MangaManager import MangaManager
from Controller import Controller

def main():
        app = QApplication(sys.argv)

        controller = Controller()
        controller.create()
        controller.show()

        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
	"""m=MangaManager()
	print m.searchManga("berserk")
        m.downloadAll()"""
