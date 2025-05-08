#Cree una función que retorne la suma de todos los números de una lista.
#a. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).



def my_function1(my_list):
    return sum(my_list)  


def main():
    my_list = [5, 4, 3]  
    result = my_function1(my_list)  
    print(f"La suma es: {result}")


main()


#Investigue el uso de sum, este es el articulo https://www.geeksforgeeks.org/sum-function-python/
