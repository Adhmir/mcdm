# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:48:51 2021

@author: Adhmir Renan Voltolini Gomes

Carrega o tree view com o método Adriana
"""


import adriana as adr
import pandas as pd
from tkinter import Toplevel, Scrollbar, ttk, LabelFrame, Button
from tkinter import filedialog
 

def novajanela(SelectVariables, pesos, lista_var, lstid, lstctg, vlamba, df1):
    RAdr = Toplevel(SelectVariables)
    RAdr.iconbitmap('choice.ico')
    RAdr.title("Resultado Adriana")
    RAdr.state('zoomed')
        
    # Frame for TreeView
    frame1 = LabelFrame(RAdr, text="Conjunto de dados")
    frame1.place(height=400, width=1200)

    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1)
    
    treescrolly = Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
    treescrollx = Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget
         
    def salvar():
        try:
            # with block automatically closes file
            with filedialog.asksaveasfile(mode='w', defaultextension=".xlsx") as file:
                df.to_excel(file.name, index = False)
        except AttributeError:
            # if user cancels save, filedialog returns None rather than a file object, and the 'with' will raise an error
            print("Ação salvar cancelada!")
        
    
    btnSalvar = Button(RAdr, text="SALVAR", 
                        fg = 'black', bg = 'White', font = 'time 12 bold',
                        command=lambda: salvar())
    btnSalvar.place(rely=0.6, relx=0.8)

   
    def calcular(df, pesos, vlambda):
        #global Metodo_salvar
        #Metodo_salvar = ["calcular"]
        df = adr.adriana(df, pesos, vlambda)
        return df
    
    
    def buildDf(df, lista_var, lstid, lstctg, pesos, vlambda):
        dfv = df[lista_var].copy()
        w = pesos
        lbda = vlambda
        emp = []

        if lstid != emp and lstctg != emp:
            
            print("lstid != emp and lstctg != emp:")
            
            df_id = df[lstid].copy()
            df_ctg = df[lstctg].copy()
            dfct = pd.concat([df_id, df_ctg, dfv], axis =1)
            dfPainel = dfct
            dfAd = dfPainel.groupby(lstctg)[lista_var].apply(calcular, 
                                                             pesos = w, 
                                                             vlambda = lbda).reset_index()
            result = pd.merge(dfPainel, dfAd, how="right")
            
        elif lstctg != emp and lstid == emp:
            print("lstctg != emp and lstid == emp:")
    
            
            df_ctg = df[lstctg].copy()
            dfct = pd.concat([df_ctg, dfv], axis =1)
            dfPainel = dfct
            dfAd = dfPainel.groupby(lstctg)[lista_var].apply(calcular, 
                                                             pesos = w, 
                                                             vlambda = lbda).reset_index()
            result = dfAd.copy()
            
        elif lstctg == emp and lstid != emp:
            print("lstctg == emp and lstid != emp:")
            
            df_id = df[lstid].copy()
            adr =  calcular(dfv, w, lbda)
            result = pd.concat([df_id, adr], axis = 1)
            
        else: 
            print('normal')
            result = calcular(dfv, w, lbda)
            
        return result
    
    
    df = buildDf(df1, lista_var, lstid, lstctg, pesos, vlamba)
    
    def clear_data():
        tv1.delete(*tv1.get_children())
        tv1["column"] = []   
        return None
    
    clear_data()
    
    
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row)
    
    RAdr.mainloop()