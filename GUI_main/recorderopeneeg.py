from serialEEG import *
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # <-- THIS MAKES IT FAST!
import numpy
from scipy import signal
import scipy
import struct
import threading
import pylab
import struct
import matplotlib.mlab as mlab
import csv
import thingspeak


class EEGRecorder:

    """Simple, cross-platform class to record from the microphone."""

    def __init__(self):

        self.threadsDieNow = False  # threading
        self.newRecord = False
        self.ys = numpy.array([0 for i in xrange(0, 128)])
        self.ys2= numpy.array([0 for i in xrange(0, 512)])
        self.alpha= numpy.array([0 for k in xrange(0,0)])
        self.alpha2= numpy.array([0 for k in xrange(0,0)])
        self.O1save= []
        self.O2save=[]
        self.filter_checker = False
        self.fftcheck = False
        self.plot_check = True
        self.stop= False
        self.chan= False
        self.alp_val_O1=0
        self.alp_val_O2=0
        # self.O1= True
        # self.O2= False

    # RECORDING THE EEG stream ###
    # get the EEG signal. Getting the raw EEG data and appending to ys

    # def continuousTrans(self): 
    #     self.thr = threading.Thread(target=self.update)
    #     self.thr.start() 

    def continuousStart(self):
        """CALL THIS to start running forever."""
        self.t = threading.Thread(target=self.record)
        self.t.start()  # starts the thread

    # kill the thread
    def continuousEnd(self):
        """shut down continuous recording."""
        print "Die!"
        self.threadsDieNow = True
        

    def record(self, forever=True):
        eegrec= openeeg()
        # epocrec = Epoc()
        # epocrec.connect()

        while True:
            if self.threadsDieNow:
                break

            #two individual arrays to allow for the recording of the data
            datarray = numpy.array(10)
            datarray2 = numpy.array(10)         

            #datarray & datarray2 get the data which is being recorded from channels 1 and 2. 
            if self.chan==False: 
                data = eegrec.aquire(1)
                # print data #DATA is printed pretty fine.. 
                numpy.append(datarray,data)
                print datarray
                # datarray = numpy.concatenate((datarray, data), axis=1)

                temp = []*128
                for i in xrange(0, len(datarray)):
                    temp.append(datarray[i])
                
                self.ys = numpy.roll(self.ys, -1)
                # for i in xrange(0, 4):
                self.ys[i] = temp[i]

            # recording of O2 data will only begin if the check box is switched on. 

            if self.chan==True: 
                data2= eegrec.aquire(2)
                print data2
                datarray2= numpy.concatenate((datarray2, data2), axis=1)

                temp2 = [] * 4
                for i in xrange(0, len(datarray2[0])):
                    if datarray2[0][i] > 0:
                        temp2.append(datarray2[0][i])

                self.ys2 = numpy.roll(self.ys2, -4)
                for i in xrange(0, 4):
                    self.ys2[508 + i] = temp2[i]     

            self.newRecord = True   

                  

            if not forever:
                break

    def update(self): 
        while True: 
            if self.threadsDieNow:
                break
            # for i in xrange(508,511): 
            update= int(self.ys[508])
            update2= int(self.ys2[508])
            thingspeak.doit(update, update2, self.alp_val_O1, self.alp_val_O2)   
            # print self.alp_val_O1, self.alp_val_O2

                
    
    def savecsv(self): 
        self.O1save.append(self.ys[508])
        self.O1save.append(self.ys[509])
        self.O1save.append(self.ys[510])
        self.O1save.append(self.ys[511])
        self.O2save.append(self.ys2[508])
        self.O2save.append(self.ys2[509])
        self.O2save.append(self.ys2[510])
        self.O2save.append(self.ys2[511])
        numpy.savetxt("O1data.csv", self.O1save, delimiter=",")
        numpy.savetxt("O2data.csv", self.O2save, delimiter=",")

    def fft(self):
        
        fs = 128
        pwr, freqs = mlab.psd(self.ys, Fs=fs, scale_by_freq=False)
       
        if self.filter_checker == False:
            for i in xrange(0,2):
                pwr[i] = 0


        #need to implement the FIR filter

        elif self.filter_checker == True:
            for i in xrange(0, 6):
                pwr[i] = 0
            for j in xrange(61, 129):
                pwr[j] = 0

        return freqs, pwr

    def fft2(self): 
        fs = 128
        pwr2, freqs2= mlab.psd(self.ys2, Fs=fs, scale_by_freq=False)

        if self.filter_checker == False:
            for i in xrange(0, 2):
                pwr2[i] = 0

        elif self.filter_checker == True:
            for i in xrange(0, 6):
                pwr2[i] = 0
            for j in xrange(61, 129):
                pwr2[j] = 0

        return freqs2,pwr2


    def alpha_plot(self,alphapwr): 
        if len(self.alpha)>300:
            self.alpha= numpy.array([0 for k in xrange(0,0)]) #resets the array to contain all 0s

        self.alpha=numpy.append(self.alpha, alphapwr)
        #print self.alpha
        return self.alpha     

    def alpha_plot2(self,alphapwr2): 
        if len(self.alpha2)>300:
            self.alpha2= numpy.array([0 for k in xrange(0,0)]) #resets the array to contain all 0s

        self.alpha2=numpy.append(self.alpha2, alphapwr2)
        #print self.alpha
        return self.alpha2          

    def signalqlty(self): 
        sig= Epoc()
        return sig.ContactQuality([9])
