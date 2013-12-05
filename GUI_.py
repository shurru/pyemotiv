from pyemotiv import emotiv
import numpy as np
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import QApplication, QMainWindow
import PyQt4.Qwt5 as Qwt

import sys
from GUImain import Ui_MainWindow
import time

class QtEEG(QtCore.QObject):

	#need to add the acquisition module in here 
	finished_adq = QtCore.pyqtSignal()
	def __init__(self,mainwindow):
		super(QtEEG, self).__init__()
				
		# Emotiv Initialization
		self.clab = ['F3', 'F4', 'P7', 'FC6', 'F7', 'F8', 'T7', 'P8', 
							'FC5', 'AF4','T8', 'O2', 'O1', 'AF3']
		self.timek = 512
		self.x = np.arange(0,self.timek,1)
		self.y = [[0] for i in xrange(len(self.clab))]
		self.offset = [2500.0*i for i in xrange(len(self.clab))]
		self.mutex_stop = Qt.QMutex()
		self.cancel = False		
	
	def addTimeSeries(self,clab):
		self.plt = []
		for i in xrange(len(clab)):
			self.plt.append(Qwt.QwtPlotCurve(clab[i]))
			self.plt[i].attach(self.mainwindow.eegPlot)
			self.plt[i].setPen(Qt.QPen(Qt.Qt.red))	
	
	def plotEEG(self):	
		import gevent
		from gevent import monkey		
		self.headset = emotiv.Emotiv()
		monkey.patch_all(True)
		print('Plotting!!!!')		
		gevent.spawn(self.headset.setup)
		while True:
			self.mutex_stop.lock()
			if self.cancel:
				break
			self.mutex_stop.unlock()			
			self.packet = self.headset.dequeue()
			if self.packet is not None:
				for i in xrange(len(self.clab)):
					p = self.packet.sensors[self.clab[i]]
						
					self.y[i].append(p['value'])
					if len(self.y[i]) > self.timek:
						self.y[i].pop(0)
						self.plt[i].setData(self.x,self.y[i]-np.mean(self.y[i])+self.offset[i])
						self.mainwindow.eegPlot.replot()	
						gevent.sleep(0.1)
		self.cancel = False				
		self.headset.close()
		self.finished_adq.emit()
		
	def stop(self):
		print('Cancel!')
		self.mutex_stop.lock()
		self.cancel = True
		self.mutex_stop.unlock()
	
			
	def __del__(self):
		self.headset.close()
			

def main():

	#shows the GUI
	app = QtGui.QApplication([])
	window = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(window)
	window.show()



if __name__ == '__main__':

	emotivObj = QtEEG(ui)
	adqThread = QtCore.QThread()
	emotivObj.moveToThread(adqThread)
	emotivObj.finished_adq.connect(adqThread.quit)
	adqThread.started.connect(emotivObj.plotEEG)
	
	ui.startEEG.clicked.connect(adqThread.start)
	ui.stopEEG.clicked.connect(emotivObj.stop)
	
	sys.exit(app.exec_())
	
	