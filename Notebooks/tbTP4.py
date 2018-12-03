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

fs=1000

mat_struct = sio.loadmat('ECG_TP4.mat')
#
ecg_one_lead =mat_struct['ecg_lead'].flatten()
N = len(ecg_one_lead)

qrs_det=mat_struct['qrs_detections'].flatten()


#Media movil de 10 muestras para reducir el ruido
ecgfil=np.convolve(ecg_one_lead,np.ones(10)/10)

data =ecgfil

hb_1 = mat_struct['heartbeat_pattern1'].flatten()



match=hb_1[::-1]

beats=sig.lfilter(match,1,ecg_med)
beats=np.clip(beats,0,max(beats))
beats=beats/1.5e9
beats=beats**2
plt.plot (beats[455000:475000])


#400
#1920
#