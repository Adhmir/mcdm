# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 12:34:27 2022

@author: Adhmir Renan Voltolini Gomes
"""

import numpy as np
import pandas as pd

#df =pd.read_excel('C:\PHD\A parte\Contribuições aleatórias\Pedidos ajuda - Professor Nelson\Flex-Nelson\Adhmir-Flex.xlsx')

#df = df.drop('CRM', axis =1)


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

def critic(x):
    df = x.copy()
    df = normalizar(df) 
    df = padronizar(df)
    dfcorr = df.corr() 
    dfcorr1 = 1-dfcorr
    dfcorr1 = dfcorr1.add_suffix('_1Menos')
    somaCorrel = np.array(dfcorr1.sum())
    
    lstDesvpad = []
    for i in range(0,len(df.columns)):
        desvap = np.std(df.iloc[:,i:i+1].values, ddof=1) 
        lstDesvpad.append(desvap)
    
    lstCritic = np.array(lstDesvpad)*np.array(somaCorrel)
   
    CriticTotal = np.sum(lstCritic)
    wCritic = lstCritic/CriticTotal
          
    dfCritic = df.mul(wCritic, axis=1)
    somaDfCritic = dfCritic.sum(axis=1)
      
    df_critic = pd.concat([x, df,somaDfCritic], axis=1) 
    df_critic = df_critic.rename(columns={0: 'Critic'})
    df_critic['ranking'] = df_critic['Critic'].rank(method='min', ascending=False)
   
    return df_critic
 

#df = pd.read_excel('C:/Users/user/Desktop/Random data/topsis.xlsx')
#df = df.drop("Alternativas", axis=1)

def pesosCritic(x):
    df = x.copy()
    df = normalizar(df)
    df = df.add_suffix('_Normalizado')
    df = padronizar(df)
    dfcorr = df.corr()
    dfcorr = dfcorr.add_suffix('_Correlação')
    dfcorr = dfcorr.add_suffix('_corr')
    dfcorr1 = 1-dfcorr
    dfcorr1 = dfcorr1.add_suffix('_1Menos')
    somaCorrel = np.array(dfcorr1.sum())
    
    lstDesvpad = []
    for i in range(0,len(df.columns)):
        desvap = np.std(df.iloc[:,i:i+1].values, ddof=1) 
        lstDesvpad.append(desvap)
    
    lstCritic = np.array(lstDesvpad)*np.array(somaCorrel)
   
    CriticTotal = np.sum(lstCritic)
    
    wCritic = lstCritic/CriticTotal
    
    spesos = pd.Series(wCritic, name='Pesos')
    scorr =pd.Series(somaCorrel,  name='Soma correlação')
    desviosp = pd.Series(lstDesvpad,  name='Desvios padrão') 
    descricao_criterios = pd.Series(x.columns,  name='Critérios')
    valores = pd.concat([desviosp,scorr,spesos,descricao_criterios], axis = 1)
    
    dfcorr = dfcorr.reset_index(drop=True)
    dfcorr1 = dfcorr1.reset_index(drop=True)
    
    df_critic = pd.concat([dfcorr,dfcorr1,valores], axis=1, 
                          ignore_index=False) 
 
    return df_critic


#teste = pesosCritic(df)
#dfCritic = critic(df)

#teste.to_excel('C:\PHD\A parte\Contribuições aleatórias\Pedidos ajuda - Professor Nelson\Flex-Nelson\Pesos-Critic.xlsx')

#print(teste['Pesos'])

#df =pd.read_excel('C:\PHD\A parte\Contribuições aleatórias\Pedidos ajuda - Professor Nelson\Flex-Nelson\Adhmir-Flex.xlsx')
#df = df.drop('CRM', axis =1)

 
def wPesosCritic(x, lista_var):
    df = x[lista_var].copy()
    df = normalizar(df)
    df = padronizar(df)
    dfcorr = df.corr()
    dfcorr = dfcorr.add_suffix('_Correlação')
    dfcorr = dfcorr.add_suffix('_corr')
    dfcorr1 = 1-dfcorr
    dfcorr1 = dfcorr1.add_suffix('_1Menos')
    somaCorrel = np.array(dfcorr1.sum()) 
    lstDesvpad = []
    for i in range(0,len(df.columns)):
        desvap = np.std(df.iloc[:,i:i+1].values, ddof=1) 
        lstDesvpad.append(desvap) 
    lstCritic = np.array(lstDesvpad)*np.array(somaCorrel) 
    CriticTotal = np.sum(lstCritic) 
    wCritic = lstCritic/CriticTotal
    wCritic = list(wCritic) 
 
    return wCritic

#lpesos = wPesosCritic(df, df.columns)