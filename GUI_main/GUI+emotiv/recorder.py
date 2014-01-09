from pyemotiv import Epoc

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


class EEGRecorder:

    """Simple, cross-platform class to record from the microphone."""

    def __init__(self):

        self.threadsDieNow = False  # threading
        self.newRecord = False
        self.ys = numpy.array([0 for i in xrange(0, 512)])
        self.ys2= numpy.array([0 for i in xrange(0, 512)])
        self.alpha= numpy.array([0 for k in xrange(0,0)])
        #self.chan = 9
        self.filter_checker = False
        self.fftcheck = False
        self.plot_check = True
        self.stop= False
        # self.O1= True
        # self.O2= False

    # RECORDING THE EEG stream ###
    # get the EEG signal. Getting the raw EEG data and appending to ys

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
        epocrec = Epoc()
        epocrec.connect()

        while True:
            if self.threadsDieNow:
                break

            # if self.O1: 
            #     self.chan=9
            # if self.O2: 
            #     self.chan=14

            #two individual arrays to allow for the recording of the data
            datarray = numpy.zeros((1, 4))
            datarray2 = numpy.zeros((1, 4))         

            #data = numpy.random.randint(4000, 5000, size=(1, 4))
            # gets raw data from channel that is stated in the epoc

            #datarray & datarray2 get the data which is being recorded from channels 9 and 14
            data = epocrec.aquire([9])
            datarray = numpy.concatenate((datarray, data), axis=1)
            
            data2= epocrec.aquire([14])
            datarray2= numpy.concatenate((datarray2, data2), axis=1)


            self.newRecord = True

            temp = [] * 4
            for i in xrange(0, len(datarray[0])):
                if datarray[0][i] > 0:
                    temp.append(datarray[0][i])
            

            
            temp2 = [] * 4
            for i in xrange(0, len(datarray2[0])):
                if datarray2[0][i] > 0:
                    temp2.append(datarray2[0][i])

            self.ys = numpy.roll(self.ys, -4)
            for i in xrange(0, 4):
                self.ys[508 + i] = temp[i]

            self.ys2 = numpy.roll(self.ys2, -4)
            for i in xrange(0, 4):
                self.ys2[508 + i] = temp2[i]


            # import time
            # time.sleep(0.015)

            # print self.ys

            if not forever:
                break

        # MATH ###

    # def animate(self, data):
    #     fig = plt.figure()
    #     N = 1

    #     self.data_an = data
    #     rects = plt.bar(range(N), self.data_an, align='center')

    #     for rect, h in zip(rects, self.data_an):
    #         rect.set_height(h)

    #     ax = fig.add_subplot(111)

    #     # discards the old graph
    #     ax.hold(False)

    #     # plot data
    #     # ax.plot()

    #     # refresh canvas
    #     fig.canvas.draw()

        # return fig

    def savecsv(self): 
        numpy.savetxt("O1data.csv", self.ys, delimiter=",")
        numpy.savetxt("O2data.csv", self.ys2, delimiter=",")

    def fft(self):
        
        fs = 128
        pwr, freqs = mlab.psd(self.ys, Fs=fs, scale_by_freq=False)
        # pwr= 10*numpy.log10(numpy.abs(pwr))
        # lolol high pass. Filters until 3 Hz.
        if self.filter_checker == False:
            for i in xrange(0, 2):
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
        # lolol high pass. Filters until 3 Hz.

        if self.filter_checker == False:
            for i in xrange(0, 2):
                pwr2[i] = 0

        return freqs2,pwr2


    def alpha_plot(self,alphapwr): 
        if len(self.alpha)>300:
            self.alpha= numpy.array([0 for k in xrange(0,0)])
        self.alpha=numpy.append(self.alpha, alphapwr)
        # self.alpha= numpy.roll(self.alpha, 5)
        return self.alpha          

    def signalqlty(self): 
        sig= Epoc()
        return sig.ContactQuality([9])
