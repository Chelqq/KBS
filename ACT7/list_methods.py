
"""Actividad 7. Listas
Escribe las premisas y clausulas necesarias que permitan trabajar con una lista,
así mismo que realice los siguientes procesos, tanto en python como prolog .
Menú
1- Insertar en Lista
2- Buscar en Lista
3- Editar Lista
4- Eliminar al inicio y Final.
5- Buscar números repetidos
6- Ordenar Ascendente
7- Ordenar Descendente
8- Mostar Cabeza
9- Mostrar Final
10-Salir
"""
from os import system
import time
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.final = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def editar(self, valor_viejo, valor_nuevo):
        actual = self.cabeza
        while actual:
            if actual.valor == valor_viejo:
                actual.valor = valor_nuevo
                return True
            actual = actual.siguiente
        return False

    def eliminar_inicio(self):
        if not self.cabeza:
            return False
        if self.cabeza == self.final:
            self.cabeza = None
            self.final = None
        else:
            self.cabeza = self.cabeza.siguiente
        return True

    def eliminar_final(self):
        if not self.final:
            return False
        if self.cabeza == self.final:
            self.cabeza = None
            self.final = None
        else:
            actual = self.cabeza
            while actual.siguiente != self.final:
                actual = actual.siguiente
            actual.siguiente = None
            self.final = actual
        return True

    def buscar_repetidos(self):
        valores = set()
        repetidos = set()
        actual = self.cabeza
        while actual:
            if actual.valor in valores:
                repetidos.add(actual.valor)
            else:
                valores.add(actual.valor)
            actual = actual.siguiente
        return list(repetidos)

    def ordenar_ascendente(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
        valores.sort()
        return valores

    def ordenar_descendente(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
        valores.sort(reverse=True)
        return valores

    def mostrar_cabeza(self):
        if self.cabeza:
            return self.cabeza.valor
        else:
            return None

    def mostrar_final(self):
        if self.final:
            return self.final.valor
        else:
            return None

if __name__ == "__main__":
    lista = ListaEnlazada()

    while True:
        time.sleep(2.5)   
        system("cls")
        print("\nMenú:")
        print("1- Insertar en Lista")
        print("2- Buscar en Lista")
        print("3- Editar Lista")
        print("4- Eliminar al inicio")
        print("5- Eliminar al final")
        print("6- Buscar números repetidos")
        print("7- Ordenar Ascendente")
        print("8- Ordenar Descendente")
        print("9- Mostrar Cabeza")
        print("10- Mostrar Final")
        print("11- Salir")

        texto=input("Selecciona una opción: ")
        try:
            opcion = int(texto)
            if opcion>=0:
                opcion = int(texto)
            else:
                print("ingresó un número negativo")
        except ValueError:
            print("No ingresó un entero")

        
        if opcion == 1:
            texto=input("Numero a insertar ")
            try:
                valor = int(texto)
                if valor>=0:
                    valor = int(texto)
                else:
                    print("ingresó un número negativo")
            except ValueError:
                print("No ingresó un entero")
            lista.insertar(valor)
            print("Valor insertado en la lista.")

        elif opcion == 2:
            valor = int(input("Ingrese el valor a buscar: "))
            if lista.buscar(valor):
                print("El valor está en la lista.")
            else:
                print("El valor no está en la lista.")

        elif opcion == 3:
            valor_viejo = int(input("Ingrese el valor a editar: "))
            valor_nuevo = int(input("Ingrese el nuevo valor: "))
            if lista.editar(valor_viejo, valor_nuevo):
                print("Valor editado en la lista.")
            else:
                print("El valor a editar no se encontró en la lista.")

        elif opcion == 4:
            if lista.eliminar_inicio():
                print("Valor eliminado al inicio de la lista.")
            else:
                print("La lista está vacía.")

        elif opcion == 5:
            if lista.eliminar_final():
                print("Valor eliminado al final de la lista.")
            else:
                print("La lista está vacía.")

        elif opcion == 6:
            repetidos = lista.buscar_repetidos()
            if repetidos:
                print("Números repetidos en la lista:", repetidos)
            else:
                print("No hay números repetidos en la lista.")

        elif opcion == 7:
            ascendente = lista.ordenar_ascendente()
            print("Lista ordenada en orden ascendente:", ascendente)

        elif opcion == 8:
            descendente = lista.ordenar_descendente()
            print("Lista ordenada en orden descendente:", descendente)

        elif opcion == 9:
            cabeza = lista.mostrar_cabeza()
            if cabeza is not None:
                print("Cabeza de la lista:", cabeza)
            else:
                print("La lista está vacía.")

        elif opcion == 10:
            final = lista.mostrar_final()
            if final is not None:
                print("Final de la lista:", final)
            else:
                print("La lista está vacía.")

        elif opcion == 11:
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")