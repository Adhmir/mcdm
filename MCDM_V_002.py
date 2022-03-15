# -*- coding: utf-8 -*-
"""
'  PHD/Disciplinas/06 - Analise Decisoria/aplicacao
 pyinstaller.exe --onedir -w MCDM_V_001.py
 pyinstaller.exe --onefile -w MCDM_V_001.py


Created on Tue Jun 22 20:03:35 2021
 pyinstaller.exe --onefile -w --icon=Triangulo_mcdm.ico MCDM_V_001.py
 --noconsole
 pyinstaller.exe --onedir -w  --icon=Triangulo_mcdm.ico MCDM_V_001.py
  pyinstaller.exe --onefile --noconsole --icon=choice.ico MCDM_V_001.py
  
  pyinstaller.exe --onefile --noconsole MCDM_V_001.py
  
  pyinstaller.exe --onefile --icon=Triangulo_mcdm.ico MCDM_V_001.py
@author: Adhmir Renan Voltolini Gomes
  --windowed
  --debug 
   PHD/Disciplinas/06 - Analise Decisoria/aplicacao/
pyinstaller.exe --onedir -w --icon=Triangulo_mcdm.ico MCDM_V_001.py

pyinstaller --onefile --noconsole --add-binary "choice.ico." icon=choice.ico MCDM_V_001.py


pyinstaller --onefile -w -F --add-binary "choice.ico;." MCDM_V_001.py
pyinstaller --onefile -w -F --add-binary "choice.ico;." MCDM_V_001.py

"""


"""
A FAZER
INSERIR JANELAS PARA ENTROPIA
O método entropia ainda não foi adicionado pesos externos

ÚLTIMA ALTERAÇÃO foi o método mínimo para o ranking
method='min', 
"""

# Youtube Link da tela inicial: https://www.youtube.com/watch?v=PgLjwl6Br0k

#import tkinter as tk
from tkinter import Tk, LabelFrame, Button, Scrollbar
from tkinter import filedialog, ttk, messagebox #, PhotoImage
#from PIL import ImageTk, Image
#import os


import pandas as pd
import SelectVariables as slv
import SelectVariablesEdas as sledas
import SelectVariablesDp2 as sdp2
import SelectVariablesCso as scso
import SelectVariablesTopsis as stpsis
import SelectVariablesCritic as scritic
import SelectVariablesEntropia as stentrop

# initalise the tkinter GUI
root = Tk()

root.title("Análise Decisória Multicritério")


root.state('zoomed')
#root.geometry("500x500") # set the root dimensions
#root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
#root.resizable(0, 0) # makes the root window fixed in size.


#photo1 = PhotoImage(file = 'choice.ico')
root.iconbitmap('choice.ico')
# Setting icon of master window
#root.iconphoto(False, photo1)

# Frame for open file dialog
file_frame = LabelFrame(root, text="Menu principal")
file_frame.place(height=100, width=1200, rely=0.58, relx=0)


file_frame1 = LabelFrame(root, text="Técnicas multicritérios")
file_frame1.place(height=100, width=1200, rely=0.75, relx=0, )
 

# Buttons
button1 = Button(file_frame, text="Buscar    ",
                    fg = 'white', bg = 'blue', font = 'time 15 bold',
                    command=lambda: File_dialog())
button1.place(rely=0.4, relx=0.10)

button2 = Button(file_frame, text="Carregar", 
                    fg = 'white', bg = 'blue', font = 'time 15 bold',
                    command=lambda: Load_excel_data())
button2.place(rely=0.4, relx=0.20)

button3 = Button(file_frame, text="Limpar  ", 
                    fg = 'white', bg = 'blue', font = 'time 15 bold',
                    command=lambda: clear_data())
button3.place(rely=0.4, relx=0.30)

button4 = Button(file_frame1, text="ADRIANA ", 
                    fg = 'black', bg = 'yellow', font = 'time 15 bold',
                    command=lambda: novajanela())
button4.place(rely=0.4, relx=0.10)

button4 = Button(file_frame1, text="DP2        ", 
                    fg = 'black', bg = 'yellow', font = 'time 15 bold',
                    command=lambda: janelaDp2())
button4.place(rely=0.4, relx=0.20)

button5 = Button(file_frame1, text="EDAS    ", 
                    fg = 'black', bg = 'yellow', font = 'time 15 bold',
                    command=lambda: janelaedas())
button5.place(rely=0.4, relx=0.30)


button6 = Button(file_frame1, text="Topsis", 
                    fg = 'black', bg = 'yellow', font = 'time 15 bold',
                    command=lambda: janelaTopsis())
button6.place(rely=0.4, relx=0.40)


button7 = Button(file_frame1, text="Critic", 
                    fg = 'black', bg = 'yellow', font = 'time 15 bold',
                    command=lambda: janelaCritic())
button7.place(rely=0.4, relx=0.50)

button8 = Button(file_frame1, text="Consenso", 
                    fg = 'black', bg = 'yellow', font = 'time 15 bold',
                    command=lambda: janelaCso())
button8.place(rely=0.4, relx=0.60)


button9 = Button(file_frame1, text="Entropia ", 
                    fg = 'black', bg = 'yellow', font = 'time 15 bold',
                    command=lambda: janelaTopsis())
button9.place(rely=0.4, relx=0.70)

"""
button7 = Button(file_frame1, text="Botão teste ", 
                    fg = 'black', bg = 'yellow', font = 'time 15 bold',
                    command=lambda: janelaDp2())
button7.place(rely=0.4, relx=0.50)
"""

# The file/file path text
label_file = ttk.Label(file_frame, text="Nenhum arquivo selecionado, clique em buscar")
label_file.place(rely=0, relx=0)

# Frame for TreeView
frame1 = LabelFrame(root, text="Conjunto de dados")
frame1.place(height=400, width=1200)


## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget



def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
    label_file["text"] = filename
    return None


def Load_excel_data():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        messagebox.showerror("Information", "Arquivo escolhido inválido")
        return None
    except FileNotFoundError:
        messagebox.showerror("Information", f"{file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None

def pegar_dados():
    file_path = label_file["text"]
    excel_filename = r"{}".format(file_path)
    if excel_filename[-4:] == ".csv":
        df = pd.read_csv(excel_filename)
    else:
        df = pd.read_excel(excel_filename)
        return df
    

def clear_data():
    tv1.delete(*tv1.get_children())
    tv1["column"] = []
   
    return None


#Nova janela ADRIANA
def novajanela():
    slv.novajanela(root, pegar_dados()) 
    


#Nova janela EDAS
def janelaedas():
    sledas.novajanela(root, pegar_dados())
    
    
#Nova janela DP2
def janelaDp2():
    sdp2.novajanela(root, pegar_dados())
    
#Nova janela Topsis
def janelaTopsis():
    stpsis.novajanela(root, pegar_dados())    

#Nova janela Critic
def janelaCritic():
    scritic.novajanela(root, pegar_dados()) 

#Nova janela CONSENSO
def janelaCso():
    scso.novajanela(root, pegar_dados())
    
#Nova janela Entropia
def janelaTopsis():
    stentrop.novajanela(root, pegar_dados())    


#Cálculo do método adriana

root.mainloop()