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
import matplotlib.mlab as mlab




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
            global datarray
            datarray=numpy.zeros((1,4))
            
           # print"Lookie"
            
            epocrec=Epoc()
            
            data= epocrec.aquire([9]) #gets raw data from channel O1
            datarray = numpy.concatenate((datarray, data), axis = 1)
            self.newRecord=True    
            #print (datarray[0][4], datarray[0][5], datarray[0][6], datarray[0][7])
            global temp
            temp= []*4
            for i in range(0, len(datarray[0])):
                if datarray[0][i]>0 : 
                    temp.append(datarray[0][i]) 

           
            global ys
            ys = temp
            #print ys
            if forever==False: break
            #print temp.shape

    def rawdata(self): 
       
        #change the way this is visualized. The logic behind it needs to be tweaked
       # print temp
        xs=numpy.arange(0,500)
        global ys
        print ys
        
        #print (rand)
        ys=numpy.roll(ys,-1)

        
        return xs,ys

        ### MATH ###
    
    def fft(self): 
       fs=128
       pwr,freqs= mlab.psd(temp, Fs=fs,scale_by_freq= False )
       #pwr= 10*np.log10(np.abs(pwr))
    

       return freqs, pwr

    def batt(self): 
        epocrec=Epoc()
        print epocrec.BatteryCharge

        

        
    