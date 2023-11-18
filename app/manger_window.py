from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys
from pg8000 import Cursor


class MainWindow(QMainWindow):
    def __init__(self, db_cursor: Cursor, parent=None):
        super().__init__(parent)
        self.db_cursor = db_cursor
        self.setupUi()

    def get_data(self):
        return self.db_cursor.execute("SELECT * FROM manager")

    def setupUi(self):
        self.setWindowTitle("Managers")  # заголовок окна
        self.resize(400, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        SetOfLines = QVBoxLayout(central_widget)
        SetOfLines.setAlignment(Qt.AlignTop)

        data = self.get_data()

        for i in data:
            j = QLineEdit()  # Используй явный индекс для текста
            print(str(i))
            j.setText(str(i))
            SetOfLines.addWidget(j)








