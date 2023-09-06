# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 14:23:41 2023

@author: XeL
"""
from tkinter import*
from tkinter import ttk
import math 
import sympy as sy

def IngresaValor(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
    elif tecla.isalpha() or tecla in 'ABCDEF.':
        entrada2.set(entrada2.get() + tecla)
    elif tecla == '(':
        if entrada2.get()[-1] in '0123456789':
            entrada2.set(entrada2.get() + '*(')
            contador_parentesis[0]+=1
        elif entrada2.get()[-1] in '/':
            entrada2.set(entrada2.get()+ '/(')
            contador_parentesis[0]+=1
        else:
            entrada2.set(entrada2.get() + tecla)
            contador_parentesis[0]+=1
    elif tecla == ')':
        if contador_parentesis[0]>0:
            entrada2.set(entrada2.get() + tecla)
            contador_parentesis[0]-=1
        else:
            entrada2.set("ERROR: paréntesis sin coincidencia")
    elif tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if entrada2.get()[-1] in '0123456789':
            entrada2.set(entrada2.get() + tecla)
        elif entrada2.get()[-1]==')':
            entrada2.set(entrada2.get() + tecla)
        elif entrada2.get()[-1] in '+-*/':
            entrada2.set(entrada2.get()[:-1]+ tecla)
    elif tecla == '=':
        expresion = entrada2.get()
        try:
            convertir_hexadecimal()
            binario()
            octal()
            hexadecimal()
            resultado = sy.sympify(expresion)
            entrada2.set(resultado)

        except Exception as e:
            entrada2.set("ERROR")

def convertir_hexadecimal():
    try:
        dec = int(entrada2.get(), 16)  # Convertir a decimal
        entrada2.set(dec)
    except ValueError:
        return "Error: Entrada no válida"


def binario():
    numBin=[]
    aux=float(entrada2.get())
    while aux !=0:
        numBin.append(int(aux%2))
        aux//=2
    numBin.reverse()
    Binario.set('Bin '+''.join(map(str,numBin)))

def octal():
    numOct=[]
    aux=float(entrada2.get())
    while aux !=0:
        numOct.append(int(aux%8))
        aux//=8
    numOct.reverse()
    Octal.set('Oct '+''.join(map(str,numOct)))

def caracter_hex(aux):
    if aux== 10:
        return 'A'
    elif aux==11:
        return 'B'
    elif aux==12:
        return 'C'
    elif aux==13:
        return 'D'
    elif aux==14:
        return 'E'
    elif aux==15:
        return 'F'
    else: 
        return str(aux)
    
def hexadecimal():
    numHex=[]
    aux=float(entrada2.get())
    while aux !=0:
        numHex.append(int(aux%16))
        aux//=16
    if len(numHex)==0:
        numHex.append(0)
    
    numHex.reverse()
    hex_string=''.join([caracter_hex(x) for x in numHex])
    Hexadecimal.set('Hex '+hex_string)


def RaizCu():
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)


def borrar():
    entrada2.set(entrada2.get()[:-1])


def borrarTodo():
    entrada2.set('')
    Binario.set('')
    Octal.set('')
    Hexadecimal.set('')

def log10():
    try:
        entrada = float(entrada2.get())
        if entrada <= 0:
            entrada2.set("ERROR: El argumento debe ser mayor que 0")
        else:
            resultado = math.log10(entrada)
            entrada2.set(resultado)
    except ValueError:
        entrada2.set("ERROR: Entrada no válida")

def factorial():
    aux=float(entrada2.get())
    if aux < 0:
        entrada2.set("ERROR")
    elif aux ==0:
       entrada2.set(1)
    else:
        fac=1
        while (aux > 1):
            fac*=aux
            aux-=1
        entrada2.set(fac)

ventana =Tk()
ventana.title("Calculadora")
ventana.geometry("+500+80")
color_rgb=(128 , 128, 255)
color_Hex="#{:02X}{:02X}{:02X}".format(*color_rgb)
#Estilos

estilo_label1=ttk.Style()
estilo_label1.configure('Label1.TLabel', font="arial 20", anchor="e", background=color_Hex)
estilo_label2=ttk.Style()
estilo_label2.configure('Label2.TLabel', font="arial 15", anchor="w", background=color_Hex)

mainframe =ttk.Frame()
mainframe.grid(row=0, column=0)

contador_parentesis=[0]

entrada2=StringVar()
label_entrada2=ttk.Label(mainframe, textvariable=entrada2, style="Label1.TLabel")
label_entrada2.grid(row=0, column=0, columnspan=5, sticky='we')

Binario=StringVar()
label_Binario=ttk.Label(mainframe, textvariable=Binario, style="Label2.TLabel")
label_Binario.grid(row=1, column=0, columnspan=5, sticky="we")

Octal=StringVar()
label_Octal=ttk.Label(mainframe, textvariable=Octal, style="Label2.TLabel")
label_Octal.grid(row=2, column=0, columnspan=5, sticky='we')

Hexadecimal=StringVar()
label_Hexadecimal=ttk.Label(mainframe, textvariable=Hexadecimal, style="Label2.TLabel")
label_Hexadecimal.grid(row=3, column=0, columnspan=5, sticky='we')

#Botones
btn1=ttk.Button(mainframe, text="1",command=lambda:IngresaValor('1'))
btn2=ttk.Button(mainframe, text="2",command=lambda:IngresaValor('2'))
btn3=ttk.Button(mainframe, text="3",command=lambda:IngresaValor('3'))
btn4=ttk.Button(mainframe, text="4",command=lambda:IngresaValor('4'))
btn5=ttk.Button(mainframe, text="5",command=lambda:IngresaValor('5'))
btn6=ttk.Button(mainframe, text="6",command=lambda:IngresaValor('6'))
btn7=ttk.Button(mainframe, text="7",command=lambda:IngresaValor('7'))
btn8=ttk.Button(mainframe, text="8",command=lambda:IngresaValor('8'))
btn9=ttk.Button(mainframe, text="9",command=lambda:IngresaValor('9'))
btn0=ttk.Button(mainframe, text="0",command=lambda:IngresaValor('0'))

btnA=ttk.Button(mainframe, text="A",command=lambda:IngresaValor('A'))
btnB=ttk.Button(mainframe, text="B",command=lambda:IngresaValor('B'))
btnC=ttk.Button(mainframe, text="C",command=lambda:IngresaValor('C'))
btnD=ttk.Button(mainframe, text="D",command=lambda:IngresaValor('D'))
btnE=ttk.Button(mainframe, text="E",command=lambda:IngresaValor('E'))
btnF=ttk.Button(mainframe, text="F",command=lambda:IngresaValor('F'))

btnPa1=ttk.Button(mainframe,text="(",command=lambda:IngresaValor('('))
btnPa2=ttk.Button(mainframe,text=")",command=lambda:IngresaValor(')'))
btnBorrar=ttk.Button(mainframe,text=chr(9003),command=lambda:borrar())
btnBorrarTodo=ttk.Button(mainframe,text="CE", command=lambda:borrarTodo())
btnPunto=ttk.Button(mainframe,text=".",command=lambda:IngresaValor('.'))
btnPorcentaje=ttk.Button(mainframe,text="%")
btnFactorial=ttk.Button(mainframe, text="n!",command=lambda:factorial())

btnSuma=ttk.Button(mainframe,text="+",command=lambda:IngresaValor('+'))
btnResta=ttk.Button(mainframe,text="-",command=lambda:IngresaValor('-'))
btnMultiplicacion=ttk.Button(mainframe,text="x",command=lambda:IngresaValor('*'))
btnDivicion=ttk.Button(mainframe,text=chr(247),command=lambda:IngresaValor('/'))
btnRaizC=ttk.Button(mainframe,text="√",command=lambda:RaizCu())
btnIgual=ttk.Button(mainframe,text="=",command=lambda:IngresaValor('='))
btnLog10=ttk.Button(mainframe,text="Log10",command=lambda:log10())
btnABS=ttk.Button(mainframe,text="ABS")

#Pocisionar botones
btnFactorial.grid(row=11,column=2)
btnA.grid(row=11,column=0)
btnLog10.grid(row=11,column=1)
btnBorrarTodo.grid(row=11,column=3)
btnBorrar.grid(row=11,column=4)
btnB.grid(row=12,column=0)
btnPa1.grid(row=12,column=1)
btnPa2.grid(row=12,column=2)
btnRaizC.grid(row=12,column=3)
btnDivicion.grid(row=12,column=4)
btnC.grid(row=13,column=0)
btn7.grid(row=13,column=1)
btn8.grid(row=13,column=2)
btn9.grid(row=13,column=3)
btnMultiplicacion.grid(row=13,column=4)
btnD.grid(row=14,column=0)
btn4.grid(row=14,column=1)
btn5.grid(row=14,column=2)
btn6.grid(row=14,column=3)
btnResta.grid(row=14,column=4)
btnE.grid(row=15,column=0)
btn1.grid(row=15,column=1)
btn2.grid(row=15,column=2)
btn3.grid(row=15,column=3)
btnSuma.grid(row=15,column=4)
btnF.grid(row=16,column=0)
btnABS.grid(row=16,column=1)
btn0.grid(row=16,column=2)
btnPunto.grid(row=16,column=3)
btnIgual.grid(row=16,column=4)

ventana.mainloop()