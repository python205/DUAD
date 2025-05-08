#2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.


text = "Batman"

for index in range(len(text) - 1, -1, -1):
    print(text[index])
