import requests
import zipfile
import os

# Paso 1: Descargar la imagen desde el URL
def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        print(f"Imagen descargada y guardada como {nombre_archivo}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")

# Paso 2: Crear un archivo ZIP que contenga la imagen
def crear_zip(nombre_archivo, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(nombre_archivo)
        print(f"Archivo ZIP creado: {nombre_zip}")
    except Exception as e:
        print(f"Error al crear el archivo ZIP: {e}")

# Paso 3: Extraer el archivo ZIP
def extraer_zip(nombre_zip, carpeta_destino):
    try:
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall(carpeta_destino)
        print(f"Archivo ZIP extraído en la carpeta: {carpeta_destino}")
    except Exception as e:
        print(f"Error al extraer el archivo ZIP: {e}")

# URL de la imagen
url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Nombres de los archivos
nombre_imagen = "imagen_descargada.jpg"
nombre_zip = "imagen_comprimida.zip"
carpeta_extraccion = "imagen_extraida"

# Descargar la imagen
descargar_imagen(url_imagen, nombre_imagen)

# Crear un archivo ZIP que contenga la imagen
crear_zip(nombre_imagen, nombre_zip)

# Extraer el archivo ZIP
extraer_zip(nombre_zip, carpeta_extraccion)
