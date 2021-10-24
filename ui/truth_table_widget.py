# from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QTableView, QWidget, QLineEdit, QPushButton, \
#     QSizePolicy, QLayout, QSplitter, QFileDialog

from PySide6.QtWidgets import *
from PySide6 import *

from PySide6.QtCore import Qt
from pathlib import Path
from pprint import pprint

from truth_table import TruthTable


class TruthTableWidget(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

        self.file_input = QHBoxLayout()
        self.file_input.setSizeConstraint(QLayout.SetNoConstraint)

        self.import_button = QPushButton("Import Table")
        self.import_button.clicked.connect(self.import_table)

        self.export_button = QPushButton("Export Table")
        self.export_button.clicked.connect(self.export_table)

        # file_input.addWidget(file_line_edit)
        self.file_input.addWidget(self.import_button)
        self.file_input.addWidget(self.export_button)

        tt = QSizePolicy.Preferred

        self.table_splitter = QSplitter()
        self.table_splitter.setSizePolicy(QSizePolicy.Expanding, tt)

        self.table_in = QTableView()
        self.table_in.setSizePolicy(QSizePolicy.Expanding, tt)
        self.table_out = QTableView()
        self.table_out.setSizePolicy(QSizePolicy.Expanding, tt)

        self.table_splitter.addWidget(self.table_in)
        self.table_splitter.addWidget(self.table_out)

        debug_button = QPushButton("Debug")
        debug_button.clicked.connect(self.debug)

        layout.addLayout(self.file_input)
        layout.addWidget(self.table_splitter)
        layout.addWidget(debug_button)

        self.table = None

    def import_table(self):
        # Get table file from user, return if empty
        filename = \
        QFileDialog.getOpenFileName(self, 'Open table file', str(Path.home()), "Table Files (*.ttbl *.tbl2)")[0]
        if filename is None or len(filename) == 0:
            return

        self.window.statusBar().showMessage(f'Loading file {filename}')

        self.table = TruthTable(path=filename)

        self.window.statusBar().showMessage(f'Loaded table file "{filename}"')

    def export_table(self):
        pass

    def debug(self):
        print(self.table_out.size())
