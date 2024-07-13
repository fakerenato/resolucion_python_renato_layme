lista_de_muestra=['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
posiciones=[0,4,5]
valores_eliminar = [lista_de_muestra[i] for i in posiciones]
for valor in valores_eliminar:
    lista_de_muestra.remove(valor)
print(lista_de_muestra)
