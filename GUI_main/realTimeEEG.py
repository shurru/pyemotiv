import ui_plot_form
from recorder import *
import equalizer
import ex2
import sys
import numpy
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt
from pyemotiv import Epoc
import matplotlib
# import xivelytry
import thingspeak
import dialog
import time


# global epoc

def plotSomething():
    if epoc.newRecord == False or epoc.fftcheck == True or epoc.plot_check == False or epoc.stop==True:
        return

    xs = numpy.arange(0, 511)

    c.setData(xs, epoc.ys)
    uiplot.qwtPlot.replot()
    
    
    #epoc.newRecord = False


def contplot():
    epoc.threadsDieNow = False
    epoc.newRecord = True
    epoc.plot_check = True
    epoc.fftcheck= False
    epoc.stop= False
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething)


def txtChange(text):
    
    uiplot.painedit.setText(text)
    uiplot.painedit.adjustSize() 

def fftplot():
    if epoc.newRecord == False or epoc.fftcheck == False or epoc.plot_check == True or epoc.stop==True:
        return

    freq, pwr = epoc.fft()
    d.setData(freq, pwr)
    uiplot.qwtPlot_2.replot()

    alpha_pwr = []
    max_alpha=[]
    pwr2=[]
    for i in xrange(0, len(pwr)):
        if freq[i] < 13 and freq[i] > 7:
            alpha_pwr.append(pwr[i])
    max_alpha.append(max(alpha_pwr))
    #print max_alpha

    for i in xrange(0, len(freq)): 
        if freq[i]<30 and freq[i]>3: 
            pwr2.append(pwr[i])

    if max(alpha_pwr)>= max(pwr2): 
        txtChange("High Alpha Power")
        epoc.alp_val= 1

    else: 
        txtChange("Low Alpha Power")
        epoc.alp_val=0

    x= numpy.arange(0,100)
    y=epoc.alpha_plot(max_alpha)
    e.setData(x,y )
    uiplot.qwtPlot_3.replot()
    

    
    #epoc.newRecord = False
def save(): 
    # dlg= dialog_.Example()
    
    dlg = dialog.QtGui.QDialog()
    ui = dialog.Ui_Dialog()
    ui.setupUi(dlg)
    dlg.show()
    # dlg= dialog.Ui_Dialog()
    # win_dlg= dialog.QtGui.QDialog()
    # dlg.setupUi(win_dlg)
    # dlg.show()
    print "save"



def stopplot(): 
    epoc.stop= True

    print "Stopped"

def filtercheck():
    state = uiplot.filter_check.checkState()
    if state == 0:  # when the checkbutton is left unpressed
        epoc.filter_checker = False

    if state == 2:  # when checkbutton is clicked
        epoc.filter_checker = True

# def channelcheck(): 
#     O1state= uiplot.O1_check.checkState()
#     O2state= uiplot.O2_check.checkState()

#     if O1state==2 and O2state==0: 
#         epoc=EEGRecorder()
#     if O2state==2 and O1state==0: 
#         epoc=EEGRecorder(14)
#     if O1state==2 and O2state==2: 
#         break
#     if O1state==0 and O2state==0: 
#         break


def contfftplot():
    epoc.fftcheck = True
    epoc.plot_check= False
    epoc.newRecord = True


    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), fftplot)


def main():
    app = QtGui.QApplication(sys.argv)
    global epoc
    global c, d, e
    global uiplot, win_plot

    #channelcheck()
    epoc = EEGRecorder()
    #epoc2 = EEGRecorder(10)

    epoc.continuousStart()  # should start the record function
    epoc.continuousTrans()

    win_plot = ui_plot_form.QtGui.QMainWindow()
    uiplot = ui_plot_form.Ui_Form()
    uiplot.setupUi(win_plot)

    # when buttonB is clicked, want it to stop
    
    uiplot.btn1.clicked.connect(contplot)
    uiplot.btn2.clicked.connect(stopplot)
    uiplot.btn3.clicked.connect(contfftplot)
    uiplot.save_btn.clicked.connect(save)
    uiplot.filter_check.stateChanged.connect(filtercheck)
    uiplot.Exit.clicked.connect(epoc.continuousEnd)

    # uiplot.pushButton_2.clicked.connect(epoc.batt)
    c = Qwt.QwtPlotCurve()
    c.attach(uiplot.qwtPlot)  # attaching the qwtplot to the object

    d = Qwt.QwtPlotCurve()
    d.attach(uiplot.qwtPlot_2)

    # creating a bar graph
    e= Qwt.QwtPlotCurve()
    e.attach(uiplot.qwtPlot_3)




    # fixing the axes for the 2 plots

    uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.xBottom, 0, 512)
    uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.yLeft, 0, 6000)
    uiplot.qwtPlot_2.setAxisScale(uiplot.qwtPlot_2.xBottom, 0, 64)
    #uiplot.qwtPlot_2.setAxisScale(uiplot.qwtPlot_2.yLeft, 0, 1e6)
    uiplot.qwtPlot_3.setAxisScale(uiplot.qwtPlot_3.xBottom, 0, 100)
    # uiplot.qwtPlot_3.setAxisAutoScale(uiplot.qwtPlot_2.yLeft, 0, 10000)
    uiplot.qwtPlot_2.setAxisAutoScale(1)
   

    uiplot.timer = QtCore.QTimer()
    uiplot.timer.start(1.0)

    # DISPLAY WINDOWS
    win_plot.show()
    code = app.exec_()

    sys.exit(code)


if __name__ == "__main__":
    main()
