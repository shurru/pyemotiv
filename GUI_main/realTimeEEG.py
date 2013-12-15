import ui_plot_form
from recorder import *
import BarPlot
import sys
import numpy
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt
from pyemotiv import Epoc


# epoc=Epoc()

def plotSomething():
    if epoc.newRecord == False:
        return

    xs = numpy.arange(0, 511)

    c.setData(xs, epoc.ys)
    uiplot.qwtPlot.replot()

    epoc.newRecord = False


def contplot():
    epoc.threadsDieNow = False
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething)


def fftplot():
    if epoc.newRecord == False:
        return

    freq, pwr = epoc.fft()
    d.setData(freq, pwr)
    uiplot.qwtPlot_2.replot()

    alpha_pwr = []
    for i in xrange(0, len(pwr)):
            if freq[i] < 13 and freq[i] > 7:
                alpha_pwr.append(pwr[i])
                max_alpha = max(alpha_pwr)

    # print max_alpha
    #e.drawFromTo(0, max_alpha, 0, 1)

    epoc.newRecord = False


def contfftplot():
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), fftplot)


def main():
    app = QtGui.QApplication(sys.argv)
    global epoc
    global c, d, e
    global uiplot, win_plot

    epoc = EEGRecorder()
    #epoc2 = EEGRecorder(10)

    epoc.continuousStart()  # should start the record function

    win_plot = ui_plot_form.QtGui.QMainWindow()
    uiplot = ui_plot_form.Ui_Form()
    uiplot.setupUi(win_plot)

    # when buttonB is clicked, want it to stop
    uiplot.btn2.clicked.connect(epoc.continuousEnd)
    uiplot.btn1.clicked.connect(contplot)
    uiplot.btn3.clicked.connect(contfftplot)
    # uiplot.pushButton_2.clicked.connect(epoc.batt)

    c = Qwt.QwtPlotCurve()
    c.attach(uiplot.qwtPlot)  # attaching the qwtplot to the object

    d = Qwt.QwtPlotCurve()
    d.attach(uiplot.qwtPlot_2)

    #e = BarPlot.BarCurve()
    # e.attach(uiplot.qwtPlot_3)

    # fixing the axes for the 2 plots

    uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.xBottom, 0, 500)
    uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.yLeft, 3000, 6000)
    uiplot.qwtPlot_2.setAxisScale(uiplot.qwtPlot_2.xBottom, 0, 64)
    uiplot.qwtPlot_2.setAxisScale(uiplot.qwtPlot_2.yLeft, 0, 1e6)
    uiplot.qwtPlot_3.setAxisScale(uiplot.qwtPlot_3.xBottom, 0, 1)
    uiplot.qwtPlot_3.setAxisScale(uiplot.qwtPlot_2.yLeft, 0, 10000)
    # uiplot.qwtPlot_2.setAxisAutoScale(1)

    uiplot.timer = QtCore.QTimer()
    uiplot.timer.start(1.0)

    # DISPLAY WINDOWS
    win_plot.show()
    code = app.exec_()
   
    sys.exit(code)


if __name__ == "__main__":
    main()
