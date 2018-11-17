# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:11:57 2018

@author: Turbo
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

# Signal
fs = 512
t = np.arange(8800) / fs
y = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*80*t) + np.sin(2*np.pi*110*t)


# Bartlett's Periodogram
n_fft = 512
Y = np.zeros(n_fft, dtype='complex128')
total_segments = len(t) // n_fft

for i in range(total_segments):
    p1 = i * n_fft                      # segment start position  
    p2 = p1 + n_fft                     # segment end position
    segment = y[p1: p2]
    Y += np.abs(np.fft.fft(segment))**2 / n_fft

psd = Y / total_segments                # average periodogram
psd = psd[0 : n_fft//2]
freq = np.linspace(0, fs, n_fft)        # calc frequency axis
freq = freq[0: n_fft//2]

# Scipy Periodogram
freq2, psd2 = scipy.signal.welch(y, fs, window='boxcar', nperseg=n_fft, noverlap=0, nfft=n_fft, scaling='density')

# Plot output
plt.figure(figsize=(12,6))
plt.title('Average Periodogram')
plt.plot(freq, psd, 'b')
plt.plot(freq2, psd2, 'r')    
plt.xlabel('Freq (Hz)')
plt.xlim([0, fs // 2])
plt.grid()
plt.show()