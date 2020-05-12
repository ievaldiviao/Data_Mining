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
    
    print('Mínimo =', mini)
    print('Máximo =', maxi)
    print('Mediana =', mediana(lista))
    print('1er Cuartil =', p1q)
    print('3er Cuartil =', p3q)
    
def media(lista):
    return sum(lista)/len(lista)
    
def desestan(lista):
    var = 0.0
    for i in lista:
        var += (float(i)-media(lista))**2
    ds = (var/len(lista))**(1/2)
    print('Desviación estandar =', ds)

def correlacion(xi, yi):
    endo, sor1, sor2 = 0, 0, 0
    for i, j in zip(xi, yi):
        x, y = i-media(xi), j-media(yi)
        endo = endo + x * y
        sor1, sor2 = sor1 + x**2, sor2 + y**2
    return endo/(sor1**(1/2) * sor2**(1/2))

def separar(l1):
    aux = []
    d = {}
    for i in l1:
        if i is not np.nan:
            if ';' in i: 
                i = i.split(';')
            aux.append(i)
        else:
            aux.append('NaN')
    for l2 in aux:
        if l2 != 'NaN':
            if isinstance(l2, list): 
                for j in l2:
                    if j not in d:
                        d[j] = 0
            else:
                if l2 not in d:
                    d[l2] = 0
    return aux, d

def agrupar(dato1, dato2):
    lista = []
    dato2, l1 = separar(dato2)
    for i in l1.keys():
        l2 = []
        for d1, d2 in zip(dato1, dato2):
            if isinstance(d2, list): 
                for j in d2:
                    if j == i and not mt.isnan(d1) and j != 'NaN':
                        l2.append(d1)
            elif d2 == i and not mt.isnan(d1) and d2 != 'NaN':
                l2.append(d1)
        l1[i] = l2
        lista.append(l1[i])
    return lista

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

## Inciso 1
#l = list(separar(genero)[1].keys())
#for i in range(len(l)):
#    s_g = agrupar(salario, genero)
#    print('-------', l[i], '-------')
#    summary(s_g[i])
#    desestan(s_g[i])
#    plt.boxplot(s_g[i])
#    plt.show()

## Inciso 2
#l = list(separar(etnia)[1].keys())
#for i in range(len(l)):
#    s_e = agrupar(salario, etnia)
#    print('-------', l[i], '-------')
#    summary(s_e[i])
#    desestan(s_e[i])
#    plt.boxplot(s_e[i])
#    plt.show()

## Inciso 3
#l = list(separar(tdesar)[1].keys())
#for i in range(len(l)):
#    s_d = agrupar(salario, tdesar)
#    print('-------', l[i], '-------')
#    summary(s_d[i])
#    desestan(s_d[i])
#    plt.boxplot(s_d[i])
#    plt.show()
    
# Inciso 4
#l = list(separar(pais)[1].keys())
#for i in range(len(l)):
#    s_p = agrupar(salario, pais)
#    print('-------', l[i], '-------')
#    if s_p[i] == []:
#        print('No se encontraron datos')
#    else:
#        print('Mediana =', mediana(s_p[i]))
#        print('Media =', media(s_p[i]))
#        desestan(s_p[i])

# Inciso 5
#frecPal = []
#for i in tdesar:
#    frecPal.append(tdesar.count(i))
#    plt.title("Frequencies of responses for each developer type")
#    plt.bar(range(len(frecPal)), list(frecPal), edgecolor='black', align='center')
#    plt.show()

# Inciso 9
l = list(separar(lenprog)[1].keys())
for i in range(len(l)):
    e_l = agrupar(edad, lenprog)
    print('-------', l[i], '-------')
    print('Mediana =', mediana(e_l))
    print('Media =', media(e_l))
    desestan(e_l)    