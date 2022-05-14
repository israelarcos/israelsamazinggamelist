# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_game_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class EditGameForm(object):
    def setupUi(self, editGameWindow):
        if not editGameWindow.objectName():
            editGameWindow.setObjectName(u"editGameWindow")
        editGameWindow.resize(405, 504)
        self.label = QLabel(editGameWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(editGameWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.titleLineEdit = QLineEdit(editGameWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.categoryLineEdit = QLineEdit(editGameWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(30, 130, 351, 20))
        self.label_3 = QLabel(editGameWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 13))
        self.label_4 = QLabel(editGameWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 61, 13))
        self.durationSpinBox = QSpinBox(editGameWindow)
        self.durationSpinBox.setObjectName(u"durationSpinBox")
        self.durationSpinBox.setGeometry(QRect(30, 180, 101, 22))
        self.label_5 = QLabel(editGameWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 250, 61, 13))
        self.filePathLineEdit = QLineEdit(editGameWindow)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setGeometry(QRect(30, 270, 181, 20))
        self.selectFileButton = QPushButton(editGameWindow)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(230, 270, 75, 23))
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
        self.label_6 = QLabel(editGameWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 310, 71, 16))
        self.descriptiontextEdit = QTextEdit(editGameWindow)
        self.descriptiontextEdit.setObjectName(u"descriptiontextEdit")
        self.descriptiontextEdit.setGeometry(QRect(30, 330, 351, 111))
        self.editButton = QPushButton(editGameWindow)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(94, 460, 101, 31))
        self.editButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton.setStyleSheet(u"QPushButton\n"
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
        icon1.addFile(u"../assets/edit-game.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.editButton.setIcon(icon1)
        self.editButton.setIconSize(QSize(30, 30))
        self.editButton.setFlat(True)
        self.addButton_2 = QPushButton(editGameWindow)
        self.addButton_2.setObjectName(u"addButton_2")
        self.addButton_2.setGeometry(QRect(210, 460, 101, 31))
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
        self.durationSpinBox_2 = QSpinBox(editGameWindow)
        self.durationSpinBox_2.setObjectName(u"durationSpinBox_2")
        self.durationSpinBox_2.setGeometry(QRect(170, 180, 101, 22))
        self.label_7 = QLabel(editGameWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 160, 71, 16))

        self.retranslateUi(editGameWindow)

        QMetaObject.connectSlotsByName(editGameWindow)
    # setupUi

    def retranslateUi(self, editGameWindow):
        editGameWindow.setWindowTitle(QCoreApplication.translate("editGameWindow", u"Edit Game", None))
        self.label.setText(QCoreApplication.translate("editGameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">EDIT GAME</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("editGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Title</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("editGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Category<br/></span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("editGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Duration</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("editGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Select file</span></p><p><br/></p></body></html>", None))
        self.selectFileButton.setText("")
        self.label_6.setText(QCoreApplication.translate("editGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Description</span></p><p><br/></p></body></html>", None))
        self.editButton.setText(QCoreApplication.translate("editGameWindow", u"EDIT", None))
        self.addButton_2.setText(QCoreApplication.translate("editGameWindow", u"CANCEL", None))
        self.label_7.setText(QCoreApplication.translate("editGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Time played</span></p></body></html>", None))
    # retranslateUi

