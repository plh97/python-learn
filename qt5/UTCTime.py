from PyQt5 import QtGui
from PyQt5.QtCore import QDateTime, QDate, QTime,Qt

datatime = QDateTime.currentDateTime()

print("Local Date And Time Is " + datatime.toString(Qt.DefaultLocaleLongDate))
print("Universal Date And Time Is " + datatime.toUTC().toString())

print("The offset From UTC Is {0}: Seconds ".format(datatime.offset))