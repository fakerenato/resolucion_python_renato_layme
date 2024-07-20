numeros = []

pares = 0
impares = 0

while True:
    
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    
   
    if respuesta == 'SI':
        
        numero = int(input("Ingrese el número: "))
        
        numeros.append(numero)
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    elif respuesta == 'NO':

        break
    else:
        print("Respuesta no válida, por favor ingrese 'SI' o 'NO'.")


print("\nNúmeros ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
