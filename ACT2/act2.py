# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:06:48 2023

@author: compa
"""

import tkinter as tk
from tkinter import END, messagebox

root =tk.Tk()
root.title("Practica_2")
valor = 0
def Mes():
    global valor
    try:
        valor = int(txtNumero.get());
        if valor == 1:
            mes = "Enero"
        elif valor == 2:
            mes = "Febrero"
        elif valor == 3:
            mes = "Marzo"
        elif valor == 4:
            mes = "Abril"
        elif valor == 5:
            mes = "Mayo"
        elif valor == 6:
            mes = "Junio"
        elif valor == 7:
            mes = "Julio"
        elif valor == 8:
            mes = "Agosto"
        elif valor == 9:
            mes = "Septiembre"
        elif valor == 10:
            mes = "Octubre"
        elif valor == 11:
            mes = "Noviembre"
        elif valor == 12:
            mes = "Diciembre"
    except:
        messagebox.showerror(message="Dato incorrecto", title = "Error")
tk.Label(root,text="ingrese numero: ").place(x=10, y=20)
txtNumero=tk.Entry(root)
txtNumero.place(x=10,y=40)
btnVerMes=tk.Button(root, text="Ver Mes", command=Mes)
btnVerMes.place(x=10, y =70)
root.mainloop()