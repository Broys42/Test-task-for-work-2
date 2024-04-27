import os

from MainWindow import Ui_MainWindow
from ViewModel import ViewModel
from Result import Result

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItem, QStandardItemModel)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget, QFileDialog)

class MainWindowUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class View():
    def __init__(self, viewModel: ViewModel):
        self.mainWindow = MainWindowUI()
        self.connect_Buttons_Events()
        self.viewModel = viewModel
        self.table_Model = QStandardItemModel()

    def show(self):
        self.mainWindow.show()

    def connect_Buttons_Events(self):
        self.mainWindow.btn_calculateResults.clicked.connect(self.onClicked_btn_calculateResults)
        self.mainWindow.btn_saveResults.clicked.connect(self.onClicked_btn_saveResults)
        self.mainWindow.btn_uploadAthletes.clicked.connect(self.onClicked_btn_uploadAthletes)
        self.mainWindow.btn_uploadResults.clicked.connect(self.onClicked_btn_uploadResults)

    def onClicked_btn_calculateResults(self):
        self.create_Athletes()
        self.viewModel.calculate_Tooked_Places_By_Athletes()
        self.make_sorted_Athletes_Model()

    def onClicked_btn_saveResults(self):
        self.save_File_Of_Athletes()

    def onClicked_btn_uploadAthletes(self):
        self.open_File_Of_Athletes()

    def onClicked_btn_uploadResults(self):
        self.open_File_Of_Results()

    def open_File_Of_Athletes(self):
        file_filter = "Json (*.json)"
        response = QFileDialog.getOpenFileName(
            parent=self.mainWindow,
            caption='Select a file',
            dir=os.getcwd(),
            filter=file_filter,
        )

        if response[0]:
            self.viewModel.change_Selected_File_Of_Athletes(response[0])
            self.mainWindow.label_filesNameOfAthletes.setText(f"Таблица спортсменов: {response[0]}")
        else:
            self.viewModel.change_Selected_File_Of_Athletes("")
            self.mainWindow.label_filesNameOfAthletes.setText("Таблица спортсменов: Файл спортсменов не выбран")

    def save_File_Of_Athletes(self):
        file_filter = "Json (*.json)"
        response = QFileDialog.getSaveFileName(
            parent=self.mainWindow,
            caption='Select a file',
            dir=os.getcwd(),
            filter=file_filter,
        )

        if response[0]:
            self.viewModel.save_File_Of_Athletes(response[0])

    def open_File_Of_Results(self):
        file_filter = "Txt (*.txt)"
        response = QFileDialog.getOpenFileName(
            parent=self.mainWindow,
            caption='Select a file',
            dir=os.getcwd(),
            filter=file_filter,
        )

        if response[0]:
            self.viewModel.change_Selected_File_Of_Results(response[0])
            self.mainWindow.label_filesNameOfResults.setText(f"Таблица результатов: {response[0]}")
        else:
            self.viewModel.change_Selected_File_Of_Results("")
            self.mainWindow.label_filesNameOfResults.setText("Таблица результатов: Файл спортсменов не выбран")

    def create_Athletes(self):
        self.viewModel.create_Athletes()

    def make_sorted_Athletes_Model(self):
        self.table_Model.clear()
        for item in self.viewModel.make_Sorted_Athletes_Model():
            self.table_Model.appendRow(item)

        self.header = ["Занятое место", "Нагрудный номер", "Имя", "Фамилия", "Результат"]
        self.table_Model.setHorizontalHeaderLabels(self.header)
        self.mainWindow.tableView_resultsOfAthletes.setModel(self.table_Model)
