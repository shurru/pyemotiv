#!/usr/bin/env python2.7
# encoding: utf-8

import sys
from random import random
from PyQt4 import QtCore, QtGui, Qwt5

from guiqwt.plot import CurvePlot
from guiqwt.builder import make


class GuiQwtPlot( QtGui.QWidget ):

    def __init__( self ):
        QtGui.QWidget.__init__( self )
        self.__create_layout()
        self.__setup_layout()


    def __create_layout( self ):
        self.setWindowTitle( "LambdaFunction - guiqwt" )

        self.plot = CurvePlot( self )
        #self.plot.set_antialiasing( True )
        self.button = QtGui.QPushButton( "Load" )

        ly = QtGui.QVBoxLayout()
        ly.addWidget( self.plot )
        ly.addWidget( self.button )

        self.setLayout( ly )


    def __setup_layout( self ):
        self.connect( self.button, QtCore.SIGNAL( "clicked()" ), self.button_Click )
        self.curve = make.curve( [ ], [ ], "curve1", QtGui.QColor( 255, 0, 0) )
        self.plot.add_item( self.curve )


    def button_Click( self ):
        self.curve.set_data( range( 0, 20, 2), map( lambda _: random(), range( 0, 10 ) ) )
        self.plot.replot( )


def main():
    app = QtGui.QApplication( sys.argv )
    prog = GuiQwtPlot( )
    prog.show( )
    sys.exit( app.exec_( ) )


if __name__ == '__main__':
    main()