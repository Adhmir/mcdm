# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:38:06 2022

@author: Adhmir Renan Voltolini Gomes
"""
 
#import tkinter as tk
from tkinter import Label, Button, Listbox, Toplevel, ANCHOR, END, LabelFrame
from tkinter import ttk, Scrollbar
import TreeviewCritic as tvcritic
#import coeficienteVariacao as coefvar


#SVariable = Tk()

def novajanela(root, df):
   
    SVariable = Toplevel(root)
    SVariable.iconbitmap('choice.ico')
    SVariable.title("Selecionar variáveis CRITIC")
    SVariable.geometry("900x600") # set the root dimensions
    SVariable.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
    SVariable.resizable(0, 0) # makes the root window fixed in size.
    #Labels
    LbNvar = Label(SVariable, text="Variáveis do conjunto de dados",
                        fg = 'black', bg = 'White', font = 'time 8 bold',)
    LbNvar.place(rely=0.01, relx=0.07)
    LbVslct = Label(SVariable, text="Variáveis selecionadas",
                        fg = 'black', bg = 'White', font = 'time 8 bold',)
    LbVslct.place(rely=0.01, relx=0.4)
    """
    LbPesos = Label(SVariable, text="PESOS",
                        fg = 'black', bg = 'White', font = 'time 8 bold',)
    LbPesos.place(rely=0.01, relx=0.75)
    """
    LbId = Label(SVariable, text="Id's",
                        fg = 'black', bg = 'White', font = 'time 8 bold',)
    LbId.place(rely=0.65, relx=0.1)
    LbCtg = Label(SVariable, text="CATEGORIAS",
                        fg = 'black', bg = 'White', font = 'time 8 bold',)
    LbCtg.place(rely=0.65, relx=0.4)
    
    
    #Scrollbar
    scrollbarNvar = Scrollbar(SVariable, orient="vertical")
    scrollbarNsel = Scrollbar(SVariable, orient="vertical")
    #scrollbarNpesos = Scrollbar(SVariable, orient="vertical")
    scrollbarNid = Scrollbar(SVariable, orient="vertical")
    scrollbarCtg = Scrollbar(SVariable, orient="vertical")

    #List box's
    Nvar = Listbox(SVariable, width=25, height=20, yscrollcommand = scrollbarNvar)
    Nvar.place(rely=0.05, relx=0.10)
    scrollbarNvar.config(command=Nvar.yview)

    Nsel = Listbox(SVariable, width=25, height=20,  yscrollcommand = scrollbarNsel)
    Nsel.place(rely=0.05, relx=0.40)
    scrollbarNvar.config(command=Nsel.yview)
    
    """
    Npesos = Listbox(SVariable, width=25, height=20, yscrollcommand = scrollbarNpesos)
    Npesos.place(rely=0.05, relx=0.75)
    scrollbarNvar.config(command=Npesos.yview)
    """
    
    Nid = Listbox(SVariable, width=25, height=5, yscrollcommand = scrollbarNid)
    Nid.place(rely=0.7, relx=0.1)
    scrollbarNvar.config(command=Nid.yview)
    
    Nctg = Listbox(SVariable, width=25, height=5, yscrollcommand = scrollbarCtg)
    Nctg.place(rely=0.7, relx=0.4)
    scrollbarNvar.config(command=Nctg.yview)
    
    listavar = df.columns.tolist()
    Nvar.insert("end", *listavar)
    
    """
    file_frame1 = LabelFrame(SVariable, text="Editar peso selecionado")
    file_frame1.place(height=100, width=190, rely=0.65, relx=0.75, )
     
    txtPeso = ttk.Entry(file_frame1, width = 15, textvariable = Npesos.get(ANCHOR))
    txtPeso.place(rely=0.40, relx=0.01)    
     
    def updatePeso():
        Lpesos = list(Npesos.curselection())
        indexPeso = Lpesos[0]
        print(indexPeso)
        pesos = list(Npesos.get(0,END))
        pesos[indexPeso]
        print(pesos[indexPeso])
        pesos[indexPeso] = txtPeso.get()
        txtPeso.delete(0, 'end') 
        print(pesos[indexPeso])
        print("Valor do texto é :",txtPeso.get())
        Npesos.delete(0,END)
        Npesos.insert("end", *pesos)
        
      
         
    btnEditW = Button(file_frame1, text="Editar", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: updatePeso())
    btnEditW.place(rely=0.01, relx=0.01)        
    """

         
    def selectvar():
        for i in Nvar.curselection():
            varx = Nvar.get(i)
            Nsel.insert("end", varx)
            Nvar.delete(ANCHOR)
            #peso1 = [1]
            #Npesos.insert("end", *peso1)
            
    def desSelectvar():
        for i in Nsel.curselection():
            varx = Nsel.get(i)
            Nvar.insert("end", varx)
            #Lpesos = list(Nsel.curselection())
            #Npesos.delete(Lpesos[0])
            #Nsel.delete(ANCHOR)

    def selectid():
        for i in Nvar.curselection():
            varx = Nvar.get(i)
            Nid.insert("end", varx)
            Nvar.delete(ANCHOR)
            
    def desSelectid():
        for i in Nid.curselection():
            varx = Nid.get(i)
            Nvar.insert("end", varx)
            Nid.delete(ANCHOR)
            
    def selectCat():
        for i in Nvar.curselection():
            varx = Nvar.get(i)
            Nctg.insert("end", varx)
            Nvar.delete(ANCHOR)
            
    def desSelectCat():
        for i in Nctg.curselection():
            varx = Nctg.get(i)
            Nvar.insert("end", varx)
            Nctg.delete(ANCHOR) 
    
    def pvar():
        
        lvar = list(Nsel.get(0,END))
        return lvar
    """
    def Wncriterio():
         Npesos.delete(0,END)
         ncrt = len(list(Nsel.get(0,END)))
         peso = 1/ncrt
         wpesos = []
         for i in range(0,ncrt):
             wpesos.append(peso)
         Npesos.insert("end", *wpesos)

    def wCoefVar():
        lista_var = pvar()
        pesos = coefvar.coefvar(df, lista_var)
        Npesos.delete(0,END)
        Npesos.insert("end", *pesos)
    
    def wConst():
        Npesos.delete(0,END)
        ncrt = len(list(Nsel.get(0,END)))
        peso = 1
        wpesos = []
        for i in range(0,ncrt):
            wpesos.append(peso)
        Npesos.insert("end", *wpesos)
    """
        
    #Botões
    btnPassar = Button(SVariable, text="Selecionar", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: selectvar())
    btnPassar.place(rely=0.3, relx=0.3)
    btnRetirar = Button(SVariable, text="Retirar       ", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: desSelectvar())
    btnRetirar.place(rely=0.4, relx=0.3)
    """
    btnNcst = Button(SVariable, text="Constante", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: wConst())
    btnNcst.place(rely=0.2, relx=0.6)
    btnNcrt = Button(SVariable, text="1/Ncriterios", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: Wncriterio())
    btnNcrt.place(rely=0.3, relx=0.6)
    btnCV = Button(SVariable, text="Coefiente variação ", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: wCoefVar())
    btnCV.place(rely=0.4, relx=0.6)    
    """
    
    btnMadr = Button(SVariable, text="Método CRITIC", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: janelaAdr()) 
    btnMadr.place(rely=0.9, relx=0.8)

    btniD = Button(SVariable, text="Adicionar IDs", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: selectid())   
    btniD.place(rely=0.6, relx=0.1)
    btniD = Button(SVariable, text="Retirar IDs", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: desSelectid())     
    btniD.place(rely=0.6, relx=0.2)
    
    btnCtg = Button(SVariable, text="Add Cat", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: selectCat()) 
    btnCtg.place(rely=0.6, relx=0.4)
    btnCtg = Button(SVariable, text="Del Cat", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: desSelectCat()) 
    btnCtg.place(rely=0.6, relx=0.5)
         

    def janelaAdr():
        #pesos = list(map(float, list(Npesos.get(0,END))))
        #print("Os pesos são :", pesos)
        lista_var = pvar()
        lstid = list(Nid.get(0,END))
        lstctg = list(Nctg.get(0,END))
        #print(lista_var)
        tvcritic.novajanela(SVariable, lista_var, lstid, lstctg,  df)          
 
    SVariable.mainloop()


    


