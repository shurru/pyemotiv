"""
This demo demonstrates how to embed a matplotlib (mpl) plot 
into a PyQt4 GUI application, including:

* Using the navigation toolbar
* Adding data to the plot
* Dynamically modifying the plot's properties
* Processing mpl events
* Saving the plot to a file from a menu

The main goal is to serve as a basis for developing rich PyQt GUI
applications featuring mpl plots (using the mpl OO API).

Eli Bendersky (eliben@gmail.com)
License: this code is in the public domain
Last modified: 19.01.2009
"""
import sys
import os
import random
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy
import ui_plot_form
import PyQt4.Qwt5 as Qwt

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure


class BarCurve(QMainWindow):

    def __init__(self,  parent=None,):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Demo: PyQt with matplotlib')

        self.create_main_frame()
        #self.textbox.setText('1 2 3 ')
        #self.attach()
        # self.data = data
        # self.on_draw()

    def on_draw(self, data):
        """ Redraws the figure
        """
        #str = unicode(self.textbox.text())
        #self.data = map(int, str.split())
        x = range(len(data))

        # clear the axes and redraw the plot anew
        #
        self.axes.clear()
        self.axes.bar(
            left=x,
            height=data,
            width=1,
            align='center',
            alpha=0.44,
            picker=5)

        self.canvas.draw()

    def attach(self):

        uiplot = ui_plot_form.Ui_Form()
        win_plot = ui_plot_form.QtGui.QMainWindow()
        uiplot.setupUi(win_plot)
       
        self.frame = uiplot.alpha_widget #attaching QWidget to self.frame

        # self.dpi = 100
        # self.fig =  Figure((5.0, 4.0), dpi=self.dpi)
        #self.canvas = FigureCanvas(self.fig)
        self.frame.setGeometry(QtCore.QRect(20, 360, 291, 241))

        self.frame.setParent(self.frame)
        self.axes = self.fig.add_subplot(111)

        # self.canvas.setParent(uiplot)
        # self.axes=self.fig.add_subplot(11)
        #self.canvas= uiplot.qwtPlot_3
        #vbox = QVBoxLayout()
        #vbox.addWidget(self.canvas)

        self.frame.setLayout(vbox)
        self.setCentralWidget(self.frame)

    def create_main_frame(self):
        self.main_frame = QWidget()
        
        # Create the mpl Figure and FigCanvas objects. 
        # 5x4 inches, 100 dots-per-inch
        #
        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        
        # Since we have only one plot, we can use add_axes 
        # instead of add_subplot, but then the subplot
        # configuration tool in the navigation toolbar wouldn't
        # work.
        #
        self.axes = self.fig.add_subplot(111)

        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)

        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)
        
        
        # Other GUI controls
        # self.textbox = QLineEdit()
        # self.textbox.setMinimumWidth(200)
        # self.connect(self.textbox, SIGNAL('editingFinished ()'), self.on_draw)
        


def main():
    app = QApplication(sys.argv)
    form = BarCurve()
    for i in xrange(0,10): 
        rand= numpy.random.randint(4000, 5000)
        form.on_draw([rand])
        print rand
    
        form.show()
    app.exec_()


if __name__ == "__main__":
    main()
