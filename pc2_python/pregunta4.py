alumnos = []
n = int(input("Ingrese la cantidad de alumnos: "))

for _ in range(n):
    alumno = {}
    alumno['Alumno'] = input("Nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la calificación {i+1} del alumno: "))
        notas.append(nota)
    alumno['Notas'] = notas
    alumnos.append(alumno)

print("\nListado de alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

