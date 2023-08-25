# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:56:08 2023

@author: Chris J
"""

import tkinter as tk
from tkinter import messagebox
mes = ""
def Mes():
    numero = int(entrada.get())
    try:
        if numero == 1:
            mes = "Enero"
        elif numero == 2:
            mes = "Febrero"
        elif numero == 3:
            mes = "Marzo"
        elif numero == 4:
            mes = "Abril"
        elif numero == 5:
            mes = "Mayo"
        elif numero == 6:
            mes = "Junio"
        elif numero == 7:
            mes = "Julio"
        elif numero == 8:
            mes = "Agosto"
        elif numero == 9:
            mes = "Septiembre"
        elif numero == 10:
            mes = "Octubre"
        elif numero == 11:
            mes = "Noviembre"
        elif numero == 12:
            mes = "Diciembre"
    except:
        messagebox.showerror(message="Dato incorrecto", title = "Error")
    
    messagebox.showinfo("Resultado", mes)

#ventana
root = tk.Tk()
root.title("Practica_2")

#Msg e input
etiqueta = tk.Label(root, text="Introduce un número del 1 al 12:")
etiqueta.pack()

entrada = tk.Entry(root)
entrada.pack()

# Button para resultado
boton = tk.Button(root, text="Obtener Mes", command=Mes)
boton.pack()

#mainloop
root.mainloop()
