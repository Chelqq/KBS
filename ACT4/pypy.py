class Persona:
    def __init__(self, nombre, genero, hijos=[]):
        self.nombre = nombre
        self.genero = genero
        self.hijos = hijos

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self):
        return self.nombre

# Crear personas
abuelo_paterno = Persona("Abuelo Paterno", "Hombre")
abuela_paterna = Persona("Abuela Paterna", "Mujer")
padre = Persona("Padre", "Hombre")
madre = Persona("Madre", "Mujer")
hijo1 = Persona("Hijo1", "Hombre")
hijo2 = Persona("Hijo2", "Mujer")

# Establecer relaciones familiares
abuelo_paterno.agregar_hijo(padre)
abuela_paterna.agregar_hijo(padre)
padre.agregar_hijo(hijo1)
padre.agregar_hijo(hijo2)
madre.agregar_hijo(hijo1)
madre.agregar_hijo(hijo2)

# Función para imprimir el árbol de inferencia
def imprimir_arbol(persona, nivel=0):
    indentacion = "  " * nivel
    print(indentacion + f"{persona.nombre} ({persona.genero})")
    for hijo in persona.hijos:
        imprimir_arbol(hijo, nivel + 1)

# Imprimir el árbol de inferencia
print("Árbol de Inferencia Familiar:")
imprimir_arbol(abuelo_paterno)
