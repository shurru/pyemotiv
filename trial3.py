from pyemotiv import Epoc
import numpy as np
import scipy
from scipy import fftpack
from scipy import signal
from matplotlib import pyplot
import matplotlib.pyplot as plt


epoc=Epoc()
#datarray= None
power_avg=[]
power_store=[]
time= 0


while time<1:
	print time
	datarray=np.zeros((1,4)) #resets datarray every time we run the loop

	for t in range(0,100):

		if type(datarray)!=np.ndarray: 
			data= epoc.aquire([9]) #gets raw data from channel O1

			#datarray=np.concatenate((datarray, data), axis = 1)

		t=t+1

	#print "Data: %r \n" %datarray 
	time_step = 1/128.0
	sampling_freqs = scipy.fftpack.fftfreq(len(datarray), d=time_step)
	positive_freqs = np.where(sampling_freqs > 0)
	freqs = sampling_freqs[positive_freqs]

	power= np.abs(scipy.fftpack.fft(signal.detrend(datarray)))[positive_freqs]
	#print power

	for i in range (0, len(power)):
		power_avg.append((power[i][0][0]+ power[i][0][1]+ power[i][0][2]+ power[i][0][3]))

	for i in range (0, len(freqs)):
		x= freqs[i]
		y= power_avg[i]
		
		
		if x<12.0 and x>7.0 : 
			print ("Frequency: %r \t Power: %r \n \n") %(x,y)
			#power_store= power_avg[i]

	time=time+1

	pyplot.plot(freqs, power_avg, '-')
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

