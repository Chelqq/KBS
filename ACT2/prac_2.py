import tkinter as tk
from tkinter import messagebox

def get_month():
    try:
        numero = int(entrada.get())
        meses = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre"
        }
        
        if numero < 1 or numero > 12:
            messagebox.showerror(message="Número incorrecto", title="Error")
        else:
            mes = meses[numero]
            messagebox.showinfo("Resultado", mes)
    except ValueError:
        messagebox.showerror(message="Dato incorrecto", title="Error")

# Ventana
root = tk.Tk()
root.title("Practica_2")

# Etiqueta e input
etiqueta = tk.Label(root, text="Introduce un número del 1 al 12:")
etiqueta.pack()

entrada = tk.Entry(root)
entrada.pack()

# Botón para obtener el mes
boton = tk.Button(root, text="Obtener Mes", command=get_month)
boton.pack()

# Mainloop
root.mainloop()
