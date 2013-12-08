import ui_plot
from recorder import *
import sys
import numpy
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt
from pyemotiv import Epoc 


#epoc=Epoc()

def plotSomething():
    if epoc.newRecord==False: 
        return
    #how do I get the code in here? Need to print the raw EEG data 
    #click a button and it stops updating it
    #click another button. it generates FFT signal
    #print "\n Plotting"
    xs,ys=epoc.rawdata()
    #print ys
    c.setData(xs,ys)
    uiplot.qwtPlot.replot()
    epoc.newRecord=False

def fftplot(): 
    if epoc.newRecord==False: 
        return 

    pwr,freq= epoc.fft()
    c.setData(pwr,freq)
    uiplot.qwtplot.replot()
    epoc.newRecord=False





def main(): 
    app = QtGui.QApplication(sys.argv)
    global epoc
    global c
    global uiplot

    epoc=EEGRecorder()
    
    #epoc.setup
    #print"boom"
    epoc.continuousStart() #should start the record function
    #print "Hi"

    win_plot = ui_plot.QtGui.QMainWindow()
    uiplot = ui_plot.Ui_win_plot()
    uiplot.setupUi(win_plot)
   #uiplot.btnA.clicked.connect(restart)
    uiplot.btnB.clicked.connect(epoc.continuousEnd) #when buttonB is clicked, want it to stop
    uiplot.btnC.clicked.connect(fftplot) #when buttonC is clicked, get it to generate the FFT and plot it
    #uiplot.btnD.clicked.connect(lambda: uiplot.timer.setInterval(1.0))
    
    c=Qwt.QwtPlotCurve()  
    c.attach(uiplot.qwtPlot) #attaching the qwtplot to the object 

    
    #uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.yLeft, 0, 1000) #are you talking about this?? 
    
    uiplot.timer = QtCore.QTimer()
    uiplot.timer.start(1.0)
    
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething)
    
    

    ### DISPLAY WINDOWS
    win_plot.show()
    code=app.exec_()
    #epoc.close()
    sys.exit(code)



if __name__ == "__main__":
    main()
    