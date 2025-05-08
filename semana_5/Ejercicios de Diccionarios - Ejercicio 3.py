#Ejercicio3

list_of_keys = ["access_level", "age"]

employee = {
    "name": "John",
    "email": "john@umbrellacorporation.com",
    "access_level": 5,
    "age": 28
}

for key in list_of_keys:
    employee.pop(key)  

print(employee)
