import ui_plot_form 
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
    #ys_arr= []
    xs,ys=epoc.rawdata()

    #print ys
     
    #print (ys_arr)

    c.setData(xs, ys)
    
    uiplot.qwtPlot.replot()
    epoc.newRecord=False
    
        
def contplot(): 
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething)   



def fftplot(): 
    if epoc.newRecord==False: 
        return 

    freq,pwr= epoc.fft()
    d.setData(freq,pwr)
    uiplot.qwtPlot.replot()
    epoc.newRecord=False

def contfftplot(): 
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), fftplot)




def main(): 
    app = QtGui.QApplication(sys.argv)
    global epoc
    global c,d
    global uiplot, win_plot
    

    epoc=EEGRecorder()
    
    #epoc.setup
    #print"boom"
    epoc.continuousStart() #should start the record function
    #print "Hi"

    win_plot = ui_plot_form.QtGui.QMainWindow()
    uiplot = ui_plot_form.Ui_Form()
    uiplot.setupUi(win_plot)
   
    uiplot.btn2.clicked.connect(epoc.continuousEnd) #when buttonB is clicked, want it to stop
    uiplot.btn1.clicked.connect(contplot)
    uiplot.btn3.clicked.connect(contfftplot)
    uiplot.pushButton_2.clicked.connect(epoc.batt)
  
    c=Qwt.QwtPlotCurve()  
    c.attach(uiplot.qwtPlot) #attaching the qwtplot to the object 

    d=Qwt.QwtPlotCurve()
    d.attach(uiplot.qwtPlot_2)

    #fixing the axes for the 2 plots

    uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.xBottom,0,500) 
    uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.yLeft, 3000,6000) 
    uiplot.qwtPlot_2.setAxisScale(uiplot.qwtPlot.xBottom,0,64) 
    uiplot.qwtPlot_2.setAxisScale(uiplot.qwtPlot_2.yLeft, 0, 500) 
    
    uiplot.timer = QtCore.QTimer()
    uiplot.timer.start(1.0)
    
   
   
    
    
    
    

    ### DISPLAY WINDOWS
    win_plot.show()
    code=app.exec_()
    #epoc.close()
    sys.exit(code)



if __name__ == "__main__":
    main()
    