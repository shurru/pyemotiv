from pyemotiv import Epoc
import sys
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
# import thingspeak
import time
import datetime


XIVELY_API_KEY= "OXrsK9MwFkcLIJvMRlAouni0TBSYPbT2ZU3tuPpP2uqTZfxi"
XIVELY_FEED_ID= 146826075


class EEGRecorder:

    """Simple, cross-platform class to record from the microphone."""

    def __init__(self, chan=9):

        self.threadsDieNow = False  # threading
        self.newRecord = False
        self.ys = numpy.array([0 for i in xrange(0, 512)])
        self.alpha= numpy.array([0 for k in xrange(0,0)])
        self.chan = chan
        self.filter_checker = False
        self.fftcheck = False
        self.plot_check = True
        self.stop= False
        self.alp_val= 0

    # RECORDING THE EEG stream ###
    # get the EEG signal. Getting the raw EEG data and appending to ys

    # def continuousTrans(self): 
    #     self.thr= threading.Thread(target=self.update)
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
        #epocrec = Epoc()
        # epocrec.connect()

        while True:
            if self.threadsDieNow:
                break

            datarray = numpy.zeros((1, 4))

            data = numpy.random.randint(4000, 5000, size=(1, 4))
            # gets raw data from channel that is stated in the epoc
            #data = epocrec.aquire([self.chan])
            datarray = numpy.concatenate((datarray, data), axis=1)
            self.newRecord = True

            temp = [] * 4
            for i in xrange(0, len(datarray[0])):
                if datarray[0][i] > 0:
                    temp.append(datarray[0][i])

            self.ys = numpy.roll(self.ys, -4)
            for i in xrange(0, 4):
                self.ys[508 + i] = temp[i]

            # import time
            # time.sleep(0.015)

            if not forever:
                break

                

        # MATH ###
    # def update(self): 
    #     while True: 
    #         for i in xrange(0, 511):
    #              update= int(self.ys[i])
    #              randomarray=[]
    #              randomarray.append(update)
    #     # xivelytry.updata(update)
    #              thingspeak.doit(randomarray, self.alp_val)
    #              # print update
    #              print self.ys[i], update



    # def updata(self):
       
    #     api = xively.XivelyAPIClient(XIVELY_API_KEY)
    #     feed = api.feeds.get(XIVELY_FEED_ID)
    #     O1= self.ys[508]
    #     now = datetime.datetime.utcnow()
    #     feed.datastreams = [
    #         xively.Datastream(id='tmpr', current_value=O1, at=now),
    #         # xively.Datastream(id='watts', current_value=watts, at=now),
    #     ]
    #     feed.update()
    #     print O1


    def bandpass_firwin(ntaps, lowcut, highcut, fs, window='hamming'):
        nyq = 0.5 * fs
        taps = scipy.signal.firwin(ntaps, [lowcut, highcut], nyq=nyq, pass_zero=False,
                      window=window, scale=False)
        return taps

    # def fft(self):
       
    #     fs = 128
    #     pwr, freqs = mlab.psd(self.ys, Fs=fs, scale_by_freq=False)
    #     # pwr= 10*numpy.log10(numpy.abs(pwr))

    #     # lolol high pass. Filters until 3 Hz.
    #     if self.filter_checker == False:
    #         for i in xrange(0, 4):
    #             pwr[i] = 0

    #     elif self.filter_checker == True:
            
    #         for i in xrange(0, 6):
    #             pwr[i] = 0
    #         for j in xrange(61, 129):
    #             pwr[j] = 0

    #     return freqs, pwr

    # def alpha_plot(self,alphapwr): 
    #     if len(self.alpha)>100:
    #         self.alpha= numpy.array([0 for k in xrange(0,0)])
    #     self.alpha=numpy.append(self.alpha, alphapwr)
    #     #self.alpha= numpy.roll(self.alpha, 5)
    #     return self.alpha          


