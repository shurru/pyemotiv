import guiplot  
import sys
import numpy
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt
from pyemotiv import emotiv

datarray=numpy.zeros((1,4))

class QTEEG(QtCore.QObject, guiplot.Ui_Form): 
    def __init__(self, parent= None): 
        super(QTEEG, self).__init__(parent)
        self.setupUi

    def plotSomething():
        epoc= Epoc()
        data= epoc.aquire([9]) #gets the data from channel O1
        datarray=numpy.concatenate((datarray, data), axis = 1)
        for i in range(0, len(datarray[0])):
            if datarray[0][i]>0:
                sth.append(datarray[0][i])
        
        numPoints=1000
        
        xs=numpy.arange(numPoints)
        #ys=numpy.sin(3.14159*xs*10/numPoints) #this is our data
        #global ys
        ys=numpy.roll(sth,-1) #rolling and repeating
        c.setData(xs,ys)
        guiplot.qwtPlot.replot()   

   # def close(): 
        #enter code to close the headset or atleast stop the functioning of the plot


def main(): 
    app= QtGui.QApplication(sys.argv)
    win_plot = guiplot.QtGui.QMainWindow()
    uiplot = guiplot.Ui_Form()
    uiplot.setupUi(win_plot)

    # tell buttons what to do when clicked
    guiplot.Start.clicked.connect(plotSomething)
    #uiplot.btnA.clicked.connect(plotSomething)

    #guiplot.Stop.clicked.connect(close)
    

    # set up the QwtPlot (pay attention!)
    c=Qwt.QwtPlotCurve()  #make a curve
    c.attach(uiplot.qwtPlot) #attach it to the qwtPlot object
    uiplot.timer = QtCore.QTimer() #start a timer (to call replot events)
    uiplot.timer.start(100.0) #set the interval (in ms)
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething)

    # show the main window
    win_plot.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    