from pyemotiv import Epoc

import matplotlib
matplotlib.use('TkAgg')  # <-- THIS MAKES IT FAST!
import numpy
from scipy import signal
import scipy
import struct
import threading
import pylab
import struct
import matplotlib.mlab as mlab


class EEGRecorder:

    """Simple, cross-platform class to record from the microphone."""

    def __init__(self, chan=9):

        self.threadsDieNow = False  # threading
        self.newRecord = False
        self.ys = numpy.array([0 for i in xrange(0, 512)])
        #self.chan = chan

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
        while True:
            if self.threadsDieNow:
                break

            datarray = numpy.zeros((1, 4))

            #epocrec = Epoc()

            data = numpy.random.randint(4000, 5000, size=(1, 4))
            # gets raw data from channel that is stated in the epoc
            #data = epocrec.aquire([self.chan])
            datarray = numpy.concatenate((datarray, data), axis=1)
            self.newRecord = True

            temp = [] * 4
            for i in xrange(0, len(datarray[0])):
                if datarray[0][i] > 0:
                    temp.append(datarray[0][i])

            self.ys = numpy.roll(self.ys, 4)
            for i in xrange(0, 4):
                self.ys[508 + i] = temp[i]

            import time
            time.sleep(0.015)

            if not forever:
                break

        # MATH ###


    def fft(self):
        fs = 128
        pwr, freqs = mlab.psd(self.ys, Fs=fs, scale_by_freq=False)
        # pwr= 10*numpy.log10(numpy.abs(pwr))

        # lolol high pass. Filters until 2 Hz.
        for i in xrange(0, 2):
            pwr[i] = 0

        return freqs, pwr

    def alpha(self): 
        fs = 128
        pwr, freqs = mlab.psd(self.ys, Fs=fs, scale_by_freq=False)




