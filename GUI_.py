from pyemotiv import Epoc
import numpy as np
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import QApplication, QMainWindow
import PyQt4.Qwt5 as Qwt

import sys
import guiplot
import time


class EEGQt(QtCore.QObject): 

	def __init__(self, mainwindow): 
		super(EEGQt, self).__init__()

class QtEEG(QtCore.QObject):
	finished_adq = QtCore.pyqtSignal()
	#need to add the acquisition module in here 
	
	def __init__(self,mainwindow):
		super(QtEEG, self).__init__()
        

	def initUI(self): 
		
		# Emotiv Initialization and data acquisition
		
		epoc= Epoc()

		# collecting data from the headset and placing into two different arrays

		data= epoc.aquire([9]) 
		#data2= epoc.aquire([16]) 
		datarray = np.concatenate((datarray, data), axis = 1)
		#datarray2= np.concatenate((datarray2, data2), axis=1)



		#self.clab = ['F3', 'F4', 'P7', 'FC6', 'F7', 'F8', 'T7', 'P8', 'FC5', 'AF4','T8', 'O2', 'O1', 'AF3']
		self.timek = 512 
		self.x = np.arange(0,self.timek,1)
		self.y = [[0] for i in xrange(len(self.datarray[0]))]
		self.offset = [2500.0*i for i in xrange(len(self.datarray[0]))]
		self.mutex_stop = Qt.QMutex()
		self.cancel = False		
	
	def addTimeSeries(self,datarray):
		self.plt = []
		for i in xrange(len(datarray[0])):
			self.plt.append(Qwt.QwtPlotCurve(datarray[0][i]))
			self.plt[i].attach(self.mainwindow.eegPlot)
			self.plt[i].setPen(Qt.QPen(Qt.Qt.red))	
	
	def plotEEG(self):	
		#import gevent
		#from gevent import monkey		
		#self.headset = emotiv.Emotiv()
		#monkey.patch_all(True)
		print('Plotting!!!!')		
		#gevent.spawn(self.headset.setup)
		while True:
			self.mutex_stop.lock()
			if self.cancel:
				break
			self.mutex_stop.unlock()			
			self.packet = self.headset.dequeue()
			if self.packet is not None:
				for i in xrange(len(self.datarray[0])):
					p = self.packet.sensors[self.datarray[0][i]]
						
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
	app = QtGui.QApplication(sys.argv)
	
	window = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(window)
	window.show()
	emotivObj = QtEEG(ui)
	adqThread = QtCore.QThread()
	emotivObj.moveToThread(adqThread)
	emotivObj.finished_adq.connect(adqThread.quit)
	adqThread.started.connect(emotivObj.plotEEG)
	
	ui.startEEG.clicked.connect(adqThread.start)
	ui.stopEEG.clicked.connect(emotivObj.stop)
	
	sys.exit(app.exec_())



if __name__ == '__main__':
	main()

	
	
	