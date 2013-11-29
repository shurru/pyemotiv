from pyemotiv import Epoc
import numpy as np
import scipy
import time
from scipy import signal
from matplotlib import pyplot
import matplotlib.pyplot as plt


epoc=Epoc()

power_avg=[]
power_store=[]
time= 0


while time<3:
	print time
	datarray=np.zeros((1,4)) #resets datarray every time we run the loop

	for t in range(0,100):
		
		#data= epoc.get_raw() #gets raw data from all the channels.. unnecessary once connect is made
		data= epoc.aquire([9]) #gets raw data from channel O1
		#print data.shape
		datarray = np.concatenate((datarray, data), axis = 1)
		
		#print "Data: %r \n" %datarray
		t=t+1

	print datarray.shape
	time_step = 1/128.0
	sampling_freqs = scipy.fftpack.fftfreq(len(datarray[0]), d=time_step)
	positive_freqs = np.where(sampling_freqs > 0)
	freqs = sampling_freqs[positive_freqs]
	
	power= np.abs(scipy.fftpack.fft(signal.detrend(datarray[0])))[freqs]
	

	#print signal.detrend(datarray)
	#print datarray[0].shape

	
	
	#print datarray.size
	#print freqs.size, len(freqs)
	#print power
	#print power.shape

	for i in range (0, len(freqs)):
		x= freqs[i]
		y=power[i]/(power.size)
		#(power[i][0]+power[i][1]+power[i][2]+power[i][3])/4

		
		print x,y
		
		#if x<12.0 and x>7.0 : 
			#print ("Frequency: %r \t Power: %r \n \n") %(x,y)
			#power_store= power_avg[i]
	
	pyplot.plot(freqs, power/power.size, '-')
	#pyplot.draw()
	#pyplot.show()
	pyplot.savefig("haiz.png")		

	

	
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

