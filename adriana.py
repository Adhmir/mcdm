# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:46:27 2021

@author: Adhmir Renan Voltolini Gomes
"""

import pandas as pd
import numpy as np


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
  
def aquisicao(x):
    for i in range(len(x.columns)):
        x[x.columns[i:i+1]] = x[x.columns[i:i+1]]-x[x.columns[i:i+1]].mean()
    return x           


def naquisicao(x):
    for i in range(len(x.columns)):
        def_norm = x.copy()
        for j in range(len(x)):
            # Pega o valor da linha e coluna normalizado
            xij = x.iloc[j,i:i+1].values
            #Pega a soma da coluna normalizado, a soma é sempre o df que não é modificado
            soma_coluna = def_norm[def_norm.columns[i:i+1]].sum()
            #Pega o grau de liberdade
            grau_liberdade = len(def_norm)-1
            #Pega o valor, diminui da soma menos o valor e divide pelo grau de liberdade
            primeiro_valor = xij-((soma_coluna-xij)/(grau_liberdade))
            # substitui o valor
            x.iloc[j,i:i+1] = primeiro_valor
         
    return x

#Modifiquei para receber a lista de pesos
def ai_tij(x, pesos):
    #pesos = 1/len(x.columns) #retirei a lista de pesos 1 sobre n critério
    x = x.mul(pesos).sum(1)    
    return x

    
def vth(x,y, vlamba = 0.5):
    Vth = (x*vlamba)+(y*(1-vlamba))
    return Vth
    

def f_utilidade(x):
    phi = (1+np.sqrt(5))/2
    if x > 0:
        utl = x/phi*np.sqrt(x)
       
    else:
        utl = -phi*np.sqrt(np.abs(x))
    return utl
   
def adriana(x, pesos, vlamba):
    
    x_norm = normalizar(x.copy())  #adicionei a lista de pesos
    x_norm.rename(lambda x: x+str("_normalizado"), axis=1, inplace=True)
    x_aquisicao = aquisicao(x_norm.copy())
    x_aquisicao.rename(lambda x: x+str("_aquisicao"), axis=1, inplace=True)
    x_naquisicao = naquisicao(x_norm.copy())
    x_naquisicao.rename(lambda x: x+str("_nao_aquisicao"), axis=1, inplace=True)
    
    serie_ai =  ai_tij(x_aquisicao.copy(), pesos) #adicionei a lista de pesos x,  pesos, 
    serie_ai.rename('Valor_ai', inplace = True)
    serie_tij =  ai_tij(x_naquisicao.copy(), pesos)  #adicionei a lista de pesos
    serie_tij.rename('Valor_Tij', inplace = True)    
    Valor_thales =  vth(serie_ai, serie_tij, vlamba) # adicionei o lambda
    Valor_thales.rename('Valor_de_Thaler', inplace = True)
    funcao_utlidade = Valor_thales.apply(f_utilidade)
    funcao_utlidade.rename("Funcao_utilidade", inplace = True)
    
    x = pd.concat([x, x_norm,
                   x_aquisicao, x_naquisicao, 
                   serie_ai, serie_tij, Valor_thales, funcao_utlidade ], axis=1)
    x['ranking'] = x['Valor_de_Thaler'].rank(method='min', ascending=False)
   
    
    
    return x

