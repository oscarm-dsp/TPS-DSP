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


N  = 1000 # muestras
fs = 1000 # Hz

n,w=pds.V_Bartlett(N)

h=np.fft.fft(w)
plt.plot(w)
plt.title("Ventana: Bartlett")
plt.ylabel("Amplitud")
plt.xlabel("n")
plt.show()
plt.figure()

A = np.fft.fft(w, 2048) / (N/2)
mag = np.abs(np.fft.fftshift(A))
freq = np.linspace(-0.5, 0.5, len(A))
resp = 20 * np.log10(mag)
#resp = np.clip(resp, -120, 100)

plt.plot(freq, resp)
plt.title("Respuesta de la ventana Bartlett")
plt.ylabel("Magnitud [dB]")
plt.xlabel("F. Normalizada [ciclos por muestra]")
plt.axis('tight')
plt.show()