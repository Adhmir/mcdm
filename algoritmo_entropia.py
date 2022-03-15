# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 17:09:59 2022

@author: Adhmir Renan Voltolini Gomes

Calcular a entropia
"""
import pandas as pd
import numpy as np

#df = pd.read_excel('C:/Users/user/Desktop/Random data/exemploEntropia.xlsx')
#df = df.drop("Alternativas", axis=1)


def normalizar(df):
    x = df.copy()
    for i in range(len(x.columns)):
        def_norm = x.copy()
        for j in range(len(x)):
            xij = x.iloc[j,i:i+1].values
            max_coluna = def_norm[def_norm.columns[i:i+1]].max()
            primeiro_valor = xij/max_coluna
            x.iloc[j,i:i+1] = primeiro_valor
    x = x.add_suffix('_Normalizado')
    return x


#df_normalizado = normalizar(df)

def padronizar(df):
    x = df.copy()
    for i in range(len(x.columns)):
        def_norm = x.copy()
        for j in range(len(x)):
            # Pega o valor da linha e coluna
            xij = x.iloc[j,i:i+1].values
            #Pega a soma da coluna normalizado, sempre do df que não é modificado
            soma_coluna = def_norm[def_norm.columns[i:i+1]].sum()
            #Pega o valor, diminui da soma menos o valor e divide pelo grau de liberdade
            primeiro_valor = xij/soma_coluna
            # substitui o valor
            x.iloc[j,i:i+1] = primeiro_valor
    #df_norm = (x-x.min())/(x.max()-x.min())
    x = x.add_suffix('_Padronizado')
    return x

#df_padronizado = padronizar(df_normalizado)
#df_padronizado = df_padronizado

def entropiaCriterios(df):
    x = df.copy()
    #EnCrt =  []
    df_valor_ent = x.copy()
    df_valor_ent = df_valor_ent.add_suffix('_Entropia')
    for i in range(len(x.columns)):
        for j in range(len(x)):
            # Pega o valor da linha e coluna
            xij = x.iloc[j,i:i+1].values
            #Pega o máximo da coluna normalizado, sempre do df que não é modificado
            xij = xij*np.log(xij)
            df_valor_ent.iloc[j,i:i+1] = xij
    
     
    return df_valor_ent

 
#df_entropiaCriterios = entropiaCriterios(df_padronizado)
  
 
def valorEntropia(df):
    x = df.copy()
    vlrEntropia = list(x.sum())
    valor = []
    for i in vlrEntropia:
        lg =-1/np.log(len(x))
        p = lg*i   
        valor.append(p)
    
    entropiaMax = np.sum(valor)
    lpesos = []
    for i in valor:    
        pesos = (1-i)/(len(x.columns)-entropiaMax)
        lpesos.append(pesos)
    return lpesos

#pesos = valorEntropia(df_entropiaCriterios)
#pesos = pesos*np.array([1])
#entropia = np.sum(df_padronizado*pesos, axis=1)
 
def FuncaoEntropia(x, wpesos = [1]):
    df = normalizar(x) 
    df1 = padronizar(df) 
    df2 = entropiaCriterios(df1) 
    pesos = valorEntropia(df2)  
    pesos = pesos*np.array(wpesos) #multiplicar as listas.
    entropia = np.sum(df1*pesos, axis=1)  
    
    df_entropia = pd.concat([x,df,df1,df2, entropia],axis=1)
    df_entropia = df_entropia.rename(columns={0: 'Entropia'})
    df_entropia['Ranking'] = df_entropia['Entropia'].rank(method='min', ascending=False)
    #df_entropia = entrop['entropia'].rank(ascending=False)
    return df_entropia

#entropia = FuncaoEntropia(df,[0.25,0.25,0.25,0.25])
 