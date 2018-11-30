# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:10:30 2018

@author: Oscar Maffei
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sg
import spectrum as sp
import scipy.stats as st

N=[10,50,100,250,500,1000,5000]
fs=1000


def Periodograma(x):    
    p=sg.periodogram(x,fs,nfft=10*len(x))
    return p[1]


def PeriodogramaB(x,k=5):
    p=sg.welch(x,fs,window='bartlett',nperseg=k,noverlap=None,nfft=10*len(x))
    return p[1]    
    
def PeriodogramaM(x):
    w=np.hamming(len(x))
    s=x*w/max(w)
    p=Periodograma(s)
    return p

def PeriodogramaW(x,L,ovr=None):
    p=sg.welch(x,fs,window='hann',nperseg=L,noverlap=ovr,nfft=10*len(x))
    return p[1]  

R = 200 # realizaciones

N = 1000 # Muestras

# Obtené los valores XX para que cumplas con el enunciado
#SNR = np.array([ XX, XX ], dtype=np.float)

##########################################
# Acá podés generar los gráficos pedidos #
##########################################
#Por Welch
k=np.linspace(0,N-1,N)
Wn=np.pi * np.ones(R)/2
Ww3=np.zeros(R)
Ww10=np.zeros(R)

fr=np.random.uniform(-0.5,0.5,N)
W=np.pi/2 + fr*2*np.pi/N 
n=0.25*np.random.normal(0,np.sqrt(2),N)

s3=1.4142 * np.sin(W * k)
s10=3.16 * np.sin(W * k) 


for i in range(R):
    fr=np.random.uniform(-0.5,0.5,N)
    n=0.25*np.random.normal(0,2,N)
    W=np.pi/2 + fr*2*np.pi/N 
    s3=1.4142 * np.sin(W * k) + n
    s10=3.16 * np.sin(W * k) + n
    #Pw=sg.welch(s3, fs=fs, nfft=N,nperseg=int(np.round(N/3)))
    Pw=PeriodogramaW(s3,20,5)
    Ww3[i]= np.pi * np.argmax(Pw)/(len(Pw))
    #Pw=sg.welch(s10, fs=fs, nfft=N,nperseg=int(np.round(N/3))) 
    Pw=PeriodogramaW(s10,20,5)
    
    Ww10[i]=np.pi * np.argmax(Pw)/(len(Pw))
    
#Por Bartlett
Ww=np.transpose(np.vstack([Wn,Ww3,Ww10]))
plt.title("Método de Welch")
line_hdls= plt.plot(Ww)
axes_hdl = plt.gca()
axes_hdl.legend(line_hdls, ['Real','SNR=3dB','SNR=10dB'], loc='upper right'  )

for i in range(R):
    fr=np.random.uniform(-0.5,0.5,N)
    n=0.25*np.random.normal(0,2,N)
    W=np.pi/2 + fr*2*np.pi/N 
    s3=1.4142 * np.sin(W * k) + n
    s10=3.16 * np.sin(W * k) + n
    Pw=PeriodogramaB(s3,20)
    Ww3[i]=np.pi * np.argmax(Pw)/(len(Pw))
    Pw=PeriodogramaB(s10,20) 
    Ww10[i]=np.pi * np.argmax(Pw)/(len(Pw))
    

Ww=np.transpose(np.vstack([Wn,Ww3,Ww10]))
plt.figure(2)
plt.title("Método de Bartlett")
line_hdls= plt.plot(Ww)
axes_hdl = plt.gca()
axes_hdl.legend(line_hdls, ['Real','SNR=3dB','SNR=10dB'], loc='upper right'  )