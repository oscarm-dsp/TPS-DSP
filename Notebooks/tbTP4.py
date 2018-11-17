# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:31:55 2018

@author: Oscar Maffei
"""
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import scipy.signal as sg
import scipy as sp
import instruments as inst
import spectrum as spc



fig_sz_x = 14
fig_sz_y = 13
fig_dpi = 80 # dpi

fig_font_family = 'Ubuntu'
fig_font_size = 16


##########################################
# Acá podés generar los gráficos pedidos #
##########################################

# para listar las variables que hay en el archivo
#io.whosmat('ECG_TP4.mat')
mat_struct = sio.loadmat('./ECG_TP4.mat')

ecg_one_lead = mat_struct['ecg_lead'].flatten()
N = len(ecg_one_lead)

hb_1 = mat_struct['heartbeat_pattern1']

#plt.figure(1)
#plt.plot(ecg_one_lead)


fs = 1000 # Hz
nyq_frec = fs / 2


# filter design
ripple = 0.5 # dB
atenuacion = 40 # dB

ws1 = 1.0 #Hz
wp1 = 3.0 #Hz
wp2 = 15.0 #Hz
ws2 = 35.0 #Hz

frecs = np.array([0.0,         ws1,         wp1,     wp2,     ws2,         nyq_frec   ]) / nyq_frec
gains = np.array([-atenuacion, -atenuacion, -ripple, -ripple, -atenuacion, -atenuacion])
gains = 10**(gains/20)



bp_sos = sg.iirdesign(wp=np.array([wp1, wp2]) / nyq_frec, ws=np.array([ws1, ws2]) / nyq_frec, gpass=0.5, gstop=40., analog=False, ftype='butter', output='sos')

cant_coef = 1024

#num_firls = sig.firls(cant_coef, frecs, gains, fs=fs)
#num_remez = sig.remez(cant_coef, frecs, gains[::2], fs=fs)

den = 1.0

w, h_butter = sg.sosfreqz(bp_sos)

w = w / np.pi * nyq_frec

# Procedemos al filtrado
ECGfil = sg.sosfiltfilt( bp_sos, ecg_one_lead)

Inter= ecg_one_lead-2*ECGfil


#f,x=inst.Espectro(ecg_one_lead,fs)

#perio =sg.periodogram(ecg_one_lead,fs )
#per= spc.speriodogram(ecg_one_lead.None,True,fs)
inst.Espectro(ecg_one_lead,fs=1000,Norm=False,dB=False,start=0,stop=0)


per=sg.welch(ecg_one_lead, fs=fs, nfft=len(ecg_one_lead), window='hanning', nperseg=int(np.round(len(ecg_one_lead)/3)) )


#plt.figure()
#plt.plot(perio[1])
#plt.figure()
#plt.plot(per[0],per[1])
#plt.plot(f)
#plt.plot(ecg_one_lead)
#plt.plot(ECGfil)
#plt.plot(Inter)

