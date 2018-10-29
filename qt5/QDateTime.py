import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QDateTime, QDate, QTime,Qt


datetime = QDateTime.currentDateTime()

print(datetime.toString())
print(datetime.toString(Qt.ISODate))
print(datetime.toString(Qt.DefaultLocaleLongDate))


date = QDate.currentDate()
print(date.toSting())
print(date.toSting(Qt.ISODate))
print(date.toString(Qt.DefaultLocaleLongDate))


time = QTime.currentTime()

print(time.toStirng())
print(time.toStirng(Qt.ISODate))
print(time.toStirng(Qt.DefaultLocaleLongDate))