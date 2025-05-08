#3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

import random
numero_secreto = random.randint(1, 10)

print("¡Bienvenido, adivina el número secreto (entre 1 y 10):")

while True:
        adivina = int(input("Tu respuesta: "))
        
        if adivina == numero_secreto:
            print("¡Felicidades! Adivinaste el número secreto.")
            break 
        elif adivina < numero_secreto:
            print("El número secreto es mayor. Inténtalo de nuevo.")
        else:
            print("El número secreto es menor. Inténtalo de nuevo.")
    
