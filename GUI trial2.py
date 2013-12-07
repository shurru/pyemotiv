import sys
from PyQt4 import QtGui, QtCore



class Example(QtGui.QMainWindow):
    #declaring what you want the closeApp to do. create your own signal
    closeApp= QtCore.pyqtSignal()

    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):  

        #allows you to type on the widget
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        #open or save a file in to the folder
        
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        #allows you to create a customized signal 

        self.closeApp.connect(self.close)


        #generates an Exit code.. Can use a shortcut or something to exit
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        #creates an icon which allows you to click and exit
        exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        #Create two buttons which allow you to see which button is pressed using 
        #emitted signals from the pressing of the button

        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)
        # connecting the buttons to the status bar.. 
        # look into whether the button can be used to link another class? 
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)


        #having a status bar in place
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')    
        self.show()
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()

    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                '/home')
        
        f = open(fname, 'r')
        
        with f:        
            data = f.read()
            self.textEdit.setText(data)

    def buttonClicked(self):
      
        sender = self.sender() #sender is called when the button is clicked
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def mousePressEvent(self, event): 

        self.closeApp.emit()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()