import sys
from PyQt4 import QtGui, QtCore
import numpy
class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colors')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
      
        for i in xrange(0,100): 
            rand= numpy.random.randint(80, 100)
            qp.setBrush(QtGui.QColor(255, 80, 0, 160))
            qp.drawRect(130, rand, 90, rand)
            print rand
            

     

        #
              
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()