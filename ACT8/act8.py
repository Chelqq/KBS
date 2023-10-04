def pot(base, exp):
    # Caso base: Cualquier número elevado a la potencia 0 es 1.
    if exp == 0:
        return 1
    # Caso recursivo: Si el exponente es positivo.
    elif exp > 0:
        return base * pot(base, exp - 1)
    # Caso recursivo: Si el exponente es negativo.
    else:
        return 1 / (base * pot(base, -exp - 1))

# Solicitar al usuario la base y el exponente
base = float(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))

# Calcular la pot y mostrar el resultado
resultado = pot(base, exp)
print(f"{base} elevado a la {exp} es igual a {resultado}")
