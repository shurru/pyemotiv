from pyemotiv import Epoc
import numpy as np
import scipy
import time
from scipy import signal
import matplotlib.mlab as mlab
from matplotlib import pyplot
import matplotlib.pyplot as plt
from math import *


epoc=Epoc()

power_avg=[]
power_store=[]
time= 0
#sth=[]



while time<4:
	print time
	datarray=np.zeros((1,4)) #resets datarray every time we run the loop
	
	for t in range(0,100):
		
		#data= epoc.get_raw() #gets raw data from all the channels.. unnecessary once connect is made
		data= epoc.aquire([9]) #gets raw data from channel O1
		#data2= epoc.aquire([14]) #connection on hardware is to AF4:not an issue at all on S/w
		#print data.shape
		datarray = np.concatenate((datarray, data), axis = 1)
		#print datarray[0]
		#datarray2= np.concatenate((datarray2, data2), axis=1)
		
		
		#print "Data: %r \n" %datarray[0]
		t=t+1
	sth =[]*len(datarray[0]) 
	
	for i in range(0, len(datarray[0])): 
		if datarray[0][i]>0: 
			sth.append(datarray[0][i])
	
	print len(sth)

	#print data.shape
	fs=128

	pwr, freqs= mlab.psd(sth, Fs=fs,scale_by_freq= False )
	pwr= 10*np.log10(np.abs(pwr))
	
	plt.plot(freqs, pwr)
	
	plt.title ('Welch')

	pyplot.savefig("pywelch.png")		

	

	
	time=time+1




	#times=epoc.times
	

	#FFT= abs(scipy.fft(signal.detrend(data)))

	
	#freqs= scipy.fftpack.fftfreq(data.size, times)

	#print freqs
	#print data



	#data_FFT = fft(data)
	#print data.size
	#sampling_freq= scipy.fftpack.fftfreq(data.size)
	#pos_freq= np.where(sampling_freq >0) #find all the points which are positive
	#freqs= sampling_freq[pos_freq]
	#print signal.detrend(data) #subtracts the mean from the signals
	#print sampling_freq
	#pylab.plot(times, data)


	#power=np.abs(fftpack.fft(signal.detrend(data)))[pos_freq]

	#print data
	#print "Frequency: %r Power: %r" %(1/times, FFT)

