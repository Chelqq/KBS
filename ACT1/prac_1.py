import tkinter as tk
from tkinter import messagebox, END

root = tk.Tk()
root.config(width=200, height=300)
root.title("Practica 1 :)")

def Mensaje():
    nombre = txtNombre.get()
    messagebox.showinfo(message="Hola " + str(nombre),title="Mensaje")
tk.Label(root, text="Ingrese nombre").place(x=30, y=10)
txtNombre = tk.Entry()
txtNombre.place(x=30,y=50)
btnVer = tk.Button(root,text="Ver", command=Mensaje)
btnVer.place(x=50,y=80)

root.mainloop()