# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 16:49:33 2021

@author: Adhmir Renan Voltolini Gomes
"""


#import tkinter as tk
from tkinter import Label, Button, Listbox, Toplevel, ANCHOR, END
from tkinter import Scrollbar
import TreeviewCso as tvcso
  

#SVariable = Tk()

def novajanela(root, df):
   
    SVariable = Toplevel(root)
    SVariable.iconbitmap('choice.ico')
    SVariable.title("Selecionar variáveis CONSENSO")
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
    LbId = Label(SVariable, text="Id's",
                        fg = 'black', bg = 'White', font = 'time 8 bold',)
    LbId.place(rely=0.65, relx=0.1)
    """
    LbCtg = Label(SVariable, text="CATEGORIAS",
                        fg = 'black', bg = 'White', font = 'time 8 bold',)
    LbCtg.place(rely=0.65, relx=0.4)
    """
    
    #Scrollbar
    scrollbarNvar = Scrollbar(SVariable, orient="vertical")
    scrollbarNsel = Scrollbar(SVariable, orient="vertical")
    #scrollbarNpesos = Scrollbar(SVariable, orient="vertical")
    scrollbarNid = Scrollbar(SVariable, orient="vertical")
    #scrollbarCtg = Scrollbar(SVariable, orient="vertical")

    #List box's
    Nvar = Listbox(SVariable, width=25, height=20, yscrollcommand = scrollbarNvar)
    Nvar.place(rely=0.05, relx=0.10)
    scrollbarNvar.config(command=Nvar.yview)

    Nsel = Listbox(SVariable, width=25, height=20,  yscrollcommand = scrollbarNsel)
    Nsel.place(rely=0.05, relx=0.40)
    scrollbarNvar.config(command=Nsel.yview)

    Nid = Listbox(SVariable, width=25, height=5, yscrollcommand = scrollbarNid)
    Nid.place(rely=0.7, relx=0.1)
    scrollbarNvar.config(command=Nid.yview)
    
    """
    Nctg = Listbox(SVariable, width=25, height=5, yscrollcommand = scrollbarCtg)
    Nctg.place(rely=0.7, relx=0.4)
    scrollbarNvar.config(command=Nctg.yview)
    """
    listavar = df.columns.tolist()
    Nvar.insert("end", *listavar)
         
    def selectvar():
        for i in Nvar.curselection():
            varx = Nvar.get(i)
            Nsel.insert("end", varx)
            Nvar.delete(ANCHOR)
            
    def desSelectvar():
        for i in Nsel.curselection():
            varx = Nsel.get(i)
            Nvar.insert("end", varx)

    def selectid():
        for i in Nvar.curselection():
            varx = Nvar.get(i)
            Nid.insert("end", varx)
            Nvar.delete(ANCHOR)
            
    def desSelectid():
        for i in Nsel.curselection():
            varx = Nsel.get(i)
            Nvar.insert("end", varx)
            Lpesos = list(Nsel.curselection())
            Nsel.delete(Lpesos[0])
            #Nsel.delete(ANCHOR)
    """
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
    """
    def pvar():
        
        lvar = list(Nsel.get(0,END))
        return lvar
    
    #Botões
    btnPassar = Button(SVariable, text="Selecionar", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: selectvar())
    btnPassar.place(rely=0.3, relx=0.3)
    btnRetirar = Button(SVariable, text="Retirar       ", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: desSelectvar())
    btnRetirar.place(rely=0.4, relx=0.3)
    
    btnMadr = Button(SVariable, text="Método CONSENSO", 
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
    """
    btnCtg = Button(SVariable, text="Add Cat", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: selectCat()) 
    btnCtg.place(rely=0.6, relx=0.4)
    btnCtg = Button(SVariable, text="Del Cat", 
                        fg = 'black', bg = 'White', font = 'time 8 bold',
                        command=lambda: desSelectCat()) 
    btnCtg.place(rely=0.6, relx=0.5)
    """    

    def janelaAdr():
        
        #print("Os pesos são :", pesos)
        lista_var = pvar()
        lstid = list(Nid.get(0,END))
        lstctg = []
        #lstctg = list(Nctg.get(0,END))
        #print(lista_var)
        tvcso.novajanela(SVariable, lista_var, lstid, lstctg, df)
                  
 
    SVariable.mainloop()


    
