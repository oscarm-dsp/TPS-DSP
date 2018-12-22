# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 21:51:59 2018

@author: Oscar Maffei
"""
import numpy as np
import scipy.signal as sg
import matplotlib.pyplot as plt


Q= [1000,500,200,100,50,20,10,5,2,1]

num = 1
Den =[[1,1/q,1] for q in Q]

S=[sg.lti(num,den) for den in Den]
B=[sg.bode(s) for s in S]

[plt.semilogx(b[0],b[1]) for b in B]



E=[d[1]/2 for d in Den]
wmax=[np.sqrt(1-(2*e**2)) for e in E]
pkt=[-20* np.log10(2*e *np.sqrt(1-e**2)) for e in E]
pkg=[max(b[1]) for b in B]