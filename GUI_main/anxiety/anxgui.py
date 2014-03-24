# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\anx_gui.ui'
#
# Created: Wed Mar 19 18:30:37 2014
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
        Form.resize(468, 666)
        self.qwtPlot = Qwt5.QwtPlot(Form)
        self.qwtPlot.setGeometry(QtCore.QRect(10, 20, 421, 241))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 560, 421, 81))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.btn2 = QtGui.QPushButton(self.frame)
        self.btn2.setGeometry(QtCore.QRect(270, 10, 141, 23))
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.Exit = QtGui.QPushButton(self.frame)
        self.Exit.setGeometry(QtCore.QRect(290, 40, 101, 23))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.btn1 = QtGui.QPushButton(self.frame)
        self.btn1.setGeometry(QtCore.QRect(130, 10, 141, 23))
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.chan_check = QtGui.QCheckBox(self.frame)
        self.chan_check.setGeometry(QtCore.QRect(20, 10, 101, 17))
        self.chan_check.setObjectName(_fromUtf8("chan_check"))
        self.save_btn = QtGui.QPushButton(self.frame)
        self.save_btn.setGeometry(QtCore.QRect(140, 40, 141, 23))
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(170, 260, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
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
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn2.setText(_translate("Form", "Stop Recording", None))
        self.Exit.setText(_translate("Form", "Exit", None))
        self.btn1.setText(_translate("Form", "Start Recording", None))
        self.chan_check.setText(_translate("Form", "Change Channel", None))
        self.save_btn.setText(_translate("Form", "Save", None))
        self.label.setText(_translate("Form", "O1 Display", None))
        self.label_3.setText(_translate("Form", "O2 Display", None))
        self.label_5.setText(_translate("Form", "Samples", None))
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

