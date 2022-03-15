# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:23:17 2022

@author: Adhmir Renan Voltolini Gomes
Topsis

A fazer zero-size array to reduction operation maximum which has no identity
linha 29 e 30
"""


import numpy as np
import pandas as pd

#df = pd.read_excel('C:/Users/user/Desktop/Random data/topsis.xlsx')

#df = df.drop("Alternativas", axis=1)
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

def topsis(df, pesos):
    df = normalizar(df)
    dfp = df.copy()
    dfn = df.copy()
    dfp = dfp.add_suffix('_positiva')
    dfn = dfn.add_suffix('_negativa') 
      
    for i in range(0,len(df.columns)):
        amais = np.max(df.iloc[:,i:i+1].values)
        amenos = np.min(df.iloc[:,i:i+1].values)
         
        for j in range(0,len(df)):
            xij = df.iloc[j,i:i+1][0]
            quadradoPos = (xij-amais)**2
            dfp.iloc[j,i:i+1] = quadradoPos
        
        
        for l in range(0,len(df)):
            xij = df.iloc[l,i:i+1][0]
            quadradoNeg = (xij-amenos)**2
            dfn.iloc[l,i:i+1] = quadradoNeg
    
    dfp = dfp.mul(pesos, axis=1)
    dfn = dfn.mul(pesos, axis=1)
    
    dpos = np.sqrt(dfp.sum(axis=1))
    dneg = np.sqrt(dfn.sum(axis=1))
    prox = (dneg/(dpos+dneg))
    dftopsis = pd.concat([df, dfp,dfn, dpos,dneg,prox], axis=1) 
    dftopsis = dftopsis.rename(columns={0: 'D+', 1: 'D-',2: 'proximidade'})
    dftopsis['ranking'] = dftopsis['proximidade'].rank(method='min', ascending=False)
   
    return dftopsis

#teste = topsis(df,pesos)

 