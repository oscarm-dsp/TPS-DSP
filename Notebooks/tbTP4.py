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

#Periodograma de welch para analizar el espectro
w = np.hamming(1024)
f, pW = sig.welch(data, fs=fs, nfft=N, window='hanning', nperseg=int(np.round(N/2)) )


nyq_frec = fs / 2


# filter design
ripple = 0.5 # dB
atenuacion = 40 # dB

ws1 = 0.1 #Hz
wp1 = 0.5 #Hz
wp2 = 30.0 #Hz
ws2 = 40.0 #Hz

frecs = np.array([0.0,         ws1,         wp1,     wp2,     ws2,         nyq_frec   ]) / nyq_frec
gains = np.array([-atenuacion, -atenuacion, -ripple, -ripple, -atenuacion, -atenuacion])
gains = 10**(gains/20)


bp_sos_butter = sig.iirdesign(wp=np.array([wp1, wp2]) / nyq_frec, ws=np.array([ws1, ws2]) / nyq_frec, gpass=0.5, gstop=40., analog=False, ftype='butter', output='sos')
bp_sos_cauer = sig.iirdesign(wp=np.array([wp1, wp2]) / nyq_frec, ws=np.array([ws1, ws2]) / nyq_frec, gpass=0.5, gstop=40., analog=False, ftype='ellip', output='sos')

cant_coef = 501

num_win =   sig.firwin2(cant_coef, frecs, gains , window='blackmanharris' )

den = 1.0

w, h_butter = sig.sosfreqz(bp_sos_butter)
_, h_cauer = sig.sosfreqz(bp_sos_cauer)

ecgbutt = sig.sosfiltfilt(bp_sos_butter, data)
ecgcauer = sig.sosfiltfilt(bp_sos_cauer, data)

start=0
stop=len(data)
plt.plot(ecg_one_lead[start:stop],label='señal')
ecgmed=sig.medfilt(data,201)
plt.plot(ecgmed[start:stop],label='señal')
ecg_med=data-ecgmed
plt.plot(ecg_med[start:stop],label='señal')
