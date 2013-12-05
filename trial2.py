from pyemotiv import Epoc
import numpy as np
import scipy
from scipy import fftpack
from scipy import signal
from matplotlib import pyplot
import matplotlib.pyplot as plt


epoc=Epoc()
datarray=np.zeros((1,4))
power_avg=[]
power_store=[]
time= 0


while time<4:
	print time

	for t in range(0,100):
		
		#data= epoc.get_raw() #gets raw data from all the channels.. unnecessary once connect is made
		data= epoc.aquire([9]) #gets raw data from channel O1
		#print data.shape
		datarray = np.concatenate((datarray, data),axis = 0)

		t=t+1
	#print "Data: %r \n" %datarray 
	time_step = 1/128.0
	sampling_freqs = scipy.fftpack.fftfreq(len(datarray), d=time_step)
	positive_freqs = np.where(sampling_freqs > 0)
	freqs = sampling_freqs[positive_freqs]

	power= np.abs(scipy.fftpack.fft(signal.detrend(datarray)))[positive_freqs]
	
	for i in range (0, len(power)): 
		for j in range (0,3):
			print power[i][j]/4
	time= time+1
	