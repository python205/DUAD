print("Ingrese tres numeros.")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if numero1 >= numero2 and numero3:
    mayor = numero1
elif numero2 >= numero1 and numero3:
    mayor = numero2
else:
    mayor = numero3    

    

print(f"El mayor de los tres numeros es: {mayor}")