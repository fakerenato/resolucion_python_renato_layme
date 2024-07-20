def omitir_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = ''.join([letra for letra in texto if letra not in vocales])
    return resultado

entrada = input("Ingrese una cadena de texto: ")
salida = omitir_vocales(entrada)
print("Texto sin vocales:", salida)
