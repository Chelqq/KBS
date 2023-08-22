# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:07:31 2023

@author: compa
"""

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
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'log',
            'sqrt', 'clear',
            'bin', 'oct', 'hex'
        ]
        
        for value in button_values:
            button = tk.Button(self.window, text=value, padx=20, pady=10,
                               command=lambda val=value: self.button_click(val))
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, value):
        current_text = self.display.get()

        if value == 'clear':
            self.display.delete(0, tk.END)

        elif value == '=':
            self.calculate()

        elif value in ('sin', 'cos', 'tan', 'log', 'sqrt'):
            self.trigonometric_function(value)

        elif value in ('bin', 'oct', 'hex'):
            self.convert_to_base(value)

        else:
            self.display.insert(tk.END, value)
            
    def convert_to_base(self, base):
        try:
            decimal_value = int(self.display.get())
            converted_value = format(decimal_value, base)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(converted_value))

            self.history.append((f"Conversion to {base} ({decimal_value})", converted_value))
            self.update_history_display()

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
            elif function == 'log':
                result = math.log10(angle)
            elif function == 'sqrt':
                result = math.sqrt(angle)

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))

            self.history.append((f"{function}({angle})", result))
            self.update_history_display()

        except Exception:
            messagebox.showerror("Error", "Invalid Input")

    def calculate(self):
        try:
            expression = self.display.get()
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))

            self.history.append((expression, result))
            self.update_history_display()

        except Exception:
            messagebox.showerror("Error", "Invalid Input")

    def update_history_display(self):
        self.history_display.delete(1.0, tk.END)
        for entry in self.history:
            self.history_display.insert(tk.END, f"{entry[0]} = {entry[1]}\n")

    def clear_buttons(self):
        for button in self.buttons:
            button.grid_forget()

        self.buttons = []

    def run(self):
        self.buttons = []
        self.window.mainloop()


calculator = Calculator()
calculator.run()
