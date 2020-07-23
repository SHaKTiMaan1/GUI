import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QSizePolicy,QGraphicsDropShadowEffect,QSizeGrip,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
from PyQt5 import *
import sqlite3

from dash_ma import *
from dash_ma import Ui_MainWindow2
from ui_function import *
from style import Style

class MainWindow():
    def __init__(self):
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.main_window)
        
        
        self.ui.toggle_button.clicked.connect(lambda:UIFunctions.toggleMenu(self,200,True))

       
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Add Dataset", "add_dataset_button","url()")
        UIFunctions.addNewMenu(self, "Attendance", "attendance_button","url(attendance.png)")
        UIFunctions.addNewMenu(self, "In and Out Movement", "in_out_button","url()")
        UIFunctions.addNewMenu(self, "Child Details", "detail_button", "url(cil-description.png)")

        UIFunctions.selectStandardMenu(self, "add_dataset_button")
        self.ui.stackedWidget.setCurrentWidget(self.ui.add_dataset)

        

    def Button(self):
        # GET BT CLICKED
        btnWidget = self.main_window.sender()

        # PAGE HOME
        if btnWidget.objectName() == "add_dataset_button":
            self.ui.stackedWidget.setCurrentWidget(self.ui.add_dataset)
            UIFunctions.resetStyle(self, "add_dataset_button")
            #UIFunctions.labelPage(self, "Add Dataset")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "attendance_button":
            self.ui.stackedWidget.setCurrentWidget(self.ui.attendance)
            UIFunctions.resetStyle(self, "attendance_button")
            #UIFunctions.labelPage(self, "Attendance")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "in_out_button":
            self.ui.stackedWidget.setCurrentWidget(self.ui.in_out)
            UIFunctions.resetStyle(self, "in_out_button")
            #UIFunctions.labelPage(self, "In and out Movement")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        
        if btnWidget.objectName() == "detail_button":
            self.ui.stackedWidget.setCurrentWidget(self.ui.detail)
            UIFunctions.resetStyle(self, "detail_button")
            #UIFunctions.labelPage(self, "Child Details")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
    def show(self):
        self.main_window.show()
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())



    


