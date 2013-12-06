# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created: Fri Dec 06 12:23:58 2013
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
        self.qwtPlot = Qwt5.QwtPlot(Form)
        self.qwtPlot.setGeometry(QtCore.QRect(330, 30, 361, 411))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 301, 421))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 131, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.BatteryLevel = QtGui.QProgressBar(self.frame)
        self.BatteryLevel.setGeometry(QtCore.QRect(10, 110, 151, 21))
        self.BatteryLevel.setProperty("value", 80)
        self.BatteryLevel.setObjectName(_fromUtf8("BatteryLevel"))
        self.Stop = QtGui.QPushButton(self.frame)
        self.Stop.setGeometry(QtCore.QRect(170, 320, 101, 23))
        self.Stop.setObjectName(_fromUtf8("Stop"))
        self.Exit = QtGui.QPushButton(self.frame)
        self.Exit.setGeometry(QtCore.QRect(100, 360, 101, 23))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.Start = QtGui.QPushButton(self.frame)
        self.Start.setGeometry(QtCore.QRect(10, 320, 141, 23))
        self.Start.setObjectName(_fromUtf8("Start"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox = QtGui.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(180, 130, 37, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(181, 157, 37, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 10, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.Start, QtCore.SIGNAL(_fromUtf8("clicked()")), self.qwtPlot.update)
        QtCore.QObject.connect(self.Stop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.qwtPlot.update)
        QtCore.QObject.connect(self.Exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Check Signal Quality", None))
        self.Stop.setText(_translate("Form", "Stop Recording", None))
        self.Exit.setText(_translate("Form", "Exit", None))
        self.Start.setText(_translate("Form", "Start Recording", None))
        self.label_2.setText(_translate("Form", "Battery Level", None))
        self.checkBox.setText(_translate("Form", "O1", None))
        self.checkBox_2.setText(_translate("Form", "O2", None))
        self.label.setText(_translate("Form", "Data Display", None))

from PyQt4 import Qwt5

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

