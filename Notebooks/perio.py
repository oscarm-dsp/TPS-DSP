# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:11:00 2018

@author: Oscar Maffei
"""
import numpy as np

def Periodograma(x):
    #de Hayes cap 8.2.1 Fig 8.1
    f=abs(np.fft.fft(x,1024))
    p=(f**2)/len(x)
    p[0]=p[1]
    return p

def PeriodogramaB(x,k=5):
    L=np.int(np.floor(len(x)/k))
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