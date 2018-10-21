# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:42:33 2018

@author: Oscar Maffei
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas import DataFrame
from IPython.display import HTML
import instruments as inst
import siggen as sig
import pds2018 as pds
import operator as op

N  = 1000 # muestras
fs = 1000 # Hz

#%% Funciones
def Graficar(w, ventana="",bottom=-50,top=10,span=0.1):

    plt.plot(w)
    plt.title("Ventana: "+ ventana)
    plt.ylabel("Amplitud")
    plt.xlabel("n")
    plt.grid()
    plt.show()
    plt.figure()
    
    
    A = np.fft.fft(w,2048) / (len(w)/2.0)
    freq = np.linspace(-span, span, 2*len(A)*span)
    mag=np.fft.fftshift(A / abs(A).max())
    minim=int(len(A)/2 - len(A)*span)
    maxim=int(len(A)/2 + len(A)*span)
    resp = 20 * np.log10(np.abs(mag[minim:maxim])+0.000001)
    resp = np.clip(resp, -50, 100)
    
    plt.plot(freq, resp)
    plt.title("Respuesta de la ventana " + ventana)
    plt.ylabel("Magnitud [dB]")
    plt.xlabel("F. Normalizada [ciclos por muestra]")
    plt.grid()
    plt.axis('tight')
    
    plt.show()

def Espectro(w, title_s="",title_fft="",bottom=-50,top=10,span=0.5,):

    plt.plot(w)
    plt.title(title_s)
    plt.ylabel("Amplitud")
    plt.xlabel("n")
    plt.grid()
    plt.show()
    plt.figure()
    
    
    A = np.fft.fft(w,2048) / (len(w)/2.0)
    mag=np.fft.fftshift(A / abs(A).max())
    minim=int(len(A)/2 - len(A)*span)
    maxim=int(len(A)/2 + len(A)*span)
    resp = 20 * np.log10(np.abs(mag[minim:maxim])+0.000001)
    resp = np.clip(resp, bottom, top)
    freq = np.linspace(-span, span, len(resp))
    
    
    plt.plot(freq, resp)
    plt.title(title_fft)
    plt.ylabel("Magnitud [dB]")
    plt.xlabel("F. Normalizada [ciclos por muestra]")
    plt.grid()
    plt.axis('tight')
    
    print(len(resp))
    print(max(resp[0:40]))
    plt.show()

def Espectro05(w, title_s="",title_fft="",bottom=-50,top=10,start=0,stop=0.5,noplot=False,Norm=True,dB=True):
    
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

#%% script
    
reps=200

def get_a1(x,w,n0,n1):
    
    res=np.zeros(reps)
    
    for i in range(0,reps):  
        xr=x[i]*w
        f,X=Espectro05(xr,"","",-20,10,0.24,0.26,True,False,False)  
        res[i]=np.sqrt(((X[65]+X[97])**2)/5)
    
    return res
    
k=np.linspace(0,N-1,N).flatten()


i=np.linspace (0,4,5, endpoint=True, retstep=False, dtype=int)
x0=2*np.sin((np.pi/2) * k)

x=[2*np.sin((np.pi/2 + ((2*((2*np.random.rand(1))-1)) * (2*np.pi)/N))*k)]*reps

for i in range(0,reps):
    x[i]=2*np.sin((np.pi/2 + ((2*((2*np.random.rand(1))-1)) * (2*np.pi)/N))*k)

f,X=Espectro05(x0,"","",-20,10,0.24,0.26,False,False,False)
W0=f[X.argmax()]
a0=X[X.argmax()]

na=65
nb=97

print (na,nb)

nn,w=pds.V_Rect(N)
ar=get_a1(x,w,na,nb)
inst.ShowHist(ar)

nn,w=pds.V_Bartlett(N)
ab=get_a1(x,w,na,nb)
inst.ShowHist(ab)

nn,w=pds.V_Hann(N)
ah=get_a1(x,w,na,nb)
inst.ShowHist(ah)

nn,w=pds.V_Blackman(N)
abm=get_a1(x,w,na,nb)
inst.ShowHist(abm)

nn,w=pds.V_Flattop(N)
aft=get_a1(x,w,na,nb)
inst.ShowHist(aft)

sr=ar.mean()-a0
vr=ar.var()
sb=ab.mean()-a0
vb=ab.var()
sh=ah.mean()-a0
vh=ah.var()
sbm=abm.mean()-a0
vbm=abm.var()
sft=aft.mean()-a0
vft=aft.var()
