from pyemotiv import Epoc
import numpy as np
import scipy
from scipy import fftpack
from scipy import signal
from matplotlib import pyplot
import matplotlib.pyplot as plt


epoc=Epoc()
datarray= []
power_avg=[]
power_store=[]
time= 0


while time<1:
	print time

	for t in range(0,100):

		data= epoc.aquire([9]) #gets raw data from channel O1
		datarray.append(data)

		t=t+1

	#print "Data: %r \n" %datarray 
	time_step = 1/128.0
	sampling_freqs = scipy.fftpack.fftfreq(len(datarray[1][0]), d=time_step)
	positive_freqs = np.where(sampling_freqs > 0)
	freqs = sampling_freqs[positive_freqs]

	power= np.abs(scipy.fftpack.fft(signal.detrend(datarray[1][0])))[positive_freqs]
	#print power

	

	for i in range (0, len(freqs)):
		x= freqs[i]
		y= power[i]
		
		
		if x<12.0 and x>7.0 : 
			print ("Frequency: %r \t Power: %r \n \n") %(x,y)
			#power_store= power_avg[i]

	time=time+1

	pyplot.plot(freqs, power, '-')
	#pyplot.title ('FFT')
	#pyplot.xlabel('Frequency')
	#pyplot.ylabel('Power')
	pyplot.savefig('FFT2.png')
	pyplot.show


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

