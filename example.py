from pyemotiv import Epoc
from time import sleep
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt


sth=[]
if __name__=="__main__":
    epoc=Epoc()
    datarray=np.zeros((1,4)) #resets datarray every time we run the loop


    for t in range(0,100):
        
        data= epoc.aquire([9]) #gets raw data from channel O1
        datarray = np.concatenate((datarray, data), axis = 1)
        for i in range(0, len(datarray[0])): 
            if datarray[0][i]>0: 
                sth.append(datarray[0][i])
        t=t+1


        t+1

print sth
np.savetxt("onhead.dat", sth, delimiter=',')
        #print data

    #plt.plot(data,t)
