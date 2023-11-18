import sys
from PyQt5.QtWidgets import QApplication

import db.init
from app.manger_window import MainWindow

cursor = db.init.init('tour_manage', user='suvorovars', password='suv')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow(cursor)
    win.show()
    sys.exit(app.exec_())