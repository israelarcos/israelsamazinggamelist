# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_game_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class newGameForm(object):
    def setupUi(self, newGameWindow):
        if not newGameWindow.objectName():
            newGameWindow.setObjectName(u"newGameWindow")
        newGameWindow.resize(405, 472)
        self.label = QLabel(newGameWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(newGameWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.titleLineEdit = QLineEdit(newGameWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.categoryLineEdit = QLineEdit(newGameWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(30, 130, 351, 20))
        self.label_3 = QLabel(newGameWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 13))
        self.label_4 = QLabel(newGameWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 61, 13))
        self.durationSpinBox = QSpinBox(newGameWindow)
        self.durationSpinBox.setObjectName(u"durationSpinBox")
        self.durationSpinBox.setGeometry(QRect(30, 180, 101, 22))
        self.label_5 = QLabel(newGameWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 220, 61, 13))
        self.filePathLineEdit = QLineEdit(newGameWindow)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setGeometry(QRect(30, 240, 181, 20))
        self.selectFileButton = QPushButton(newGameWindow)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(230, 240, 75, 23))
        self.selectFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectFileButton.setStyleSheet(u"QPushButton:hover\n"
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
        icon.addFile(u"../assets/select-file.icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectFileButton.setIcon(icon)
        self.selectFileButton.setIconSize(QSize(30, 30))
        self.selectFileButton.setFlat(True)
        self.label_6 = QLabel(newGameWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 280, 71, 16))
        self.descriptiontextEdit = QTextEdit(newGameWindow)
        self.descriptiontextEdit.setObjectName(u"descriptiontextEdit")
        self.descriptiontextEdit.setGeometry(QRect(30, 300, 351, 111))
        self.addButton = QPushButton(newGameWindow)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(94, 430, 101, 31))
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../assets/add-game-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setFlat(True)
        self.addButton_2 = QPushButton(newGameWindow)
        self.addButton_2.setObjectName(u"addButton_2")
        self.addButton_2.setGeometry(QRect(210, 430, 101, 31))
        self.addButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_2.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        self.addButton_2.setIconSize(QSize(30, 30))
        self.addButton_2.setFlat(True)

        self.retranslateUi(newGameWindow)

        QMetaObject.connectSlotsByName(newGameWindow)
    # setupUi

    def retranslateUi(self, newGameWindow):
        newGameWindow.setWindowTitle(QCoreApplication.translate("newGameWindow", u"New Game", None))
        self.label.setText(QCoreApplication.translate("newGameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">NEW GAME</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("newGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Title</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("newGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Category<br/></span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("newGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Duration</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("newGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Select file</span></p><p><br/></p></body></html>", None))
        self.selectFileButton.setText("")
        self.label_6.setText(QCoreApplication.translate("newGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Description</span></p><p><br/></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("newGameWindow", u"ADD", None))
        self.addButton_2.setText(QCoreApplication.translate("newGameWindow", u"CANCEL", None))
    # retranslateUi

