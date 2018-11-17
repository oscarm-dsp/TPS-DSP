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
    p=(1/len(x))* abs(np.fft.fft(x))**2
    p[0]=p[1]
    return p




def PeriodogramaB(x,k=5):
    L=int(len(x)/k)
    p=np.zeros(L)
    n=0
    for i in range(k):
        p=p+Periodograma(x[n:n+L])/k
        n=n+L    
    return p

def PeriodogramaM(x):
    w=np.hamming(len(x))
    s=x*w/max(w)
    p=Periodograma(s)
    return p

def PeriodogramaW(x,L,ovr=0):
    n=0
    stp=(1-ovr)*L
    k=1+np.floor((len(x)-L)/stp)
    p=np.zeros(L)
    for i in range(int(k)):
        p=p+PeriodogramaM(x[n:n+L])/k
        n=n+int(stp)
    
    return p 

#ruido normal de varianza 2

sn= [np.random.normal(0,np.sqrt(2),n).flatten() for n in N]

R=200
N=1000

k=np.linspace(0,N-1,N)
Wn=np.pi * np.ones(200)/2
Ww3=np.zeros(200)
Ww10=np.zeros(200)
for i in range(200):
    fr=np.random.uniform(-0.5,0.5,N)
    n=np.random.normal(0,2,N)
    W=np.pi/2 + fr*2*np.pi/N 
    s3=3.3 * np.sin(W * k) + n
    s10=4.7 * np.sin(W * k) + n
    Pw=sp.speriodogram(s3,N)
    Ww3[i]=2* np.pi * np.argmax(Pw)/len(Pw)
    Pw=sp.speriodogram(s10,N) 
    Ww10[i]=2*np.pi * np.argmax(Pw)/len(Pw)
    

Ww=np.transpose(np.vstack([Wn,Ww3,Ww10]))

#plt.title("Método de Welch")
line_hdls= plt.plot(Ww)
axes_hdl = plt.gca()
axes_hdl.legend(line_hdls, ['Real','SNR=3dB','SNR=10dB'], loc='upper right'  )
