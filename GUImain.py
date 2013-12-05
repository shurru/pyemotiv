from PyQt4 import QtCore, QtGui, Qwt5
from PyQt4.Qwt5 import QwtPlot
import sys 

try: 
	_fromUtf8= QtCore.QString.fromUtf8
except AttributeError: 
	def _fromUtf8(s): 
		return s 

try: 
	_encoding= QtGui.QApplication.UnicodeUTF8
	def translate(context, text, disambig): 
		return QtGui.QApplication.translate(context, text, disambig)
except AttributeError: 
	def translate(context, text, disambig): 
		return QtGui.QApplication.translate(context,text,disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.eegPlot = QwtPlot(self.centralwidget)
        self.eegPlot.setGeometry(QtCore.QRect(30, 20, 411, 411))
        self.eegPlot.setObjectName(_fromUtf8("EEG Plot"))
        self.startEEG = QtGui.QPushButton(self.centralwidget)
        self.startEEG.setGeometry(QtCore.QRect(460, 370, 87, 27))
        self.startEEG.setObjectName(_fromUtf8("Start EEG"))
        self.stopEEG = QtGui.QPushButton(self.centralwidget)
        self.stopEEG.setGeometry(QtCore.QRect(580, 370, 87, 27))
        self.stopEEG.setObjectName(_fromUtf8("Stop EEG"))
        self.signal= QtGui.QPushButton("Signal")
        self.signal.setGeometry(QtCore.QRect(600, 370, 87, 27))
        self.signal.setObjectName(_fromUtf8("Check Signal"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 24))
        self.menubar.setObjectName(_fromUtf8("MenuBar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("StatusBar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(translate("MainWindow", "MainWindow", None))
        self.startEEG.setText(translate("MainWindow", "Start", None))
        self.stopEEG.setText(translate("MainWindow", "Stop", None))


	
