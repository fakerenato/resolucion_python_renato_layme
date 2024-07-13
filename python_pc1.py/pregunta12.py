def obtener_tipo_mime(nombre_archivo):
    
    tipos_mime = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    
    nombre_archivo = nombre_archivo.lower()

    
    extension = None
    if "." in nombre_archivo:
        extension = "." + nombre_archivo.split(".")[-1]

    
    return tipos_mime.get(extension, "application/octet-stream")


nombre_archivo = input("Ingrese el nombre del archivo: ")


tipo_mime = obtener_tipo_mime(nombre_archivo)
print(f"El tipo MIME del archivo es: {tipo_mime}")
