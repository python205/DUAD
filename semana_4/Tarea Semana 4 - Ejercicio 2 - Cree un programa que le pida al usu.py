#2 - Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

nombre = input (" Cual es su nombre? ")
apellido = input (" Cual es su apellido? ")
edad = int(input(" Cual es su edad? "))

if (edad <4):
    print(f"{nombre} {apellido} tiene {edad} entonces es un bebe")
elif (edad <12):
    print(f"{nombre} {apellido} tiene {edad} entonces es un niño/niña")
elif (edad <14):
    print(f"{nombre} {apellido} tiene {edad} entonces es un preadolescente")
elif (edad <18):
        print(f"{nombre} {apellido} tiene {edad} entonces es un adolescente")
elif (edad <30):
        print(f"{nombre} {apellido} tiene {edad} entonces es un adulto joven")
elif (edad <60):
        print(f"{nombre} {apellido} tiene {edad} entonces es un adulto")        
else:
    print(f"{nombre} {apellido} tiene {edad} entonces es un adulto mayor")