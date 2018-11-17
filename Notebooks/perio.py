# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:11:00 2018

@author: Oscar Maffei
"""
import numpy as np

def Periodograma(s,N=1024,n1=1, n2=0):
    if n2==0:
        n2=len(s)
    
    res=(abs(np.fft.fft(s,N))**2)/(n2-n1+1)
    res[0]=res[1]
    
    return(res)
    
    
    