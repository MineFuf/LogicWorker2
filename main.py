import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Slot
from qt_material import apply_stylesheet


class LogicGeneratorWidget(QtWidgets.QWidget):
    def __init__(self, t):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QtWidgets.QLabel(t))


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        # self.setStyleSheet(open('resources/main_style.qss', 'r').read())
        apply_stylesheet(app, 'dark_purple.xml')

        button = QtWidgets.QPushButton("Man press me")
        button.clicked.connect(lambda: print('hello'))

        tab_layout = QtWidgets.QTabWidget()
        tab_layout.addTab(LogicGeneratorWidget('kys'), "Table To Logic")
        tab_layout.addTab(button, 'Button')
        layout.addWidget(tab_layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    size = (600, 400)

    widget = Window()
    widget.resize(*size)
    widget.setFixedSize(*size)
    widget.show()

    sys.exit(app.exec())
