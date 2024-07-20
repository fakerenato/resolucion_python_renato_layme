def factorial(n):
    if n < 0:
        return "El número debe ser un entero no negativo."
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
numero = int(input("Ingrese un número entero no negativo: "))
print("El factorial de", numero, "es", factorial(numero))
