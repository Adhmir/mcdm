# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:41:18 2021

@author: Adhmir Renan Voltoni Gomes
"""
import pandas as pd
import MCDM_V_001 as mcdm

def pegar_dados():
    file_path = mcdm.label_file["text"]
    excel_filename = r"{}".format(file_path)
    if excel_filename[-4:] == ".csv":
        df = pd.read_csv(excel_filename)
    else:
        df = pd.read_excel(excel_filename)
        return df
