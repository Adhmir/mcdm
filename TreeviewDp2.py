# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:20:24 2021

@author: Adhmir Renan Voltolini Gomes
"""


import algoritmo_dp2_1 as dp2
import pandas as pd
from tkinter import Toplevel, Scrollbar, ttk, LabelFrame, Button
from tkinter import filedialog #, messagebox
 

def novajanela(SelectVariables, lista_var, lstid, lstctg, df1):
    RAdr = Toplevel(SelectVariables)
    RAdr.iconbitmap('choice.ico')
    RAdr.title("Resultado DP2")
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
    
    #messagebox.showerror("Erro cálculo DP2", "Possível matrix singular entre as categorias \n Não foi possível calcular as regressões das categorias")
    
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

   
    def calcular(df):
        #global Metodo_salvar
        #Metodo_salvar = ["calcular"]
        df = dp2.calculo_DP2(df)
        return df
    
    
    def buildDf(df, lista_var, lstid, lstctg):
        dfv = df[lista_var].copy()
        emp = []

        if lstid != emp and lstctg != emp:
            print("lstid != emp and lstctg != emp:")
            df_id = df[lstid].copy()
            df_ctg = df[lstctg].copy()
            dfct = pd.concat([df_id, df_ctg, dfv], axis =1)
            dfPainel = dfct
            dfAd = dfPainel.groupby(lstctg)[lista_var].apply(calcular).reset_index()
            result = pd.merge(dfPainel, dfAd, how="right")
        elif lstctg != emp and lstid == emp:
            print("lstctg != emp and lstid == emp:")
            df_ctg = df[lstctg].copy()
            dfct = pd.concat([df_ctg, dfv], axis =1)
            dfPainel = dfct
            dfAd = dfPainel.groupby(lstctg)[lista_var].apply(calcular).reset_index()
            result = dfAd.copy()
        elif lstctg == emp and lstid != emp:
            print("lstctg == emp and lstid != emp:")
            df_id = df[lstid].copy()
            cdp2 = calcular(dfv)
            result = pd.concat([df_id, cdp2], axis = 1)
        else: 
            print('normal')
            result = calcular(dfv)
        return result
    
    
    df = buildDf(df1, lista_var, lstid, lstctg)
    
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
