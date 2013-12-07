#!/usr/bin/env python2.7
# encoding: utf-8


import sys
import time
import datetime

from random import random
from PyQt4 import QtCore, QtGui, Qwt5

from guiqwt.plot import CurvePlot, PlotManager
from guiqwt.tools import SelectPointTool
from guiqwt.builder import make

from threading import Timer



class Producer( QtGui.QWidget ):
    '''Widget used to create a tokens producer and generate
    a PyQt signal every time.
    '''

    def __init__( self ):
        QtGui.QWidget.__init__( self )
        self.do = True
        self.start_timer()


    def produce( self ):
        '''Thi is the method who creates the new token and
        who emits the signal received by the MainWindow.
        '''
        self.start_timer()
        self.emit( QtCore.SIGNAL( 'newToken' ), random() )


    def start_timer( self ):
        '''Method usd to create the new timer and to 
        control the stop.
        '''
        if self.do:
            self.timer = Timer( 1, self.produce )
            self.timer.start()


class DateTimeScaleDraw( Qwt5.Qwt.QwtScaleDraw ):
    '''Class used to draw a datetime axis on our plot.
    '''
    def __init__( self, *args ):
        Qwt5.Qwt.QwtScaleDraw.__init__( self, *args )


    def label( self, value ):
        '''Function used to create the text of each label
        used to draw the axis.
        '''
        try:
            dt = datetime.datetime.fromtimestamp( value )
        except:
            dt = datetime.datetime.fromtimestamp( 0 )
        #return Qwt5.Qwt.QwtText( '%s' % dt.strftime( '%d/%m%Y %H:%M:%S' ) )
        return Qwt5.Qwt.QwtText( '%s' % dt.strftime( '%H:%M:%S' ) )


class GuiQwtPlot( QtGui.QMainWindow ):
    '''MainWindow, in charge to create the plot, the toolbar and the
    legend. It also works as a consumer of tokens generated by the
    inner producer. It is the entry point of the program.
    '''

    def __init__( self ):
        QtGui.QMainWindow.__init__( self )
        self.__init_inners()
        self.__create_layout()
        self.__setup_layout()


    def __create_layout( self ):
        '''Function used to create the layout of the MainWindow.
        '''
        self.setWindowTitle( 'LambdaFunction - guiqwt' )

        self.plot = CurvePlot( self )
        self.plot.set_antialiasing( True )

        ly = QtGui.QVBoxLayout()
        ly.addWidget( self.plot )

        w = QtGui.QWidget()
        w.setLayout( ly )

        self.setCentralWidget( w )

        # Set axis's labels
        self.plot.setAxisTitle( Qwt5.Qwt.QwtPlot.xBottom, 'Time' )
        self.plot.setAxisTitle( Qwt5.Qwt.QwtPlot.yLeft, 'Value' )


    def __init_inners( self ):
        '''Function used to setup the inner variables of
        the MainWindow.
        '''
        self.producer = Producer()
        self.data = [ ]


    def __setup_layout( self ):
        '''Function used to setup the differet elements of the layout.
        '''
        self.connect( self.producer, QtCore.SIGNAL( 'newToken' ), self.consume )
        
        # Create the curves
        self.curve = make.curve( [ ], [ ], 'Ramdom values', QtGui.QColor( 255, 0, 0 ) )
        self.plot.add_item( self.curve )

        # Crate the PlotManager
        self.manager = PlotManager( self )
        self.manager.add_plot( self.plot )

        # Create Toolbar
        toolbar = self.addToolBar( 'tools' )
        self.manager.add_toolbar( toolbar, id( toolbar ) )

        # Register the ToolBar's type
        self.manager.register_all_curve_tools( )
        self.manager.register_other_tools()

        # Register a custom tool
        self.manager.add_tool( SelectPointTool, title = 'Test', on_active_item = True, mode = 'create' )
        
        # Create the Legend
        legend = make.legend( 'TL' )
        self.plot.add_item( legend )

        # Setup the plot's scale
        self.plot.setAxisScaleDraw( Qwt5.Qwt.QwtPlot.xBottom, DateTimeScaleDraw() )


    def closeEvent( self, _ ):
        '''Method runed when the signal 'close' of the
        MainWindow is emited.
        '''
        self.producer.do = False


    def consume( self, token ):
        '''Function called when the signal 'newToken'
        is captured.
        '''
        self.data.append( ( token, time.time() ) )
        self.draw()


    def draw( self ):
        '''Method used to update the plot:

            * Set label's orientation.
            * Set label's align.
            * Add income data to the curve.
            * Update the plot.
        '''
        # Set x-axis's label rotation
        self.plot.setAxisLabelRotation( Qwt5.Qwt.QwtPlot.xBottom, -45.0 )
        self.plot.setAxisLabelAlignment( Qwt5.Qwt.QwtPlot.xBottom, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom )

        # Set the data to the curve and update the plot
        self.curve.set_data( map( lambda x: x[ 1 ], self.data ), map( lambda x: x[ 0 ], self.data ) )
        self.plot.replot()


def main():
    app = QtGui.QApplication( sys.argv )
    prog = GuiQwtPlot( )
    prog.show( )
    sys.exit( app.exec_( ) )


if __name__ == '__main__':
    main()