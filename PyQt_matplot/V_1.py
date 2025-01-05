from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTableWidgetItem
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys
import csv


#Віджет#
app = QtWidgets.QApplication([])
ui = uic.loadUi("Wnd.ui")



ui.show() #Створення інтерфуйсу
app.exec() #Запуск додатку