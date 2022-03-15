# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:45:37 2021

@author: Adhmir Renan Voltolini Gomes
"""

import pandas as pd
import numpy as np

#df = pd.read_excel('CONSENSO.xlsx')


#df = pd.read_excel('C:/PHD/Disciplinas/06 - Analise Decisoria/Dp2_df.xlsx')
 
#lista_unicos = np.unique(df)
#df = df.drop(["Aluno"], axis = 1)

"""
Elaborar uma função que permita calcular a probabilidade, independentemente
se o valor é observado no instrumento.
Valores = [1,2,3,4,5]
"""

def consenso(x):
    
    Valores = np.unique(x) 
    x = x.copy()
    nome_colunas = x.columns
    x_prob = x.apply(pd.value_counts).fillna(0)/len(x)
    xa = pd.DataFrame([],columns=([x.columns]))     
   
    serie_media = x.mean(axis = 0)
     
    
    for i in range(len(serie_media)):
        lista_valor = []
        for j in range(len(Valores)):
            valor = np.log2(1-(np.abs(serie_media[i]-Valores[j])/(np.max(Valores)-np.min(Valores))))
            
            lista_valor.append(valor)        
        xa.iloc[:,i] = lista_valor    
    df_mul = xa.values * x_prob.values    
    df_sum = 1+df_mul.sum(axis=0)
    df_sum = pd.DataFrame(df_sum).T    
    x = pd.DataFrame( np.concatenate( (x.values, df_sum.values), axis=0 ) )
    x.columns = nome_colunas
    
    return x


#df_teste = consenso(df.copy())
 
