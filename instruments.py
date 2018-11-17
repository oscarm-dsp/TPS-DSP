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
#%%   
def Espectro(w, title_s="",title_fft="",bottom=-50,top=10,start=0,stop=0.5,noplot=False,Norm=True,dB=True):
    
    if (noplot==False):
        plt.plot(w)
        plt.title(title_s)
        plt.ylabel("Amplitud")
        plt.xlabel("n")
        plt.grid()
        plt.show()
        plt.figure()
        
    
    
    if (Norm==True):
        A = np.fft.fft(w,8192) / (len(w)/2.0)
        mag=np.fft.fftshift(A / abs(A).max())
    else:
        A = np.fft.fft(w,8192) / (len(w)/2)
        mag=np.fft.fftshift(A)    
        
    minim=len(mag)/2 + len(mag) * start
    maxim=len(mag)/2 + len(mag) * stop 
    
    if (dB==True):
        resp = 20 * np.log10(np.abs(mag[int(minim):int(maxim)])+0.000001)
    else:
        resp=np.abs(mag[int(minim):int(maxim)])
    
    resp = np.clip(resp, bottom, top)
    freq = np.linspace(start, stop, len(resp))
    
    if (noplot==False):
        plt.plot(freq, resp)
        plt.title(title_fft)
        if (dB==True):    
            plt.ylabel("Magnitud [dB]")
        else:    
            plt.ylabel("Magnitud")

        plt.xlabel("F. Normalizada [ciclos por muestra]")
        plt.grid()
        plt.axis('tight')
        plt.show()
       
    return freq,resp
    