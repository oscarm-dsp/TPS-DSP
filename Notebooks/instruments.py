# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:20:16 2018

@author: Oscarm
"""
#
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
#%%
def ShowFFT(sig,N,fs):

    # Number of samplepoints
    
    # sample spacing
    T = 1/fs
    yf = scipy.fftpack.fft(sig)
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
    
    fig, ax = plt.subplots()
    ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
    plt.grid()
    plt.show()
    
    #return yf,xf
#%%
def ShowSig(x,y,titulo=''):
    #plt.figure(1)
    plt.plot(x, y)
    plt.title(titulo)
    plt.xlabel('tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.grid()
    plt.show()
#%%    
def NormAmp(x):
    res=x/max(x)
    return res
#%%
def Cuantificar(x,n):
    res=np.floor(x*2**n)
    return res
#%%    
def ShowHist(s,bins='auto'):
    
    plt.hist(s, bins)  # arguments are passed to np.histogram
    plt.title("Histograma")
    plt.grid()
    plt.show()
    
    