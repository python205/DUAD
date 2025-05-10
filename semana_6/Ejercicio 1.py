#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.


def my_function1():
    print("Llama a la segunda función")
    my_function2()  


def my_function2():
    print("Hola, soy segunda función.")


my_function1()

