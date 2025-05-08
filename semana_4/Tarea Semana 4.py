#1-Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

#string + string
name2 = "Iron Man"
value = 3
name1 = "Tony" + " Stark " 
print(name1)

#string + int
movie = "Iron Man"
value = 3
print(f"{movie}{ value }")

#int + string
sport = "Medal"
value2 = 1
print(f"{value2} {sport }")

#list + list
my_list1 = ["Spiderman", "Hulk", "Thor"]
my_list2 = ["Deadpool", "Wolverine"] 
print(f"{my_list1[2]} vs {my_list2[1]}")

#string + list
print(f"{name2} and {my_list1[0]}")

#float + int
value3 = 3.3 + 2
print(value3)

#bool + bool
my_statement1 = True
my_statement2 = False
print(my_statement1 + my_statement2)

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

