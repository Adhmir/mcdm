# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:14:41 2021

@author: Adhmir Renan Voltolini Gomes
"""


#Apresentação

"""
De acordo com essa necessidade, foi utilizado o método de 
Evaluation Based on Distance from Average Solution (EDAS), 
proposto por Ghorabaee et al. (2015) e que pode ser utilizado 
para resolução de problemas multicriteriais.
Este método seleciona a melhor alternativa em relação à distância da solução média (AV), 
utilizando a distância positiva da média (PDA) e a distância negativa da média (NDA), 
a fim de mostrar a diferença entre cada alternativa e a solução média. 
Sendo que a avaliação das alternativas é feita por meio dos maiores valores de PDA e
menores valores de NDA. 

Pode-se dizer que este método utiliza a solução média a fim de analisar alternativas, 
de forma que a partir dos valores mais altos de PDA e/ou os valores mais baixos de NDA é possível 
verificar a alternativa que é melhor do que a solução média (GHORABAEE et al., 2015).


A segunda etapa refere-se à elaboração da matriz de decisão (X), construída a partir das 
variáveis analisadas no estudo, dispostas conforme alternativas e critérios.

A terceira etapa é a determinação da solução média para cada um dos critérios.

"""
#import time

#start = time.time()


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


def pda(x):
    x = x.copy()
   
    for i in range(len(x.columns)):
        df_refer = x.copy()
        for j in range(len(x)):
            xij = np.float(x.iloc[j,i:i+1].values)
            avj = np.float(df_refer[df_refer.columns[i:i+1]].mean().values)
            pda = (np.max([0,(xij-avj)])/avj)
            x.iloc[j,i:i+1] = pda
            x.add_suffix('_PDA')
    return x
 
 
def nda(x):
    x = x.copy() 
    
    for i in range(len(x.columns)):
        df_refer = x.copy()
        for j in range(len(x)):
            xij = np.float(x.iloc[j,i:i+1].values)
            avj = np.float(df_refer[df_refer.columns[i:i+1]].mean().values)
            nda = (np.max([0,(avj-xij)])/avj)
            x.iloc[j,i:i+1] = nda
            x.add_suffix('_NDA')
    return x
   


def spi_sni(x, pesos):
    
   
    x = x.copy()
    #pesos = [(1/len(x.columns))]
    #pesos = pesos*len(x.columns)
     
    x1 = pda(x.copy())
    x2 = nda(x.copy())
    
    
    x1 = np.sum(x1*pesos, axis=1)
    x1 = x1.rename("spi", inplace = True).reset_index(drop=True) 
    
    x2 = np.sum(x2*pesos, axis=1)
    x2 = x2.rename("sni", inplace = True).reset_index(drop=True)
    
    xa = x1.copy() 
    xb = x2.copy() 
    
    #Normalização
    for i in range(len(x1)):
        xa[i] = x1[i]/np.max(x1)
        xb[i] = 1-(x2[i]/np.max(x2))
    
    xc = pd.concat([xa,xb],axis=1)
    return xc


def edas(x, pesos):
    
    x_pda = pda(x.copy()).reset_index(drop=True)
    x_nda = nda(x.copy()).reset_index(drop=True)
    df_spi_sni = spi_sni(x.copy(), pesos).reset_index(drop=True)
         
    df_spi_sni["EDAS"] = (1/2)*(df_spi_sni['spi']+df_spi_sni['sni'])
    df_spi_sni['Ranking'] = df_spi_sni['EDAS'].rank(method='min', ascending=False)
    
    x = pd.concat([x.copy().reset_index(drop=True),
                   x_pda.add_suffix('_PDA'),
                   x_nda.add_suffix('_NDA'),
                   df_spi_sni],axis=1)
    return x 



#df_teste = edas(df_57.copy())

#df = pd.read_excel('C:/PHD/Disciplinas/06 - Analise Decisoria/Adriana_df.xlsx')
#df = pd.read_excel('C:/PHD/Disciplinas/06 - Analise Decisoria/Artigo fama multicriterio/Python DP2/edas.xlsx')

#df_edas1 = edas(df_edas.copy())

#end = time.time()

#elapsed = time.strftime("%H:%M:%S", time.gmtime(end - start))
 
