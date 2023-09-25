def fibonacci(n):
    # Inicializamos los primeros dos términos de la serie
    a, b = 0, 1
    serie = []

    # Generamos la serie hasta el término n
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b

    return serie

# Preguntamos al usuario el término hasta el cual quiere generar la serie
n = int(input("Ingrese el número de términos de la serie de Fibonacci que desea generar: "))

if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    resultado = fibonacci(n)
    print("Serie de Fibonacci hasta el término", n, ":")
    print(resultado)