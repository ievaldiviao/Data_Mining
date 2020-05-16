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
        endo += x * y
        sor1 += x**2
        sor2 += y**2
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

# Inciso 1
#l = list(separar(genero)[1].keys())
#s_g = agrupar(salario, genero)
#for i in range(len(l)):
#    print('-------', l[i], '-------')
#    summary(s_g[i])
#    media(s_g[i])
#    desestan(s_g[i])
#    plt.boxplot(s_g[i])
#    plt.show()

# Inciso 2
#l = list(separar(etnia)[1].keys())
#s_e = agrupar(salario, etnia)
#for i in range(len(l)):
#    print('-------', l[i], '-------')
#    summary(s_e[i])
#    media(s_e[i])
#    desestan(s_e[i])
#    plt.boxplot(s_e[i])
#    plt.show()

# Inciso 3
#l = list(separar(tdesar)[1].keys())
#s_d = agrupar(salario, tdesar)
#for i in range(len(l)):
#    print('-------', l[i], '-------')
#    summary(s_d[i])
#    media(s_d[i])
#    desestan(s_d[i])
#    plt.boxplot(s_d[i])
#    plt.show()
    
# Inciso 4
#l = list(separar(pais)[1].keys())
#s_p = agrupar(salario, pais)
#for i in range(len(l)):
#    print('-------', l[i], '-------')
#    if s_p[i] == []:
#        print('No se encontraron datos')
#    else:
#        print('Mediana =', mediana(s_p[i]))
#        print('Media =', media(s_p[i]))
#        desestan(s_p[i])

# Inciso 5
#c_td = []
#t_d = separar(tdesar)
#for i in t_d[1]:
#    c_td.append(t_d[0].count(i))
#plt.title("Frecuencia de respuesta para cada tipo de desarrollador")
#plt.bar(range(len(c_td)), list(c_td), edgecolor='black', align='center')
#plt.xticks(range(len(t_d[1])), list(t_d[1]), rotation=90)
#plt.show()

# Inciso 6
#a_e = []
#for i in aexper:
#    if i == 'Less than 1 year':
#        a_e.append(0)
#    elif i == 'More than 50 years':
#        a_e.append(50)
#    else: 
#        a_e.append(float(i))
#l = list(separar(genero)[1].keys())
#a_g = agrupar(a_e, genero)
#for i in range(len(l)):
#    plt.title(l[i])
#    plt.hist(a_g[i], bins=10, edgecolor='black')
#    plt.show()

# Inciso 7
#l = list(separar(tdesar)[1].keys())
#h_t = agrupar(hseman, tdesar)
#for i in range(len(l)):
#    print('-------', l[i], '-------')
#    plt.hist(h_t[i], bins=10, edgecolor='black')
#    plt.show()

# Inciso 8
#l = list(separar(genero)[1].keys())
#e_g = agrupar(edad, genero)
#for i in range(len(l)):
#    print('-------', l[i], '-------')
#    plt.hist(e_g[i], bins=10, edgecolor='black')
#    plt.show()
    
# Inciso 9
#l = list(separar(lenprog)[1].keys())
#e_l = agrupar(edad, lenprog)
#for i in range(len(l)):
#    print('-------', l[i], '-------')
#    print('Mediana =', mediana(e_l[i]))
#    print('Media =', media(e_l[i]))
#    desestan(e_l[i])

# Inciso 10
#a_e = []
#for i in aexper:
#    if i == 'Less than 1 year':
#        a_e.append(0)
#    elif i == 'More than 50 years':
#        a_e.append(50)
#    else: 
#        a_e.append(float(i))
#l_ae, l_sa = [], []
#for ae, sa in zip(a_e, salario):
#    if not mt.isnan(ae) and not mt.isnan(sa):
#        l_ae.append(ae)
#        l_sa.append(sa)
#print('Correlación =', correlacion(l_ae, l_sa))

# Inciso 11
#l_e, l_s = [], []
#for ed, sa in zip(edad, salario):
#    if not mt.isnan(ed) and not mt.isnan(sa):
#        l_e.append(ed)
#        l_s.append(sa)
#print('Correlación =', correlacion(l_e, l_s))

# Inciso 12
#l_n_e = []
#for i in nedu:
#    if i == 'I never completed any formal education':
#        l_n_e.append(0.0)
#    elif i == 'Primary/elementary school':
#        l_n_e.append(1.0)
#    elif i == 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)':
#        l_n_e.append(2.0)
#    elif i == 'Associate degree':
#        l_n_e.append(3.0)
#    elif i == 'Bachelor’s degree (BA, BS, B.Eng., etc.)':
#        l_n_e.append(4.0)
#    elif i == 'Some college/university study without earning a degree':
#        l_n_e.append(5.0)
#    elif i == 'Professional degree (JD, MD, etc.)':
#        l_n_e.append(6.0)
#    elif i == 'Master’s degree (MA, MS, M.Eng., MBA, etc.)':
#        l_n_e.append(7.0)
#    elif i == 'Other doctoral degree (Ph.D, Ed.D., etc.)':
#        l_n_e.append(8.0)
#    else:
#        l_n_e.append(i)
#l_ne, l_sa = [], []
#for ne, sa in zip(l_n_e, salario):
#    if not mt.isnan(ne) and not mt.isnan(sa):
#        l_ne.append(ne)
#        l_sa.append(sa)
#print('Correlación =', correlacion(l_ne, l_sa))
#
### Inciso 13
#c_lp = []
#l_p = separar(lenprog)
#for i in l_p[1]:
#    c_lp.append(l_p[0].count(i))
#plt.title("Frecuencia de respuesta para cada tipo de desarrollador")
#plt.bar(range(len(c_lp)), list(c_lp), edgecolor='black', align='center')
#plt.xticks(range(len(l_p[1])), list(l_p[1]), rotation=90)
#plt.show()
