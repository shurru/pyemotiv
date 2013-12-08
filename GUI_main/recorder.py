from pyemotiv import Epoc

import matplotlib
matplotlib.use('TkAgg') # <-- THIS MAKES IT FAST!
import numpy
from scipy import signal
import scipy
import struct
#import pyaudio
import threading
import pylab
import struct



class EEGRecorder:
    """Simple, cross-platform class to record from the microphone."""
    
    def __init__(self):

        self.threadsDieNow=False #threading 
        self.newRecord=False
        
        
    ### RECORDING THE EEG stream ###  
    
    #get the EEG signal. Getting the raw EEG data and appending to ys
           
    
    #want the app to record continuously, but only plot when a button is pressed
    def continuousStart(self):
        """CALL THIS to start running forever."""
        #print "Holla"
        self.t = threading.Thread(target=self.record)
        
        self.t.start() #starts the thread
        
    #kill the thread
    def continuousEnd(self):
        """shut down continuous recording."""
        print "Die!"
        self.threadsDieNow=True  

    
    def record(self,forever=True): 
          #need to find a way to empty the array or get it to read from
        while True: 
            if self.threadsDieNow: break
            datarray=numpy.zeros((1,4))
            
           # print"Lookie"
            epocrec=Epoc()
            for t in range(0,50):
                data= epocrec.aquire([9]) #gets raw data from channel O1
       
                datarray = numpy.concatenate((datarray, data), axis = 1)
                # can you do 
                # datarray[i]=numpy.concatenate((datarray, data), axis = 1)
                # then stick dataarray into ys. 
                #i will go from what to what? oh ok 
                #print len (datarray[0])
                t=t+1
            global sth
            sth= []*len(datarray[0]) 

            for i in range(0, len(datarray[0])):
                
                if datarray[0][i]>0 : 
                    sth.append(datarray[0][i]) 
                    #sth[i] = datarray[0][i] #so this doesn't work
                
                        #sth=[]
            

            
            self.newRecord=True 


            if forever==False: break

    def rawdata(self): 
        #print "Yo"
        
        xs=numpy.arange(0,1000)
        ys=sth
        #print len(ys) #need it to stay fixd
        #global ys
        ys=numpy.roll(ys,-1)

        return xs,ys

        ### MATH ###
    
    def fft(self): 
        time_step = 1/128.0
        sampling_freqs = numpy.fft.fftfreq(len(sth), d=time_step) #works fine, generates frequency between 0 to 60+ Hz
        positive_freqs = numpy.where(sampling_freqs > 0) #gets only the positive frequencies
        freqs = sampling_freqs[positive_freqs] #generates the frequencies perfectly

        power= numpy.abs(numpy.fft.rfft(signal.detrend((sth))))[positive_freqs]
        #idx= numpy.argsort(freqs)

        return freqs, power
        
    