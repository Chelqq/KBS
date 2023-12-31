# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 14:23:41 2023

@author: XeL
"""

import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora")

        self.display = tk.Entry(self.window, width=50, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.history_display = tk.Text(self.window, width=50, height=10, borderwidth=5)
        self.history_display.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
 
        self.buttons = []

        self.history = []

        self.create_buttons()

    def create_buttons(self):
        row, col = 2, 0
        button_values = [
            ('A', None), ('log10', 'log10'), ('%', 'percentage'), ('CE', 'clear_entry'), ('<--', 'backspace'),
            ('B', None), ('sqrt', 'sqrt'), ('pow', 'power'), ('n!', 'factorial'), ('/', '/'),
            ('C', None), ('9', '9'), ('8', '8'), ('7', '7'), ('*', '*'),
            ('D', None), ('6', '6'), ('5', '5'), ('4', '4'), ('-', '-'),
            ('E', None), ('3', '3'), ('2', '2'), ('1', '1'), ('+', '+'),
            ('F', None), ('abs', 'abs'), ('0', '0'), ('.', '.'), ('=', 'calculate')
        ]
        
        for value, operation in button_values:
            button = tk.Button(self.window, text=value, padx=20, pady=10,
                               command=lambda op=operation: self.button_click(op))
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def button_click(self, operation):
        current_text = self.display.get()

        if operation == 'clear_entry':
            self.display.delete(0, tk.END)

        elif operation == 'calculate':
            self.calculate()

        elif operation in ('sin', 'cos', 'tan', 'log10', 'sqrt'):
            self.trigonometric_function(operation)

        elif operation in ('bin', 'oct', 'hex', 'dec'):
            self.convert_to_base(operation)

        else:
            self.display.insert(tk.END, operation)
            
    def convert_to_base(self, base):
        self.history_display = tk.Text(self.window, width=50, height=10, borderwidth=5)
        self.history_display.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        try:
            decimal_value = int(self.display.get())
            converted_value = format(decimal_value, base)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(converted_value))

            self.history.append((f"Conversion to {base} ({decimal_value})", converted_value))
            self.display_bases()  # Call the method to update base conversions
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    
            
    def trigonometric_function(self, function):
        try:
            angle = float(self.display.get())
            if function == 'sin':
                result = math.sin(math.radians(angle))
            elif function == 'cos':
                result = math.cos(math.radians(angle))
            elif function == 'tan':
                result = math.tan(math.radians(angle))
            elif function == 'log10':
                result = math.log10(angle)
            elif function == 'sqrt':
                result = math.sqrt(angle)

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))

            self.history.append((f"{function}({angle})", result))
            self.display_bases()

        except Exception:
            messagebox.showerror("Error", "Invalid Input")

    def calculate(self):
        try:
            expression = self.display.get()
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.display_bases()

            self.history.append((expression, result))
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    
    def decimal_to_octal(decimal_num):
        if decimal_num == 0:
            return '0'  # Manejar caso especial de decimal 0
    
        octal_digits = []  # Almacenar los dígitos octales en una lista
    
        while decimal_num > 0:
            remainder = decimal_num % 8  # Obtener el residuo al dividir por 8
            octal_digits.append(str(remainder))  # Agregar el dígito a la lista
            decimal_num //= 8  # Actualizar el número decimal dividiéndolo por 8
    
        octal_digits.reverse()  # Revertir la lista para obtener la representación correcta
    
        octal_str = ''.join(octal_digits)  # Convertir la lista de dígitos en una cadena
    
        return octal_str

    def display_bases(self):
        decimal_value = int(self.display.get())
        base_labels = ['bin', 'oct', 'hex', 'dec']

        
        self.history_display.delete(1.0, tk.END)  # Clear history display
        
        for base in base_labels:
            converted_value = self.convert_to_base(decimal_value, base)
            self.history_display.insert(tk.END, f"Conversion to {base}: {converted_value}\n")

    def clear_buttons(self):
        for button in self.buttons:
            button.grid_forget()

        self.buttons = []

    def run(self):
        self.buttons = []
        self.window.mainloop()


calculator = Calculator()
calculator.run()
