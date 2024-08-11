# Datos proporcionados
datos_temperaturas = """2024-01-01,15.5
2024-01-02,17.0
2024-01-03,16.2
2024-01-04,14.8
2024-01-05,18.1
2024-01-06,13.9
2024-01-07,19.3
2024-01-08,20.1
2024-01-09,21.4
2024-01-10,22.0"""

# Paso 1: Procesar los datos
def procesar_temperaturas(datos):
    temperaturas = []
    
    lineas = datos.strip().split('\n')
    for linea in lineas:
        fecha, temp = linea.strip().split(',')
        temperaturas.append(float(temp))
    
    temperatura_max = max(temperaturas)
    temperatura_min = min(temperaturas)
    temperatura_promedio = sum(temperaturas) / len(temperaturas)
    
    return temperatura_promedio, temperatura_max, temperatura_min

# Paso 2: Escribir los resultados en un nuevo archivo
def escribir_resumen(nombre_resumen, promedio, maxima, minima):
    with open(nombre_resumen, 'w') as file:
        file.write(f"Temperatura Promedio: {promedio:.2f}°C\n")
        file.write(f"Temperatura Máxima: {maxima:.2f}°C\n")
        file.write(f"Temperatura Mínima: {minima:.2f}°C\n")
    print(f"Resumen guardado en {nombre_resumen}")

# Ejecución del código
if __name__ == "__main__":
    promedio, maxima, minima = procesar_temperaturas(datos_temperaturas)
    
    escribir_resumen("resumen_temperaturas.txt", promedio, maxima, minima)
