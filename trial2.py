from pyemotiv import Epoc
import numpy as np
import scipy
from scipy import fftpack
from scipy import signal
import matplotlib.pyplot as plt


epoc=Epoc()
datarray=[]
power_avg=[]
time= 0

data= epoc.aquire([9]) #gets raw data from channel O1
datarray.append( data)
print datarray

		#datarray.append(data) 
	