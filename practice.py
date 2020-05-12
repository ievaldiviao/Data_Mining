#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:24:12 2020

@author: ievaldiviao
"""
import math as mt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def percentil(lista, perc):
    p = (len(lista) - 1) * perc
    pl = mt.floor(p)
    pu = mt.ceil(p)
    return lista[pl] + (lista[pu] - lista[pl]) * perc

def mediana(lista):
    lista.sort()
    return percentil(lista, 0.5)

def summary(lista):
    lista.sort()
    maxi = lista[-1]
    mini = lista[0]
    p1q = percentil(lista, 0.25)
    p3q = percentil(lista, 0.75)
    
    print('Mínimo = ', mini)
    print('Máximo = ', maxi)
    print('Mediana = ', mediana(lista))
    print('1er Cuartil = ', p1q)
    print('3er Cuartil = ', p3q)
    
def media(lista):
    return sum(lista)/len(lista)
    
def desestan(lista):
    var = 0.0
    for i in lista:
        var += (float(i)-media(lista))**2
    ds = (var/len(lista))**(1/2)
    print('Desviación estandar = ', ds)

def correlacion(xi, yi):
    endo, sor1, sor2 = 0, 0, 0
    for i, j in zip(xi, yi):
        x, y = i-media(xi), j-media(yi)
        endo = endo + x * y
        sor1, sor2 = sor1 + x**2, sor2 + y**2
    return endo/(sor1**(1/2) * sor2**(1/2))

def separar(lista):
    aux = []
    d = {}
    for i in lista:
        if i is not np.nan:
            if ';' in i: 
                i = i.split(';')
            aux.append(i)
        else:
            aux.append('NaN')
    for lista2 in aux:
        if lista2 != 'NaN':
            if isinstance(lista2, list): 
                for item in lista2:
                    if item not in d:
                        d[item] = 0
            else:
                if lista2 not in d:
                        d[lista2] = 0
    return aux, d

def agrupar(lista):
    country, d_c = separar(country)
        for i in d_c.keys():
            l_s = []
            for s, c in zip(salary, country):
                if isinstance(c, list): 
                    for item in c:
                        if item == i and not mt.isnan(s) and item != 'NaN':
                            l_s.append(s)
                elif c == i and not mt.isnan(s) and c != 'NaN':
                    l_s.append(s)
            d_c[i] = l_s

w_d = '../data/'
i_f = w_d + 'survey_results_public.csv'

data = pd.read_csv(i_f, encoding = 'utf-8')

pais = data['Country'].tolist()
nedu = data['EdLevel'].tolist()
tdesar = data['DevType'].tolist()
aexper = data['YearsCode'].tolist()
salario = data['ConvertedComp'].tolist()
hseman = data['WorkWeekHrs'].tolist()
lenprog = data['LanguageWorkedWith'].tolist()
edad = data['Age'].tolist()
genero = data['Gender'].tolist()
etnia = data['Ethnicity'].tolist()

# Inciso 1
#h = [sa for sa,ge in zip(salario, genero) if ge == 'Man' and not mt.isnan(sa)]
#m = [sa for sa,ge in zip(salario, genero) if ge == 'Woman' and not mt.isnan(sa)]
#
#print('Salario de los Hombres:')
#summary(h)
#desestan(h)
#print('Salario de las Mujeres:')
#summary(m)
#desestan(m)
#plt.boxplot([h,m])