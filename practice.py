#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:24:12 2020

@author: ievaldiviao
"""
import math as mt
import numpy as np
import pandas as pd

def percentil(lista, perc):
    p = (len(lista) - 1) * perc
    pl = mt.floor(p)
    pu = mt.ceil(p)
    return lista[pl] + (lista[pu] - lista[pl]) * perc

def summary(lista):
    lista.sort()
    maxi = np.max(lista)
    mini = np.min(lista)
    mediana = percentil(lista, 0.5)
    p1q = percentil(lista, 0.25)
    p3q = percentil(lista, 0.75)
    
    print('Mínimo = ', mini)
    print('Máximo = ', maxi)
    print('Mediana = ', mediana)
    print('1er Cuartil = ', p1q)
    print('3er Cuartil = ', p3q)

w_d = '../data/'
i_f = w_d + 'survey_results_public.csv'

data = pd.read_csv(i_f, encoding = 'utf-8')

salario = data['ConvertedComp'].tolist()
sexo = data['Gender'].tolist()

h = [se for sa,se in zip(salario, sexo) if se == 'Man' and not mt.isnan(se)]
m = [se for sa,se in zip(salario, sexo) if se == 'Woman' and not mt.isnan(se)]

print('Salario de Hombres:')
summary(h)
print('Salario de mujeres:')
summary(m)