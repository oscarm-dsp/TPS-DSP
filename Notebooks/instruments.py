# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:20:16 2018

@author: Oscar Maffei
"""
#
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import cmath as cm
#%% Genera y/o grafica la FFT de una señal
def ShowFFT(sig,N,fs,show=0,titulo='',start=0,stop=0):

    # Number of samplepoints
    
    # sample spacing
    T = 1/fs
    
    start=start * N / fs 
    if stop==0:
        stop=N/2
    else:
        stop=stop * N / fs
            
    yf = scipy.fftpack.fft(sig)
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
    
    if show==1:
        fig, ax = plt.subplots()
        ax.plot(xf[int(start):int(stop)], 2.0/fs * np.abs(yf[int(start):int(stop)]))
        plt.grid()
        plt.xlabel("Frecuencia[Hz]")
        plt.ylabel("|Amplitud|")
        
        if titulo=='':    
            plt.title("FFT")
        else:
            plt.title(titulo)
        
        plt.show()
    
    return xf[int(start):int(stop)],2.0/fs * np.abs(yf[int(start):int(stop)])
    
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
#%% cuantifica una señal con n bits
def Cuantificar(s,n,fsq=0):
    x=s-min(s)
    x=x/max(x)  
    res=np.floor(x*2**n)  
    
    return res

#%% cuantifica una señal con n bits
def CuantificarB(s,n,fsq=0):
    res=np.floor(s*2**(n-1))/(2**(n-1))  
    
    return res

#%%    
def ShowHist(s,bins='auto'):
    
    plt.hist(s, bins)  # arguments are passed to np.histogram
    plt.title("Histograma")
    plt.grid()
    plt.show()
    
#%% Transformada de Forurier de una secuencia
def MyDFT(sig,N,fs,show=0,titulo=''):
    
    T = 1/fs
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
    
    yf = []
    
    for m in range(N):
        y = 0.0
        for n in range(N):
            y += sig[n] * cm.exp(- 1j * 2* np.pi * m * n / N)
        yf.append(y)
    
    if show==1:
        fig, ax = plt.subplots()
        ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
        plt.grid()
        
        if titulo=='':
            plt.title("DFT")
        else:
            plt.title(titulo)
            
        plt.show()
        
    else:
        return yf,xf
    
