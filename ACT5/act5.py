import sys
import heapq

class Nodo:
    def __init__(self, objetivo, regla=None):
        self.objetivo = objetivo
        self.regla = regla
        self.hijos = []

class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz

class Regla:
    def __init__(self, cabeza, cuerpo):
        self.cabeza = cabeza
        self.cuerpo = cuerpo

def construir_arbol(base_conocimientos, objetivo):
    raiz = Nodo(objetivo)
    arbol = Arbol(raiz)
    # Implementa el resto de la lógica aquí
    return arbol

def imprimir_arbol(nodo, nivel=0):
    if nodo is None:
        return
    print(" " * nivel + str(nodo.objetivo))
    for hijo in nodo.hijos:
        imprimir_arbol(hijo, nivel + 1)

base_conocimientos = [
    Regla("padre(juan,pedro)", ["juan", "pedro"]),
    Regla("padre(pedro,pepe)", ["pedro", "pepe"]),
]

objetivo = "padre(juan,pepe)"
arbol = construir_arbol(base_conocimientos, objetivo)
imprimir_arbol(arbol.raiz)
