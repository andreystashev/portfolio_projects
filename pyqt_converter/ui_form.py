# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Converter(object):
    def setupUi(self, Converter):
        if not Converter.objectName():
            Converter.setObjectName(u"Converter")
        Converter.resize(800, 600)
        self.binButton = QPushButton(Converter)
        self.binButton.setObjectName(u"binButton")
        self.binButton.setGeometry(QRect(20, 210, 151, 81))
        self.binButton.setStyleSheet(u"")
        self.console = QTextBrowser(Converter)
        self.console.setObjectName(u"console")
        self.console.setGeometry(QRect(210, 40, 561, 521))
        self.console.setStyleSheet(u"background-color:black;\n"
"color:white;")
        self.numPanel = QLineEdit(Converter)
        self.numPanel.setObjectName(u"numPanel")
        self.numPanel.setGeometry(QRect(210, 10, 561, 31))
        self.multiplier = QLineEdit(Converter)
        self.multiplier.setObjectName(u"multiplier")
        self.multiplier.setGeometry(QRect(20, 10, 151, 31))
        self.bitButton = QPushButton(Converter)
        self.bitButton.setObjectName(u"bitButton")
        self.bitButton.setGeometry(QRect(20, 300, 151, 81))
        self.hexButton = QPushButton(Converter)
        self.hexButton.setObjectName(u"hexButton")
        self.hexButton.setGeometry(QRect(20, 120, 151, 81))
        self.hexButton.setStyleSheet(u"")
        self.radioBigButton = QRadioButton(Converter)
        self.radioBigButton.setObjectName(u"radioBigButton")
        self.radioBigButton.setGeometry(QRect(30, 490, 99, 31))
        self.radioBigButton.setChecked(True)
        self.radioLittleButton = QRadioButton(Converter)
        self.radioLittleButton.setObjectName(u"radioLittleButton")
        self.radioLittleButton.setGeometry(QRect(30, 530, 99, 31))
        self.mulButton = QPushButton(Converter)
        self.mulButton.setObjectName(u"mulButton")
        self.mulButton.setGeometry(QRect(20, 40, 151, 71))
        self.mulButton.setStyleSheet(u"")

        self.retranslateUi(Converter)

        QMetaObject.connectSlotsByName(Converter)
    # setupUi

    def retranslateUi(self, Converter):
        Converter.setWindowTitle(QCoreApplication.translate("Converter", u"Converter", None))
        self.binButton.setText(QCoreApplication.translate("Converter", u"bin", None))
        self.numPanel.setText(QCoreApplication.translate("Converter", u"787480576", None))
        self.multiplier.setText(QCoreApplication.translate("Converter", u"1", None))
        self.bitButton.setText(QCoreApplication.translate("Converter", u"bit", None))
        self.hexButton.setText(QCoreApplication.translate("Converter", u"hex", None))
        self.radioBigButton.setText(QCoreApplication.translate("Converter", u"Big Endian", None))
        self.radioLittleButton.setText(QCoreApplication.translate("Converter", u"Little Endian", None))
        self.mulButton.setText(QCoreApplication.translate("Converter", u"mul", None))
    # retranslateUi

