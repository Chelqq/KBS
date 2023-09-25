# Función para calcular el factorial de un número
def calcular_factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos"
    elif numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

# Solicitar al usuario un número entero no negativo
try:
    numero = int(input("Ingrese un número entero no negativo: "))
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es {resultado}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
