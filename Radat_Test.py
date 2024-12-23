
##########################################################
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTableWidgetItem
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import numpy as np


#Віджет#
app = QtWidgets.QApplication([]) #Створюю додаток
ui = uic.loadUi("Wind_Radar.ui") #Завантажую інтерфейс
ui.setWindowTitle("Ultrasonic Radar") # Назві вікна


baudRate = 115200 #Змінна для швидкості порту
serial = QSerialPort() #Створюю порт
serial.setBaudRate(baudRate) #Встановлюю Boot


import Radat_MatPlot
def open_radar(): #Функція для відкриття радара
    # Radat_MatPlot
    Radat_MatPlot.plt.show()#Відкриваю вікно радара
ui.Button_Radar.clicked.connect(open_radar) #Кнопка радара


def slider_radar(val):
    # Radat_MatPlot.np.arange(0, 180, 0.5)
    print(val)
    ui.Lcd_Angle.display(val)
ui.Slider_Servo.valueChanged.connect(slider_radar)


def connect_port(): #Функція з'єднання з портом
    serial.setPortName(ui.comboBox_Ports.currentText()) #Підставляю ім'я порту з comboBox
    serial.open(QIODevice.ReadWrite) #Відкриваю вибраний порт для читання і запису
    print("Connect")
ui.Button_Connect.clicked.connect(connect_port) #Кнопка з'єднання


def close_port(): #Функція закриття порту
    serial.close() #Закриваю порт
    print("Close")
ui.Button_Close.clicked.connect(close_port) #Кнопка закриття порту



portList = [] #Список для портів
def refresh_port(): #Функція оновлення списку портів
    ports = QSerialPortInfo().availablePorts() #Список портів
    for port in ports: portList.append(port.portName()) #Читаю список портів і записую в список
    ui.comboBox_Ports.addItems(portList) #Добавляю в comboBox
    print("Refresh")
refresh_port() #Добавляю в comboBox при запуску
ui.Button_Refresh.clicked.connect(refresh_port) #Кнопка оновлення списку портів


def read_port(): #Функція читання порту
    s_r = serial.readLine() #Читаю порт по лініях і записую в змінну
    data = str(s_r, 'utf-8').strip() #Декодую перетворивши в рядок
    print(data)
serial.readyRead.connect(read_port) #Якцо є вхідні дані то викликаю функцію читання порту


def serial_send(data): #Функція для надсилання даних (список int)
    txs = "" #Змінна для вихідного рядка
    for val in data: #Цикл для додаваня коми між значеннями
        txs += str(val) #Додаю значення
        txs += "," #Додаю кому
    txs = txs[:-1] #Видаляю останню кому в рядку
    txs += ";" #Добавляю крапку з комою
    serial.write(txs.encode()) #Відправляю в порт рядок txs
    print(txs)
# serial_send([0,1])




def laser_control(val):
    if val == 2:
        val = 1
    serial_send([1, val])
    # print(f"Laser OK {val}")

ui.checkBox_Laser.stateChanged.connect(laser_control)

def Led_control(val):
    if val == 2:
        val = 1
    serial_send([2, val])
    # print(f"Led OK {val}")

ui.checkBox_Led_1.stateChanged.connect(Led_control)
















ui.show() #Створення інтерфуйсу
app.exec() #Запуск додатку