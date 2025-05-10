

n = int (input("Ingrese las notas:"))

notas_aprobadas = 0
notas_desaprobadas = 0
suma_total = 0
sumas_aprobadas = 0
sumas_desaprobadas = 0

counter = 0

while counter < n:
    nota = int(input("Ingresa tu nota"))
    suma_total+= nota

    if nota > 70:
        notas_aprobadas +=1
        sumas_aprobadas +=nota
    else:
        notas_desaprobadas +=1
        sumas_desaprobadas +=nota

    counter +=1

if n > 0:
    promedio_total = suma_total/n
else:
    promedio_total = 0

if notas_aprobadas > 0:
    promedio_aprobadas = sumas_aprobadas / notas_aprobadas
else:
    promedio_aprobadas = 0

if notas_desaprobadas > 0:
    promedio_desaprobadas = sumas_desaprobadas / notas_desaprobadas
else:
    promedio_desaprobadas = 0

print(f"Notas Aprobadas:{notas_aprobadas}")
print(f"Notas desaprobadas:{notas_desaprobadas}")  
print(f"Este es el promedio total{promedio_total}") 
print(f"Promedio de notas aprobadas{promedio_aprobadas}") 
print(f"Promedio de notas desaprobadas{promedio_desaprobadas}")


                    


    

