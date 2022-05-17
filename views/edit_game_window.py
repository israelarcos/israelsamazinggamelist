# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_game_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class EditGameForm(object):
    def setupUi(self, EditGameWindow):
        if not EditGameWindow.objectName():
            EditGameWindow.setObjectName(u"EditGameWindow")
        EditGameWindow.resize(405, 536)
        EditGameWindow.setCursor(QCursor(Qt.PointingHandCursor))
        self.label = QLabel(EditGameWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(EditGameWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.titleLineEdit = QLineEdit(EditGameWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(EditGameWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 13))
        self.categoryLineEdit = QLineEdit(EditGameWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(30, 130, 271, 20))
        self.label_4 = QLabel(EditGameWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 121, 16))
        self.durationSpinBox = QSpinBox(EditGameWindow)
        self.durationSpinBox.setObjectName(u"durationSpinBox")
        self.durationSpinBox.setGeometry(QRect(30, 180, 101, 22))
        self.label_5 = QLabel(EditGameWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 270, 121, 16))
        self.filePathLineEdit = QLineEdit(EditGameWindow)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setGeometry(QRect(30, 290, 191, 20))
        self.selectFileButton = QPushButton(EditGameWindow)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(230, 290, 31, 31))
        self.selectFileButton.setStyleSheet(u"\n"
"QPushButton:hover\n"
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
        icon.addFile(u"./assets/icons/select-file.icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectFileButton.setIcon(icon)
        self.selectFileButton.setIconSize(QSize(30, 30))
        self.selectFileButton.setFlat(True)
        self.label_6 = QLabel(EditGameWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 340, 121, 16))
        self.descriptionTextedit = QTextEdit(EditGameWindow)
        self.descriptionTextedit.setObjectName(u"descriptionTextedit")
        self.descriptionTextedit.setGeometry(QRect(30, 360, 351, 111))
        self.editButton = QPushButton(EditGameWindow)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(94, 490, 101, 31))
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
        icon1.addFile(u"./assets/icons/edit-game.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editButton.setIcon(icon1)
        self.editButton.setIconSize(QSize(30, 30))
        self.editButton.setFlat(True)
        self.cancelButton = QPushButton(EditGameWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(200, 490, 101, 31))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton\n"
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
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setFlat(True)
        self.label_7 = QLabel(EditGameWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 220, 161, 16))
        self.playedtimeSpinBox = QSpinBox(EditGameWindow)
        self.playedtimeSpinBox.setObjectName(u"playedtimeSpinBox")
        self.playedtimeSpinBox.setGeometry(QRect(30, 240, 101, 22))

        self.retranslateUi(EditGameWindow)

        QMetaObject.connectSlotsByName(EditGameWindow)
    # setupUi

    def retranslateUi(self, EditGameWindow):
        EditGameWindow.setWindowTitle(QCoreApplication.translate("EditGameWindow", u"Edit game", None))
        self.label.setText(QCoreApplication.translate("EditGameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">EDIT GAME</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("EditGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Title</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("EditGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Category</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("EditGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Duration</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("EditGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Select file</span></p></body></html>", None))
        self.selectFileButton.setText("")
        self.label_6.setText(QCoreApplication.translate("EditGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Game's description</span></p></body></html>", None))
        self.editButton.setText(QCoreApplication.translate("EditGameWindow", u"EDIT", None))
        self.cancelButton.setText(QCoreApplication.translate("EditGameWindow", u"CANCEL", None))
        self.label_7.setText(QCoreApplication.translate("EditGameWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Played time</span></p></body></html>", None))
    # retranslateUi

