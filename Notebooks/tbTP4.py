# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:31:55 2018

@author: Oscar Maffei
"""
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy as sp
import instruments as inst
import spectrum as spc
import z_plane as zp


N=1000
fs=1000

mat_struct = sio.loadmat('./ECG_TP4.mat')
#
ecg_one_lead =mat_struct['ecg_lead'].flatten()
N = len(ecg_one_lead)

#Media movil de 10 muestras para reducir el ruido
ecgfil=np.convolve(ecg_one_lead,np.ones(10)/10)

data =ecgfil

for i in range (int(N-1)):
    data[i]=data[i]-data[i+1]

print (np.argmax(data[0:500]))
print (np.argmax(data[5000:1500]))
print (np.argmax(data[1500:2500]))
print (np.argmax(data[2500:3000]))


#400
#1920
#