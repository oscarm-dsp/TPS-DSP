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
    N = 1000 # cantidad de muestras
    
    #x,tt=sg.Senoidal(1,5,0,N,fs)
    
    t,noise=sg.Ruido(0.1,N,fs)

    t,sen=sg.Senoidal(1,10,0,N,fs)
    
    t,tri=sg.Triang(1,10,0,0.1,N,fs)
    
    t,cua=sg.Rectan(1,10,0,0.8,N,fs)
    
    s=sen
    
    inst.ShowSig(t,s,'Señal')
    
    inst.ShowFFT(s,N,fs)
    
    inst.ShowHist(s,50)
    #%% Presentación gráfica de los resultados
    
 

    


#%% Comienzo de nuestro script
    ##########################

    
# Invocamos a nuestro testbench exclusivamente: 
my_testbench()

    

