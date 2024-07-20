def convertir_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    # Verificar si la fecha está en formato MM/DD/AAAA
    if '/' in fecha:
        partes = fecha.split('/')
        mes = partes[0].zfill(2)
        dia = partes[1].zfill(2)
        anio = partes[2]
    else:
        # Fecha en formato "Mes D, AAAA"
        partes = fecha.split()
        mes = str(meses.index(partes[0]) + 1).zfill(2)
        dia = partes[1].strip(',').zfill(2)
        anio = partes[2]
    
    return f"{anio}-{mes}-{dia}"

# Solicitar la fecha al usuario
entrada = input("Ingrese una fecha (MM/DD/AAAA o Mes D, AAAA): ")
salida = convertir_fecha(entrada)
print("Fecha en formato AAAA-MM-DD:", salida)

