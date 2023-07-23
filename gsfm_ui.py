# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gsfm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(356, 260)
        MainWindow.setMinimumSize(QSize(356, 260))
        MainWindow.setMaximumSize(QSize(356, 260))
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 130, 331, 81))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 53, 22))
        self.game_list = QComboBox(self.groupBox)
        self.game_list.setObjectName(u"game_list")
        self.game_list.setGeometry(QRect(70, 20, 251, 22))
        self.s_game = QPushButton(self.groupBox)
        self.s_game.setObjectName(u"s_game")
        self.s_game.setGeometry(QRect(10, 50, 181, 23))
        self.run_b = QPushButton(self.groupBox)
        self.run_b.setObjectName(u"run_b")
        self.run_b.setGeometry(QRect(200, 50, 121, 23))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.run_b.setFont(font)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 40, 331, 81))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 61, 21))
        self.game_f = QLineEdit(self.groupBox_2)
        self.game_f.setObjectName(u"game_f")
        self.game_f.setGeometry(QRect(70, 20, 211, 21))
        self.open_f = QPushButton(self.groupBox_2)
        self.open_f.setObjectName(u"open_f")
        self.open_f.setGeometry(QRect(284, 20, 37, 23))
        self.run_z = QPushButton(self.groupBox_2)
        self.run_z.setObjectName(u"run_z")
        self.run_z.setGeometry(QRect(10, 50, 311, 21))
        self.run_z.setFont(font)
        self.jcyj = QPushButton(self.centralwidget)
        self.jcyj.setObjectName(u"jcyj")
        self.jcyj.setGeometry(QRect(10, 10, 331, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 356, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.log = QStatusBar(MainWindow)
        self.log.setObjectName(u"log")
        MainWindow.setStatusBar(self.log)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GoldSrc-Fix", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u5b98\u7f51", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u4e13\u4e1a\u6a21\u5f0f\uff08\u6b63\u7248 \u4e14 \u975e\u81ea\u5b9a\u4e49\u5e93\u6587\u4ef6\u5939\uff09", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u540d\u79f0\uff1a", None))
        self.s_game.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u6240\u6709\u5e93\u6587\u4ef6\u5939\uff08\u65f6\u95f4\u8f83\u957f\uff09", None))
        self.run_b.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4fee\u8865", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u6a21\u5f0f\uff08\u975e\u6b63\u7248 \u6216 \u81ea\u5b9a\u4e49\u5e93\u6587\u4ef6\u5939\uff09", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u8def\u5f84\uff1a", None))
        self.open_f.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.run_z.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4fee\u8865", None))
        self.jcyj.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u6a21\u5f0f \u4e00\u952e\u4fee\u590d\uff08\u4fee\u590dHalf-Life\uff09", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

