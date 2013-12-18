
import sys
from PyQt4 import QtGui
import ui_plot_form
#from ui_plot_form import Ui_Form

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt

import random


class Window(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        win_plot = ui_plot_form.QtGui.QMainWindow()
        uiplot = ui_plot_form.Ui_Form()
        uiplot.setupUi(win_plot)

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        #self.canvas = uiplot.alpha_widget(self.figure)
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        #self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        # self.button = QtGui.QPushButton('Plot')
        # self.button.clicked.connect(self.plot)

        # set the layout
        layout = QtGui.QVBoxLayout()
        # layout.addWidget(self.toolbar)
        # layout.addWidget(self.canvas)
        # layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self, data):
        ''' plot some random stuff '''
        fig = plt.figure()
        N = 1

        self.data_an = data
        rects = plt.bar(range(N), self.data_an, align='center')
        print "Bleh"

        for rect, h in zip(rects, self.data_an):
            rect.set_height(h)
        # fig.canvas.draw()

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
