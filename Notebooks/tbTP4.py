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
import siggen as sg
import perio as per



def BeatDet(x,th):
    
    n= []
    start=0
    for i in range(len(x)):
        if start==0:
            if x[i]>th: 
                start=i
        else:
            if x[i]<th:
                n.append(start + np.argmax(x[start:i]))
                start=0
            
    return n
    




fs=1000

mat_struct = sio.loadmat('ECG_TP4.mat')
#
ecg_one_lead =mat_struct['ecg_lead'].flatten()
N = len(ecg_one_lead)

qrs_det=mat_struct['qrs_detections'].flatten()


#Media movil de 10 muestras para reducir el ruido
ecgfil=np.convolve(ecg_one_lead,np.ones(10)/10)

data =ecgfil/max(ecgfil)

hb_1 = mat_struct['heartbeat_pattern1'].flatten()
hb_1=hb_1/max(hb_1)

match=hb_1[::-1]
plt.plot (data[455000:475000])
beats=sig.lfilter(match,1,data)
plt.plot (beats[455000:475000])
beats=np.clip(beats,0,max(beats))
beats=beats
beats=beats**2
plt.plot (beats[455000:475000])

bt=BeatDet(beats[455000:475000],40)

[plt.axvline (x,0,1,color='r',linestyle='--') for x in bt]

#400
#1920
#