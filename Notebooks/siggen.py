# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 20:19:45 2018

@author: Oscarm
"""

import numpy as np
import scipy.signal as signal


#%% Señal senoidal
def Senoidal(amplitud, frecuencia, fase, N, fs):
    
    ts=1/fs
    
    #Genero el eje de abcisas
    x = np.linspace(0, (N-1)*ts, N).flatten()
    
    #genero el eje de ordenadas de N muestras
    
    y=amplitud * np.sin(frecuencia * 2.0*np.pi*x + fase)
    
    return x,y
#%% Ruido blanco gausiano
def Ruido (varianza,N,fs)    :
    
    ts=1/fs
    
    #Genero el eje de abcisas
    x = np.linspace(0, (N-1)*ts, N).flatten()
    
    #genero el eje de ordenadas de N muestras
    #y = np.array([], dtype=np.float).reshape(N,0)
    
    
    y = np.sqrt(varianza) * 2*np.random.rand(N,1).flatten()
    
    y=y-np.average(y)
    
    # para concatenar horizontalmente es necesario cuidar que tengan iguales FILAS
    #x = np.hstack([x, aux] )
    return x,y
#%% Señal triangular de simetria variable
def Triang(amplitud,frecuencia,fase=0,sim=0.5, N=1000,fs=1000):
    ts=1/fs
    
    #Genero el eje de abcisas
    t = np.linspace(0, (N-1)*ts, N).flatten()
        
    y = signal.sawtooth(2 * np.pi * frecuencia * t, sim)    
    return t,y

#%%
def Rectan(amplitud,frecuencia,fase=0,D=0.5, N=1000,fs=1000):
    ts=1/fs
    
    #Genero el eje de abcisas
    t = np.linspace(0, (N-1)*ts, N).flatten()
        
    y = signal.square(2 * np.pi * frecuencia * t, D)    
    return t,y