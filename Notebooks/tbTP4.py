# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:31:55 2018

@author: Oscar Maffei
"""
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy as sp
import instruments as inst
import spectrum as spc
import z_plane as zp
import siggen as sg
import perio as per

N=256
fs=1000


t=np.linspace(0,(N-1),N)
th=np.random.uniform(-np.pi/50,np.pi/50,N)
ns=np.random.normal(0,1,N)

s=5*np.sin(t*0.1*np.pi)+ns


plt.figure()
plt.plot(s)
#s=np.pad(s,1024,'constant')
p=per.Periodograma(s)
pdb=20* np.log10(p+0.000000001)

W=np.linspace(0,2*np.pi,len(p))

plt.figure()
plt.plot(W,p)
print (np.mean(p),np.var(p))



#data=[[p.mean(),p.var()] for p in Pw]


#400
#1920
#