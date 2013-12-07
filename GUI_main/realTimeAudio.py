import uiplot
import sys
import numpy
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt
from recorder import *



def plotSomething():
    if epoc.newRecord==False: 
        return
    #how do I get the code in here? Need to print the raw EEG data 
    #click a button and it stops updating it
    #click another button. it generates FFT signal
    
    xs,ys=epoc.fft()
    c.setData(xs,ys)
    uiplot.qwtPlot.replot()
    epoc.newRecord=False

def PlotFFT(): 
    if epoc.newRecord==False: 
        return 

    xs,ys=epoc.fft()
    c.setData(xs,ys)
    uiplot.qwtPlot.replot()
    epoc.newRecord=False

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    win_plot = ui_plot.QtGui.QMainWindow()
    uiplot = ui_plot.Ui_win_plot()
    uiplot.setupUi(win_plot)
    uiplot.btnA.clicked.connect(plotSomething)
    uiplot.btnB.clicked.connect(epoc.continuousStop())) #when buttonB is clicked, want it to stop
    uiplot.btnC.clicked.connect(PlotFFT)) #when buttonC is clicked, get it to generate the FFT and plot it
    #uiplot.btnD.clicked.connect(lambda: uiplot.timer.setInterval(1.0))
    c=Qwt.QwtPlotCurve()  
    c.attach(uiplot.qwtPlot)
    
    uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.yLeft, 0, 1000)
    
    uiplot.timer = QtCore.QTimer()
    uiplot.timer.start(1.0)
    
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething) 
    
    epoc=EEGRecorder()
    epoc.setup()
    epoc.continuousStart()

    ### DISPLAY WINDOWS
    win_plot.show()
    code=app.exec_()
    epoc.close()
    sys.exit(code)