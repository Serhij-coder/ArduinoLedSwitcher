# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(357, 136)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.conect = QPushButton(self.centralwidget)
        self.conect.setObjectName(u"conect")

        self.horizontalLayout.addWidget(self.conect)

        self.diskonect = QPushButton(self.centralwidget)
        self.diskonect.setObjectName(u"diskonect")

        self.horizontalLayout.addWidget(self.diskonect)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.port = QComboBox(self.centralwidget)
        self.port.setObjectName(u"port")

        self.verticalLayout.addWidget(self.port)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.speed = QComboBox(self.centralwidget)
        self.speed.setObjectName(u"speed")

        self.verticalLayout_2.addWidget(self.speed)

        self.onoff = QRadioButton(self.centralwidget)
        self.onoff.setObjectName(u"onoff")

        self.verticalLayout_2.addWidget(self.onoff)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.conect.setText(QCoreApplication.translate("MainWindow", u"CONECT", None))
        self.diskonect.setText(QCoreApplication.translate("MainWindow", u"DISKONECT", None))
        self.onoff.setText(QCoreApplication.translate("MainWindow", u"ON/OFF", None))
    # retranslateUi

