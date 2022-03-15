# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:30:06 2021

@author: ADHMIR RENAN VOLTOLINI GOMES
"""

import numpy as np
import pandas as pd


def normalizar(x):
        
    for i in range(len(x.columns)):
        def_norm = x.copy()
        for j in range(len(x)):
            # Pega o valor da linha e coluna
            xij = x.iloc[j,i:i+1].values
            #Pega o máximo da coluna normalizado, sempre do df que não é modificado
            max_coluna = def_norm[def_norm.columns[i:i+1]].max()
            #Pega o grau de liberdade
            min_coluna = def_norm[def_norm.columns[i:i+1]].min()
            #Pega o valor, diminui da soma menos o valor e divide pelo grau de liberdade
            primeiro_valor = ((xij-min_coluna)/(max_coluna-min_coluna))
            # substitui o valor
            x.iloc[j,i:i+1] = primeiro_valor
    #df_norm = (x-x.min())/(x.max()-x.min())
    return x

def coefvar(df, lista_var):
    x = df[lista_var].copy()
    x = normalizar(x)
    listcv = []
    for i in range(len(x.columns)):
        cv = list(np.std(x[x.columns[i:i+1]])/np.mean(x[x.columns[i:i+1]]))[0]
        listcv.append(cv)
    lstw = listcv/np.sum(listcv)
    #print(listcv)
    #print(lstw)
    #print(np.sum(lstw))
    return lstw