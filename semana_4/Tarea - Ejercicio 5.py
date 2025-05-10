#5 - Dada n cantidad de notas de un estudiante, calcular
#Cuantas notas tiene aprobadas (mayor a 70).
#Cuantas notas tiene desaprobadas (menor a 70).
#El promedio de todas.
#El promedio de las aprobadas.
#El promedio de las desaprobadas.

n = int(input("Ingrese la cantidad de notas: "))

notas_aprobadas = 0
notas_desaprobadas = 0
suma_total = 0
suma_aprobadas = 0
suma_desaprobadas = 0

contador = 0

while contador < n:
    nota = int(input("Ingrese una nota: "))
    suma_total += nota

    if nota > 70:
        notas_aprobadas += 1
        suma_aprobadas += nota
    else:
        notas_desaprobadas += 1
        suma_desaprobadas += nota

    contador += 1 

if n > 0:
    promedio_total = suma_total / n
else:
    promedio_total = 0

if notas_aprobadas > 0:
    promedio_aprobadas = suma_aprobadas / notas_aprobadas
else:
    promedio_aprobadas = 0

if notas_desaprobadas > 0:
    promedio_desaprobadas = suma_desaprobadas / notas_desaprobadas
else:
    promedio_desaprobadas = 0

print(f"Notas aprobadas: {notas_aprobadas}")
print(f"Notas desaprobadas: {notas_desaprobadas}")
print(f"Este es el promedio total: {promedio_total}")
print(f"Promedio de notas aprobadas: {promedio_aprobadas}")
print(f"Promedio de notas desaprobadas: {promedio_desaprobadas}")
