# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:47:09 2018

@author: Oscar Maffei
"""
#%% imports

import numpy as np

#%% Funciones

# Ventanas

def V_Rect(N):
    n=np.linspace(0,N,N).flatten()
    w=np.ones(N)
    return n,w

def V_Hann (N):
    n=np.linspace(0,N,N).flatten()
    w=0.5*(1.0 + np.cos(2*np.pi*(n-N/2)/N))
    return n,w

def V_Bartlett(N):
    n=np.linspace(0,N,N).flatten()
    w=(2/(N-1))*((N-1)/2-np.abs(n-(N-1)/2))
    return n,w

def V_Blackman(N):
    n=np.linspace(0,N,N).flatten()
    w = 0.42 - 0.5 * np.cos(2*np.pi*n/(N-1)) + 0.08*np.cos(4*np.pi*n/(N-1))
    return n,w

def V_Blackman_Harris(N):
    n=np.linspace(0,N,N).flatten()
    w = 0.35875 - 0.48829 * np.cos(2*np.pi*n/(N-1)) + 0.14128*np.cos(4*np.pi*n/(N-1))- 0.01168*np.cos(6*np.pi*n/(N-1))
    return n,w

def V_Blackman_Nuttall(N):
    n=np.linspace(0,N,N).flatten()
    w = 0.3635819 - 0.4891775 * np.cos(2*np.pi*n/(N-1)) + 0.1365995*np.cos(4*np.pi*n/(N-1))- 0.0106411*np.cos(6*np.pi*n/(N-1))
    return n,w

def V_Flattop(N):
    n=np.linspace(0,N,N).flatten()
    w = 1 - 1.93 * np.cos(2*np.pi*n/(N-1)) + 1.29*np.cos(4*np.pi*n/(N-1))- 0.388*np.cos(6*np.pi*n/(N-1)) + 0.028*np.cos(8*np.pi*n/(N-1))
    return n,w
