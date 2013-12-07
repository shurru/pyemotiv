import sys 
from PyQt4 import QtGui, QtCore

#how do we integrate different widgets into a single GUI? 

#able to create different classes for the GUI itself (need to know how to get it to work with PyEmotiv)
class Example2(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example2, self).__init__()
        self.initUI()
        
    def initUI(self):  

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.show()
       

       
class Example (QtGui.QWidget): #inherits from QtGUI and QWidget Classes
	def __init__(self): 
		super(Example, self).__init__()
		self.initUI()

	def initUI(self): 

		self.resize(500, 500)
		self.center()

		#printing out pictures on the pretty GUI.

		hbox= QtGui.QHBoxLayout(self)
		pixmap= QtGui.QPixmap("trollWifi.png") #allows the printing of the image

		lbl= QtGui.QLabel(self)
		lbl.setPixmap(pixmap)
		hbox.addWidget(lbl)
		self.setLayout(hbox)

		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10 ))
		#self.setToolTip('This is a <b> QWidget</b> widget')

		

		#define all buttons

		btn= QtGui.QPushButton('Start',self) #declaration of buttons
		btn.setToolTip('Start collecting data') #what it shows when we hover
		btn.resize(btn.sizeHint()) #button gets resized and moved
		btn.move(10, 400)  #positioning of the button
		#need to figure out how to connect this with the trial.py -> collect the data



		#a button which lets you quit the window itself
		qbtn= QtGui.QPushButton('Quit', self)
		#when button is clicked, it sends a signal 'Clicked'
		#instance gives you the current instance
		qbtn.clicked.connect(QtCore.QCoreApplication. instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(50,50)



		self.setGeometry(300, 300, 500,500) #detects the location and sets the size
		self.setWindowTitle('GUI')
		#self.setWindowIcon(QtGui.QIcon('web.png'))

		self.show()

	def keyPressEvent(self, e): 
		if e.key()== QtCore.Qt.Key_Escape: 
			self.close()

	

	def center(self): 
		qr= self.frameGeometry()
		cp= QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def closeEvent(self, event): 
		#when you close a QT wiedge, it generates a QT Close Event
		reply= QtGui.QMessageBox.question(self, 'Message', "are you sure you want to quit? " 
				,QtGui.QMessageBox.Yes| QtGui.QMessageBox.No, QtGui.QMessageBox.No)
					#last one is the default option
		if reply== QtGui.QMessageBox.Yes: 
			event.accept()
		else: 
			event.ignore()


def main(): 
	app = QtGui.QApplication(sys.argv)
	
	ex= Example()
	#ex1= Example2()


	#w = QtGui.QWidget()
	#w.resize(250, 150) #allows us to resize the size of the window
	#w.move(300, 300) #allows movement of the screen 
	#w.setWindowTitle('GUI')
	#w.show()

	sys.exit(app.exec_()) #exec is a python keyword; use exec_ instead. Quits main

if __name__== '__main__': 
	main()