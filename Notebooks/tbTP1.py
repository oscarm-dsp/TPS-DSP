# -*- coding: utf-8 -*-
"""
Created on ...

@author: ...

Descripción:
------------

Este testbench sigue con el ejemplo del "testbench0" pero agrega algunas funcionalidades
como la posibilidad de ejecutarlo a través de la consola, haciendo algún parseo de argumentos.

"""

# Ejemplificaremos el uso de las herramientas que utilizaremoos frecuentemente 

# Importación de módulos que utilizaremos en nuesto testbench:
# Una vez invocadas estas funciones, podremos utilizar los módulos a través del identificador que indicamos luego de "as". 
# Por ejemplo np.linspace() -> función linspace dentro e NumPy
import numpy as np
#import scipy.signal as sig
import matplotlib as mpl
# la siguiente línea solo afecta en caso que lo quisiéramos correr desde la línea de comandos
mpl.use('Qt5Agg')

import time
import matplotlib.pyplot as plt
import siggen as sg
import instruments as inst

###################################
## Formas de incluir comentarios ##
###################################

# Comentarios con "#"

""" Bloques de comentario
    bla bla bla
    bla ...
"""

#%% Separación de bloques de código para ordenar tu trabajo "#%%"

#%%  Inicialización

#%%  Generación de señales de prueba

#%%  Presentación de resultados


#%%  Inicialización de librerías

# Setup inline graphics
mpl.rcParams['figure.figsize'] = (10,10)

#%%  Testbench: creamos una función que no recibe argumentos para asegurar que siempre encontraremos nuestro espacio de variables limpio.
# Prestar atención al indentado, ya que Python interpreta en función del indentado !!

def my_testbench():
    
    # Datos generales de la simulación
    fs = 1000.0 # frecuencia de muestreo (Hz)
    N = 1000  # cantidad de muestras
    
    #x,tt=sg.Senoidal(1,5,0,N,fs)
    
    s=[]
    
    
    t,sa=sg.Senoidal(1,9*fs/N,0,N,fs)
    
    
    
    
    s=np.append(sa[:111],sa[56:111+56])
    s=np.append(s,np.zeros(778))
    
    
    inst.ShowSig(t,s)
    
    f,f1=inst.ShowFFT(s,N,fs)
    
    inst.ShowFFT(s,N,fs,1,"Señal Original",0,35)
    
    f2=f1**2
    
    print (np.sum(f2))
    
    print (f2[9])
    
    print(np.argmax(f2))
    


#%% Comienzo de nuestro script
    ##########################

    
# Invocamos a nuestro testbench exclusivamente: 
my_testbench()

    

