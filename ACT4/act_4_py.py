from kanren import run, eq, lall, var

# Definir las relaciones
hombre = ('Jose', 'Luis', 'Luisito', 'Luis angel', 'Carlos')
mujer = ('Maria', 'Karla', 'Luisita', 'Elvira')

# Crear variables lógicas
X = var()
Y = var()

padre_madre = lall(eq, ('Jose', 'Luis'), ('Maria', 'Luis'), ('Jose', 'Karla'), ('Maria', 'Karla'),
                   ('Luis', 'Luisito'), ('Luis', 'Luisita'), ('Luis', 'Luis angel'), ('Karla', 'Carlos'), ('Karla', 'Juan'),
                   ('Luisito', 'Andres'), ('Luisito', 'Tomas'), ('Luisita', 'Elvira'), ('Luis angel', 'Angel'),
                   ('Luis angel', 'Angelito'), ('Carlos', 'Carlitos'))

# Realizar una consulta
result = run(1, ('X',), lall(eq, ('Jose', 'X')), padre_madre)

# Imprimir el resultado
print(result)
