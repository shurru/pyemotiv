# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI_change.ui'
#
# Created: Mon Jan 27 10:45:59 2014
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
        Form.resize(1330, 701)
        self.qwtPlot = Qwt5.QwtPlot(Form)
        self.qwtPlot.setGeometry(QtCore.QRect(10, 20, 421, 241))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 540, 551, 131))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 131, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.BatteryLevel = QtGui.QProgressBar(self.frame)
        self.BatteryLevel.setGeometry(QtCore.QRect(0, 60, 151, 21))
        self.BatteryLevel.setProperty("value", 80)
        self.BatteryLevel.setObjectName(_fromUtf8("BatteryLevel"))
        self.btn2 = QtGui.QPushButton(self.frame)
        self.btn2.setGeometry(QtCore.QRect(250, 40, 141, 23))
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.Exit = QtGui.QPushButton(self.frame)
        self.Exit.setGeometry(QtCore.QRect(360, 70, 101, 23))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.btn1 = QtGui.QPushButton(self.frame)
        self.btn1.setGeometry(QtCore.QRect(250, 10, 141, 23))
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 90, 51, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.btn3 = QtGui.QPushButton(self.frame)
        self.btn3.setGeometry(QtCore.QRect(400, 10, 141, 21))
        self.btn3.setObjectName(_fromUtf8("btn3"))
        self.filter_check = QtGui.QCheckBox(self.frame)
        self.filter_check.setGeometry(QtCore.QRect(139, 10, 71, 20))
        self.filter_check.setObjectName(_fromUtf8("filter_check"))
        self.chan_check = QtGui.QCheckBox(self.frame)
        self.chan_check.setGeometry(QtCore.QRect(140, 30, 101, 17))
        self.chan_check.setObjectName(_fromUtf8("chan_check"))
        self.save_btn = QtGui.QPushButton(self.frame)
        self.save_btn.setGeometry(QtCore.QRect(400, 40, 141, 23))
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.qwtPlot_2 = Qwt5.QwtPlot(Form)
        self.qwtPlot_2.setGeometry(QtCore.QRect(440, 20, 421, 241))
        self.qwtPlot_2.setObjectName(_fromUtf8("qwtPlot_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(870, 20, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(170, 260, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(620, 260, 51, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.qwtPlot_3 = Qwt5.QwtPlot(Form)
        self.qwtPlot_3.setGeometry(QtCore.QRect(870, 40, 391, 241))
        self.qwtPlot_3.setObjectName(_fromUtf8("qwtPlot_3"))
        self.painedit = QtGui.QLineEdit(Form)
        self.painedit.setGeometry(QtCore.QRect(1130, 10, 113, 20))
        self.painedit.setObjectName(_fromUtf8("painedit"))
        self.qwtPlot_5 = Qwt5.QwtPlot(Form)
        self.qwtPlot_5.setGeometry(QtCore.QRect(440, 300, 421, 221))
        self.qwtPlot_5.setObjectName(_fromUtf8("qwtPlot_5"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(630, 520, 51, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.painedit_2 = QtGui.QLineEdit(Form)
        self.painedit_2.setGeometry(QtCore.QRect(1150, 300, 113, 20))
        self.painedit_2.setObjectName(_fromUtf8("painedit_2"))
        self.qwtPlot_6 = Qwt5.QwtPlot(Form)
        self.qwtPlot_6.setGeometry(QtCore.QRect(870, 330, 391, 211))
        self.qwtPlot_6.setObjectName(_fromUtf8("qwtPlot_6"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(870, 310, 101, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.qwtPlot_4 = Qwt5.QwtPlot(Form)
        self.qwtPlot_4.setGeometry(QtCore.QRect(10, 300, 421, 221))
        self.qwtPlot_4.setObjectName(_fromUtf8("qwtPlot_4"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(180, 520, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.qwtPlot.update)
        QtCore.QObject.connect(self.btn2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.qwtPlot.update)
        QtCore.QObject.connect(self.Exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "GUI", None))
        self.pushButton.setText(_translate("Form", "Check Signal Quality", None))
        self.btn2.setText(_translate("Form", "Stop Recording", None))
        self.Exit.setText(_translate("Form", "Exit", None))
        self.btn1.setText(_translate("Form", "Start Recording", None))
        self.label_2.setText(_translate("Form", "Battery Level", None))
        self.pushButton_2.setText(_translate("Form", "Refresh", None))
        self.btn3.setText(_translate("Form", "FFT", None))
        self.filter_check.setText(_translate("Form", "Filter", None))
        self.chan_check.setText(_translate("Form", "Change Channel", None))
        self.save_btn.setText(_translate("Form", "Save", None))
        self.label.setText(_translate("Form", "O1 Display", None))
        self.label_3.setText(_translate("Form", "O2 Display", None))
        self.label_4.setText(_translate("Form", "Alpha Power O1", None))
        self.label_5.setText(_translate("Form", "Samples", None))
        self.label_6.setText(_translate("Form", "Frequency", None))
        self.label_8.setText(_translate("Form", "Frequency", None))
        self.label_9.setText(_translate("Form", "Alpha Power O2", None))
        self.label_7.setText(_translate("Form", "Samples", None))

from PyQt4 import Qwt5

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

