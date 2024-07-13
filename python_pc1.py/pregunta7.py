numero1=float(input("Ingresar primer numero"))
numero2=float(input("Ingresar segundo numero"))
print("""
      Elegir entre las 3 opciones
1.Suma de 2 numeros
2.Resta de 2 numeros (primero mnenos segundo)  
3.Multiplicacion de los 2 numeros    
      """)
opcion_elegida=int(input("Ingrese su opcion elegida"))
if opcion_elegida== 1 :
        resultado=numero1 + numero2
        print(resultado)

elif opcion_elegida== 2 :
        resultado=numero1 - numero2
        print(resultado)
    
elif opcion_elegida== 3 :
        resultado=numero1 * numero2
        print(resultado)
else :
    print("Opcion invalida no es correcta")
    