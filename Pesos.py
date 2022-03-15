# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:45:09 2021

@author: Adhmir Renan Voltolini Gomes
"""

 
from tkinter import Toplevel, ttk, Scrollbar, LabelFrame

def JanPesos(SelectVariables, lista_var, df1):
    RAdr = Toplevel(SelectVariables)
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
         