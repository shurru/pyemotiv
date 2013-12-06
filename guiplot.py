# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created: Fri Dec 06 15:25:10 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(737, 471)
        #QwtPlot which will get the plot refreshed in 

        self.qwtPlot = Qwt5.QwtPlot(Form)
        self.qwtPlot.setGeometry(QtCore.QRect(330, 30, 361, 411))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))

        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 301, 421))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        #Need to check the signal quality. When button clicked, need to show the status of the signal quality
        self.sigqlty = QtGui.QPushButton(self.frame)
        self.sigqlty.setGeometry(QtCore.QRect(0, 10, 131, 23))
        self.sigqlty.setObjectName(_fromUtf8("sigqlty"))

        #Battery level denoted by a progress bar, need to add in the refresh button  
        self.BatteryLevel = QtGui.QProgressBar(self.frame)
        self.BatteryLevel.setGeometry(QtCore.QRect(10, 110, 151, 21))
        self.BatteryLevel.setProperty("value", 80)
        self.BatteryLevel.setObjectName(_fromUtf8("BatteryLevel"))
        self.battlevel = QtGui.QLabel(self.frame)
        self.battlevel.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.battlevel.setObjectName(_fromUtf8("battlevel"))
        self.refreshbattlevel = QtGui.QPushButton(self.frame)
        self.refreshbattlevel.setGeometry(QtCore.QRect(80, 80, 51, 23))
        self.refreshbattlevel.setObjectName(_fromUtf8("refreshbattlevel"))


        #Start and stop push buttons declared
        self.Stop = QtGui.QPushButton(self.frame)
        self.Stop.setGeometry(QtCore.QRect(170, 320, 101, 23))
        self.Stop.setObjectName(_fromUtf8("Stop"))
        self.Exit = QtGui.QPushButton(self.frame)
        self.Exit.setGeometry(QtCore.QRect(100, 360, 101, 23))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.Start = QtGui.QPushButton(self.frame)
        self.Start.setGeometry(QtCore.QRect(10, 320, 141, 23))
        self.Start.setObjectName(_fromUtf8("Start"))

        #Add checkboxes which are supposed to show what happens in O1 and O2        
        self.O1 = QtGui.QCheckBox(self.frame)
        self.O1.setGeometry(QtCore.QRect(9, 193, 37, 17))
        self.O1.setObjectName(_fromUtf8("O1"))
        self.O2 = QtGui.QCheckBox(self.frame)
        self.O2.setGeometry(QtCore.QRect(10, 220, 37, 17))
        self.O2.setObjectName(_fromUtf8("O2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 10, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))

        #Signals which are sent out by the push buttons. Need to redirect them towards the functions we have in the Emotiv EPOC
        self.retranslateUi(Form)
        QtCore.QObject.connect(self.Start, QtCore.SIGNAL(_fromUtf8("clicked()")), self.qwtPlot.update)
        QtCore.QObject.connect(self.Stop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.qwtPlot.update)
        QtCore.QObject.connect(self.Exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QObject.connect(self.refreshbattlevel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.BatteryLevel.update)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.sigqlty.setText(_translate("Form", "Check Signal Quality", None))
        self.Stop.setText(_translate("Form", "Stop Recording", None))
        self.Exit.setText(_translate("Form", "Exit", None))
        self.Start.setText(_translate("Form", "Start Recording", None))
        self.battlevel.setText(_translate("Form", "Battery Level", None))
        self.refreshbattlevel.setText(_translate("Form", "Refresh", None))
        self.O1.setText(_translate("Form", "O1", None))
        self.O2.setText(_translate("Form", "O2", None))
        self.label.setText(_translate("Form", "Data Display", None))

from PyQt4 import Qwt5
