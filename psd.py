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
    w=np.ones(N)
    return w,n

def V_Hann (N):
    n=np.linspace(0,1,N).flatten
    w=0.5*(1+np.cos(2*np.pi*(n-N/2)/N))
    return w,n
