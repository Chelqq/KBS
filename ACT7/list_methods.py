
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
"""# Definir una lista vacía
mi_lista = []

# Función para insertar elementos en la lista
mi_lista = []

# Función para insertar elementos enteros en la lista
def insertar_en_lista():
    try:
        elemento = int(input("Ingrese el elemento entero que desea insertar: "))
        mi_lista.append(elemento)
        print("Elemento insertado en la lista.")
    except ValueError:
        print("Error: Debe ingresar un valor entero.")

# Función para buscar un elemento en la lista
def buscar_en_lista():
    elemento = int(input("Ingrese el elemento que desea buscar: "))
    if elemento in mi_lista:
        print(f"{elemento} está en la lista.")
    else:
        print(f"{elemento} no está en la lista.")

# Función para editar un elemento en la lista
def editar_lista():
    indice = int(input("Ingrese el índice del elemento que desea editar: "))
    if 0 <= indice < len(mi_lista):
        nuevo_valor = input("Ingrese el nuevo valor: ")
        mi_lista[indice] = nuevo_valor
        print("Elemento editado correctamente.")
    else:
        print("Índice fuera de rango.")

# Función para eliminar el primer y último elemento de la lista
def eliminar_inicio():
    if len(mi_lista) > 0:
        primer_elemento = mi_lista.pop(0)
        print(f"Elemento eliminado al inicio: {primer_elemento}")
    else:
        print("La lista está vacía.")

def eliminar_final():
    if len(mi_lista) > 0:
        ultimo_elemento = mi_lista.pop()
        print(f"Elemento eliminado al final: {ultimo_elemento}")
    else:
        print("La lista está vacía.")

# Función para buscar números repetidos en la lista
def buscar_numeros_repetidos():
    numeros_repetidos = []
    for elemento in mi_lista:
        if mi_lista.count(elemento) > 1 and elemento not in numeros_repetidos:
            numeros_repetidos.append(elemento)
    if numeros_repetidos:
        print("Números repetidos en la lista:", numeros_repetidos)
    else:
        print("No hay números repetidos en la lista.")

# Función para ordenar la lista en orden ascendente
def ordenar_ascendente():
    listaint = [int(elemento) for elemento in mi_lista]
    listaint.sort()
    listastr = [str(elem) for elem in listaint]
    mi_lista = listastr
    print("Lista ordenada en orden ascendente:", listastr)

# Función para ordenar la lista en orden descendente
def ordenar_descendente():
    listaint = [int(elemento) for elemento in mi_lista]
    listaint.sort(reverse=True)
    listastr = [str(elem) for elem in listaint]
    mi_lista = listastr
    print("Lista ordenada en orden descendente:", listastr)

# Función para mostrar el primer elemento de la lista (cabeza)
def mostrar_cabeza():
    if len(mi_lista) > 0:
        print("Primer elemento de la lista:", mi_lista[0])
    else:
        print("La lista está vacía.")

# Función para mostrar el último elemento de la lista
def mostrar_final():
    if len(mi_lista) > 0:
        print("Último elemento de la lista:", mi_lista[-1])
    else:
        print("La lista está vacía.")

# Bucle principal
while True:
    print("\nOperaciones disponibles:")
    print("1- Insertar en Lista")
    print("2- Buscar en Lista")
    print("3- Editar Lista")
    print("4- Eliminar al inicio")
    print("5- Eliminar al Final")
    print("6- Buscar números repetidos")
    print("7- Ordenar Ascendente")
    print("8- Ordenar Descendente")
    print("9- Mostrar Cabeza")
    print("10- Mostrar Final")
    print("11- Salir")

    opcion = input("Seleccione una operación (1-10): ")

    if opcion == "1":
        insertar_en_lista()
    elif opcion == "2":
        buscar_en_lista()
    elif opcion == "3":
        editar_lista()
    elif opcion == "4":
        eliminar_inicio()
    elif opcion == "6":
        buscar_numeros_repetidos()
    elif opcion == "7":
        ordenar_ascendente()
    elif opcion == "8":
        ordenar_descendente()
    elif opcion == "9":
        mostrar_cabeza()
    elif opcion == "10":
        mostrar_final()
    elif opcion == "5":
        eliminar_final()
    elif opcion == "11":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
