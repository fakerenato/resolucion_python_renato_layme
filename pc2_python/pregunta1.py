
inicio = 1500
fin = 2700

numero = inicio

numeros_divisibles = []


while numero <= fin:
    
    if numero % 7 == 0 and numero % 5 == 0:
        numeros_divisibles.append(numero)
    
    numero += 1

print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:")
print(numeros_divisibles)

