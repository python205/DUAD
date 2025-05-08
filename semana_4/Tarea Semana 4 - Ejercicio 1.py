#1-Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

#string + string
name1 = "Iron + Man"
print(name1)

#string + int
#movie = "Iron Man" + 3
#print(movie)
#Eso integer y string no se pueden concatenar 
#TypeError: can only concatenate str (not "int") to str

movie = ("Iron Man")
value1 = str("3")
print(f"{movie} {value1}")

#int + string
#value2 = 1
#item = "Medal"
#print(value2 + item)
#Genera error TypeError: unsupported operand type(s) for +: 'int' and 'str'

value2 = str("1")
item = "Medal"
print (f"{value2} {item}")

#list + list
my_list1 = ["Spiderman", "Hulk", "Thor"]
my_list2 = ["Deadpool", "Wolverine"] 
print(my_list1 + my_list2)

#string + list
#name2="Iron Man"
#print(name2 + my_list1)
#Error TypeError: can only concatenate str (not "list") to str
name2="Iron Man"
print(f"{name2} + {my_list1[1]}")


#float + int
value3 = 3.3
value4 = 5 
print(value3 + value4)

#bool + bool
my_statement1 = True
my_statement2 = False
print(my_statement1 + my_statement2)



