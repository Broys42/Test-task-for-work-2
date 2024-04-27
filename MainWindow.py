# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 699)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_pageTitle = QLabel(self.frame)
        self.label_pageTitle.setObjectName(u"label_pageTitle")
        font = QFont()
        font.setPointSize(20)
        self.label_pageTitle.setFont(font)
        self.label_pageTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_pageTitle)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView_resultsOfAthletes = QTableView(self.frame_2)
        self.tableView_resultsOfAthletes.setObjectName(u"tableView_resultsOfAthletes")

        self.verticalLayout_2.addWidget(self.tableView_resultsOfAthletes)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_uploadAthletes = QPushButton(self.frame_3)
        self.btn_uploadAthletes.setObjectName(u"btn_uploadAthletes")

        self.horizontalLayout.addWidget(self.btn_uploadAthletes)

        self.btn_uploadResults = QPushButton(self.frame_3)
        self.btn_uploadResults.setObjectName(u"btn_uploadResults")

        self.horizontalLayout.addWidget(self.btn_uploadResults)

        self.btn_calculateResults = QPushButton(self.frame_3)
        self.btn_calculateResults.setObjectName(u"btn_calculateResults")

        self.horizontalLayout.addWidget(self.btn_calculateResults)

        self.btn_saveResults = QPushButton(self.frame_3)
        self.btn_saveResults.setObjectName(u"btn_saveResults")

        self.horizontalLayout.addWidget(self.btn_saveResults)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_filesNameOfAthletes = QLabel(self.frame_4)
        self.label_filesNameOfAthletes.setObjectName(u"label_filesNameOfAthletes")

        self.horizontalLayout_2.addWidget(self.label_filesNameOfAthletes)

        self.label_filesNameOfResults = QLabel(self.frame_4)
        self.label_filesNameOfResults.setObjectName(u"label_filesNameOfResults")

        self.horizontalLayout_2.addWidget(self.label_filesNameOfResults)


        self.verticalLayout.addWidget(self.frame_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_pageTitle.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0441\u043f\u043e\u0440\u0442\u0441\u043c\u0435\u043d\u043e\u0432", None))
        self.btn_uploadAthletes.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u043f\u043e\u0440\u0442\u0441\u043c\u0435\u043d\u043e\u0432", None))
        self.btn_uploadResults.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.btn_calculateResults.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.btn_saveResults.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.label_filesNameOfAthletes.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0441\u043f\u043e\u0440\u0442\u0441\u043c\u0435\u043d\u043e\u0432:", None))
        self.label_filesNameOfResults.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432:", None))
    # retranslateUi
