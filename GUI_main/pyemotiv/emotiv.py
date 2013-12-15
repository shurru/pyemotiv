from ctypes import c_char_p, c_uint, c_int, c_bool, byref, CDLL
import numpy as np
import time
import sys


class Epoc(object):

    """
    Class that connects to Emotiv Epoc by wrapping the 
    research SDK dynamic link libraries
    """

    def __init__(self):
        self.raw_channels_idx = range(3, 17)
        self.gyro_idx = [
            self.channels.index("ED_GYROX"), self.channels.index("ED_GYROY")]
        self.names = [name[3:] for name in self.channels]
        self.name_dict = {name: i for name, i in zip(self.names,
                                                     xrange(len(self.names)))}
        self.m = len(self.channels)
        self.all_data = np.zeros((25, 2))
        self.raw = np.zeros((14, 2))
        self.gyros = np.zeros((2, 2))
        self.sr = 1 / 128
        self.times = [0.]

        # setup access to binaries
        if sys.platform == 'darwin':
            edk_file = 'libedk.1.0.0.dylib'
        elif sys.platform == 'win32':
            sys.path.append('lib')
            edk_file = 'edk.dll'
        self.edk = CDLL(edk_file)

        self.connected = False

    def connect(self, timeout=10):
        """
        Establishes connection to Emotiv Epoc
        """
        connect_param = c_char_p(b'Emotiv Systems-5')
        self.edk.EE_EngineConnect(connect_param)
        # creation of a datahandle
        self.data_handler = self.edk.EE_DataCreate()
        self.edk.EE_DataSetBufferSizeInSec(5)

        eEvent = self.edk.EE_EmoEngineEventCreate()
        state = self.edk.EE_EngineGetNextEvent(eEvent)
        t0 = time.time()
        while not self.connected:
            state = self.edk.EE_EngineGetNextEvent(eEvent)
            if not state:
                self.connected = True
                self.edk.EE_DataAcquisitionEnable(c_uint(0), c_bool(1))
                break
            if time.time() - t0 > timeout:
                raise Exception('Timeout while connecting to Epoc!')

    def aquire(self, idx):
        nSamples = c_int()
        if not self.connected:
            self.connect()
        while True:
            self.edk.EE_DataUpdateHandle(c_uint(0), self.data_handler)
            #byref returns pointer to nsamples
            self.edk.EE_DataGetNumberOfSample(self.data_handler, byref(nSamples))
            n = nSamples.value
            if not n:
                continue
            container = np.empty((len(idx), n))
            k = 0
            for i in idx:
                data = np.empty((1, n))
                data_ctype = np.ctypeslib.as_ctypes(data)
                self.edk.EE_DataGet(self.data_handler, i, byref(data_ctype),c_uint(n))
                data_read = np.ctypeslib.as_array(data_ctype)
                container[k, :] = data_read[0]
                k += 1
            self.times = np.linspace(self.times[-1] + self.sr,
                                     self.times[-1] + n * self.sr, n)
            return container
    # Get Contact Quality
    #
    # Get the contact quality of a specific sensor.

    def ContactQuality(self, emostatehandle, sensorid):
        return self.EmotivEngineDLL.ES_ContactQuality(emostatehandle, sensorid)

    # Get Battery Charge Level
    #
    # Get the level of charge remaining in the headset battery.
    def BatteryCharge(self, emostatehandle):
        chrglvl = ctypes.c_int()
        maxchrglvl = ctypes.c_int()
        self.EmotivEngineDLL.BatteryCharge(
            emostatehandle, ctypes.byref(chrglvl), ctypes.byref(maxchrglvl))
        returnchrglvl, returnmaxlvl = chrglvl.value, maxchrglvl.value
        return (returnchrglvl, returnmaxlvl)


if __name__ == "__main__":
    e = Epoc()
    while True:
        e.get_raw()
