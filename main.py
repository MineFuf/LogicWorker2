import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QStatusBar
from PySide6.QtCore import Slot
from qt_material import apply_stylesheet
from ui.truth_table_widget import TruthTableWidget


class LogicGeneratorWidget(QtWidgets.QWidget):
    def __init__(self, window):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(TruthTableWidget(window))


class MainWindowWidget(QtWidgets.QWidget):
    def __init__(self, window):
        super().__init__()

        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        # self.setStyleSheet(open('resources/main_style.qss', 'r').read())
        apply_stylesheet(app, 'dark_purple.xml')

        button = QtWidgets.QPushButton("Man press me")
        button.clicked.connect(lambda: print('hello'))

        tab_layout = QtWidgets.QTabWidget()
        tab_layout.addTab(LogicGeneratorWidget(window), "Table To Logic")
        tab_layout.addTab(button, 'Button')
        layout.addWidget(tab_layout)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(*size)
        self.setMinimumSize(*size)

        self.setCentralWidget(MainWindowWidget(self))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    size = (500, 300)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
