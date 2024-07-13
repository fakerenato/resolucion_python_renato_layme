from datetime import datetime

# Solicitar al usuario que ingrese una hora
hora_str = input("Ingrese la hora en formato de 24 horas (ejemplo: 7:30 o 18:45): ")

# Convertir la entrada a un objeto datetime
hora = datetime.strptime(hora_str, "%H:%M").time()

# Definir los rangos de tiempo para las comidas
hora_desayuno_inicio = datetime.strptime("7:00", "%H:%M").time()
hora_desayuno_fin = datetime.strptime("8:00", "%H:%M").time()

hora_almuerzo_inicio = datetime.strptime("12:00", "%H:%M").time()
hora_almuerzo_fin = datetime.strptime("13:00", "%H:%M").time()

hora_cena_inicio = datetime.strptime("18:00", "%H:%M").time()
hora_cena_fin = datetime.strptime("19:00", "%H:%M").time()

# Verificar si es la hora de alguna comida
if hora_desayuno_inicio <= hora <= hora_desayuno_fin:
    print("Es hora del desayuno")
elif hora_almuerzo_inicio <= hora <= hora_almuerzo_fin:
    print("Es hora del almuerzo")
elif hora_cena_inicio <= hora <= hora_cena_fin:
    print("Es hora de la cena")

