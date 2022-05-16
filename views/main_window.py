# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ListGameForm(object):
    def setupUi(self, ListGameForm):
        if not ListGameForm.objectName():
            ListGameForm.setObjectName(u"ListGameForm")
        ListGameForm.resize(961, 550)
        ListGameForm.setCursor(QCursor(Qt.ArrowCursor))
        self.buttonsFrame = QFrame(ListGameForm)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setGeometry(QRect(10, 10, 943, 91))
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.openGameButton = QPushButton(self.buttonsFrame)
        self.openGameButton.setObjectName(u"openGameButton")
        self.openGameButton.setGeometry(QRect(20, 10, 71, 51))
        self.openGameButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.openGameButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../assets/open-game-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openGameButton.setIcon(icon)
        self.openGameButton.setIconSize(QSize(50, 50))
        self.openGameButton.setFlat(True)
        self.label = QLabel(self.buttonsFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 91, 21))
        self.newGameButton = QPushButton(self.buttonsFrame)
        self.newGameButton.setObjectName(u"newGameButton")
        self.newGameButton.setGeometry(QRect(110, 10, 71, 51))
        self.newGameButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.newGameButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../assets/add-game-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newGameButton.setIcon(icon1)
        self.newGameButton.setIconSize(QSize(50, 50))
        self.newGameButton.setFlat(True)
        self.label_2 = QLabel(self.buttonsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 60, 91, 21))
        self.label_3 = QLabel(self.buttonsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 60, 91, 21))
        self.editGameButton = QPushButton(self.buttonsFrame)
        self.editGameButton.setObjectName(u"editGameButton")
        self.editGameButton.setGeometry(QRect(190, 10, 71, 51))
        self.editGameButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editGameButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../assets/edit-game.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.editGameButton.setIcon(icon2)
        self.editGameButton.setIconSize(QSize(50, 50))
        self.editGameButton.setFlat(True)
        self.deleteGameButton = QPushButton(self.buttonsFrame)
        self.deleteGameButton.setObjectName(u"deleteGameButton")
        self.deleteGameButton.setGeometry(QRect(280, 10, 71, 51))
        self.deleteGameButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteGameButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../assets/delete-game-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteGameButton.setIcon(icon3)
        self.deleteGameButton.setIconSize(QSize(50, 50))
        self.deleteGameButton.setFlat(True)
        self.label_4 = QLabel(self.buttonsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 60, 91, 21))
        self.frame = QFrame(ListGameForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 110, 941, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.searchbyComboBox = QComboBox(self.frame)
        self.searchbyComboBox.setObjectName(u"searchbyComboBox")
        self.searchbyComboBox.setGeometry(QRect(70, 10, 161, 22))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 71, 16))
        self.parameterLineEdit = QLineEdit(self.frame)
        self.parameterLineEdit.setObjectName(u"parameterLineEdit")
        self.parameterLineEdit.setGeometry(QRect(240, 10, 411, 20))
        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(660, 10, 131, 25))
        icon4 = QIcon()
        icon4.addFile(u"../assets/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon4)
        self.refreshButton = QPushButton(self.frame)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(800, 10, 131, 25))
        icon5 = QIcon()
        icon5.addFile(u"../assets/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon5)
        self.listGamesTable = QTableWidget(ListGameForm)
        self.listGamesTable.setObjectName(u"listGamesTable")
        self.listGamesTable.setGeometry(QRect(10, 160, 941, 341))
        self.label_6 = QLabel(ListGameForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 510, 81, 16))
        self.gameQtyLabel = QLabel(ListGameForm)
        self.gameQtyLabel.setObjectName(u"gameQtyLabel")
        self.gameQtyLabel.setGeometry(QRect(100, 510, 47, 13))
        self.frame.raise_()
        self.buttonsFrame.raise_()
        self.listGamesTable.raise_()
        self.label_6.raise_()
        self.gameQtyLabel.raise_()

        self.retranslateUi(ListGameForm)

        QMetaObject.connectSlotsByName(ListGameForm)
    # setupUi

    def retranslateUi(self, ListGameForm):
        ListGameForm.setWindowTitle(QCoreApplication.translate("ListGameForm", u"Israel's Amazing Gamelist", None))
        self.openGameButton.setText("")
        self.label.setText(QCoreApplication.translate("ListGameForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Open Game</span></p></body></html>", None))
        self.newGameButton.setText("")
        self.label_2.setText(QCoreApplication.translate("ListGameForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">New Game</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ListGameForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Edit Game</span></p></body></html>", None))
        self.editGameButton.setText("")
        self.deleteGameButton.setText("")
        self.label_4.setText(QCoreApplication.translate("ListGameForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Delete Game</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("ListGameForm", u"Search for:", None))
        self.searchButton.setText(QCoreApplication.translate("ListGameForm", u"SEARCH", None))
        self.refreshButton.setText(QCoreApplication.translate("ListGameForm", u"REFRESH", None))
        self.label_6.setText(QCoreApplication.translate("ListGameForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Game count:</span></p></body></html>", None))
        self.gameQtyLabel.setText(QCoreApplication.translate("ListGameForm", u"#", None))
    # retranslateUi

