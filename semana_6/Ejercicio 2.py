#Experimente con el concepto de scope:
#A. Intente accesar a una variable definida dentro de una función desde afuera.

def my_function1():
    my_list = ["item1", "item2"]
    print(f"Esta es mi lista: {my_list}")
    return my_list  


def main():
    my_list = my_function1()  
    print(f"My lista afuera de la función: {my_list}")


main()


#B. Intente accesar a una variable global desde una función y cambiar su valor.

my_list2 = ["item1", "item2"]

def my_function2():
    print(f"Esta es mi lista: {my_list2}") 


def main2():
    global my_list2  
    my_list2.append("Item3")  
    my_function2()  

main2()

#Para esta parte investigue respecto al uso de la funcion global. Este es el articulo: https://www.w3schools.com/python/python_variables_global.asp