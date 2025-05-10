#Ejercicio 2

list_a = ["first_name", "last_name", "role"]
list_b = ["John", "Smith", "Software Engineer"]

result = {}
for i in range(len(list_a)):  
    result[list_a[i]] = list_b[i]  

print(result)
