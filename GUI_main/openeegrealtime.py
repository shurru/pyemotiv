import ui_plot_form
from recorderopeneeg import *
import sys
import numpy
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt
from pyemotiv import Epoc
import matplotlib

# import xivelytry



# global epoc

def plotSomething():
    if epoc.newRecord == False or epoc.fftcheck == True or epoc.plot_check == False or epoc.stop==True:
        return
    epoc.savecsv()
    
    if epoc.chan==False:
        uiplot.qwtPlot.show()
        uiplot.qwtPlot_2.show()
        uiplot.qwtPlot_3.show()
        
        xs = numpy.arange(0, 1023)
        c.setData(xs, epoc.ys)
        uiplot.qwtPlot.replot()
        
        uiplot.qwtPlot_4.hide()
        uiplot.qwtPlot_5.hide()
        uiplot.qwtPlot_6.hide()


    if epoc.chan==True: 
        uiplot.qwtPlot_4.show()
        uiplot.qwtPlot_5.show()
        uiplot.qwtPlot_6.show()
       
        xs2= numpy.arange(0, 1023)
        f.setData(xs2, epoc.ys2)
        uiplot.qwtPlot_4.replot()
        
        uiplot.qwtPlot.hide()
        uiplot.qwtPlot_2.hide()
        uiplot.qwtPlot_3.hide()
    
    epoc.newRecord = False


def contplot():
    
    epoc.threadsDieNow = False
    epoc.newRecord = True
    epoc.plot_check = True
    epoc.fftcheck=False
    epoc.stop= False
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething)


def txtChange(text):
    
    uiplot.painedit.setText(text)
    uiplot.painedit.adjustSize() 

def txtChange2(text):
    
    uiplot.painedit_2.setText(text)
    uiplot.painedit_2.adjustSize() 

def fftplot():
    if epoc.newRecord == False or epoc.fftcheck == False or epoc.plot_check == True or epoc.stop==True:
        return

    if epoc.chan==False: 
        uiplot.qwtPlot.show()
        uiplot.qwtPlot_2.show()
        uiplot.qwtPlot_3.show()

        freq, pwr = epoc.fft()
        d.setData(freq, pwr)
        uiplot.qwtPlot_2.replot()

        alpha_pwr = []
        max_alpha=[]
        pwr_change=[] #identifying the max value of the power
        
        for i in xrange(0, len(pwr)):
            if freq[i] < 13 and freq[i] > 7:
                alpha_pwr.append(pwr[i])
        max_alpha.append(max(alpha_pwr))

        #O1 alpha power change
        x= numpy.arange(0,300)
        y=epoc.alpha_plot(max_alpha)
        e.setData(x,y)
        uiplot.qwtPlot_3.replot()

        #text change O1
        for i in xrange(0, len(freq)): 
            if freq[i]<30 and freq[i]>5: 
                pwr_change.append(pwr[i])

        if max(alpha_pwr)== max(pwr_change): 
            epoc.alp_val_O1=1
            txtChange("High Alpha Power")


        else: 
            txtChange("Low Alpha Power")
            epoc.alp_val_O1=0
        
        uiplot.qwtPlot_4.hide()
        uiplot.qwtPlot_5.hide()
        uiplot.qwtPlot_6.hide()

    if epoc.chan==True: 
        uiplot.qwtPlot.hide()
        uiplot.qwtPlot_2.hide()
        uiplot.qwtPlot_3.hide()
        uiplot.qwtPlot_4.show()
        uiplot.qwtPlot_5.show()
        uiplot.qwtPlot_6.show()

        freq2, pwr2 = epoc.fft2()
        g.setData(freq2, pwr2)
        uiplot.qwtPlot_5.replot()
        alpha_pwr_2 = []
        max_alpha_2=[]
        pwr_change_2=[] 

        for i in xrange(0, len(pwr2)):
            if freq2[i] < 13 and freq2[i] > 7:
                alpha_pwr_2.append(pwr2[i])
        max_alpha_2.append(max(alpha_pwr_2))

        x2= numpy.arange(0,300)
        y2=epoc.alpha_plot2(max_alpha_2)
        h.setData(x2,y2)
        uiplot.qwtPlot_6.replot()

        #text change O2
        for i in xrange(0, len(freq2)): 
            if freq2[i]<30 and freq2[i]>5: 
                pwr_change_2.append(pwr2[i])

        if max(alpha_pwr_2)== max(pwr_change_2): 
            epoc.alp_val_O2= 1
            txtChange2("High Alpha Power")

        else: 
            txtChange2("Low Alpha Power")
            epoc.alp_val_O2=0

    epoc.newRecord = False



def stopplot(): 
    epoc.stop= True

    print "stopped"

def filtercheck(): 
    state= uiplot.filter_check.checkState()

    if state==0: 
        epoc.filter_checker= False 

    if state==2: 
        epoc.filter_checker= True

def chancheck(): 
    state_ch= uiplot.chan_check.checkState()

    if state_ch==0: 
        epoc.chan=False

    if state_ch==2: 
        epoc.chan=True


def contfftplot():
    epoc.fftcheck = True
    epoc.plot_check=False
    epoc.newRecord = True

    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), fftplot)


def main():
    app = QtGui.QApplication(sys.argv)
    global epoc
    global c, d, e, f, g, h
    global uiplot, win_plot

    win_plot = ui_plot_form.QtGui.QMainWindow()
    uiplot = ui_plot_form.Ui_Form()
    uiplot.setupUi(win_plot)
    
    epoc=EEGRecorder()

    epoc.continuousStart()  #start the record function
    # epoc.continuousTrans()
    
    uiplot.btn1.clicked.connect(contplot)
    uiplot.btn2.clicked.connect(stopplot)
    uiplot.btn3.clicked.connect(contfftplot)
    uiplot.filter_check.stateChanged.connect(filtercheck)
    # uiplot.save_btn.clicked.connect(save)
    uiplot.chan_check.stateChanged.connect(chancheck)
    uiplot.Exit.clicked.connect(epoc.continuousEnd)
   
    # O1 plots
    c = Qwt.QwtPlotCurve()
    c.attach(uiplot.qwtPlot)  # attaching the qwtplot to the object

    d = Qwt.QwtPlotCurve()
    d.attach(uiplot.qwtPlot_2)

    e = Qwt.QwtPlotCurve()
    e.attach(uiplot.qwtPlot_3)

    #O2 plots
    f= Qwt.QwtPlotCurve()
    f.attach(uiplot.qwtPlot_4)

    g= Qwt.QwtPlotCurve()
    g.attach(uiplot.qwtPlot_5)

    h= Qwt.QwtPlotCurve()
    h.attach(uiplot.qwtPlot_6)

    # fixing the axes for the 2 plots

    uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.xBottom, 0,512)
    uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.yLeft, -512, 512)
    uiplot.qwtPlot_2.setAxisScale(uiplot.qwtPlot_2.xBottom, 0, 64)
    uiplot.qwtPlot_2.setAxisAutoScale(1)
    uiplot.qwtPlot_3.setAxisScale(uiplot.qwtPlot_3.xBottom, 0, 300)
    uiplot.qwtPlot_3.setAxisScale(uiplot.qwtPlot_3.yLeft, 0, 20000)
    uiplot.qwtPlot_4.setAxisScale(uiplot.qwtPlot.xBottom, 0, 512)
    uiplot.qwtPlot_4.setAxisScale(uiplot.qwtPlot.yLeft, -512,512)
    uiplot.qwtPlot_5.setAxisScale(uiplot.qwtPlot_2.xBottom, 0, 64)
    uiplot.qwtPlot_5.setAxisAutoScale(1)
    uiplot.qwtPlot_6.setAxisScale(uiplot.qwtPlot_3.xBottom, 0, 300)
    uiplot.qwtPlot_6.setAxisScale(uiplot.qwtPlot_3.yLeft, 0, 20000)

   
   

    uiplot.timer = QtCore.QTimer()
    uiplot.timer.start(1.0)


    # DISPLAY WINDOWS
    win_plot.show()
    code = app.exec_()

    sys.exit(code)


if __name__ == "__main__":
    main()