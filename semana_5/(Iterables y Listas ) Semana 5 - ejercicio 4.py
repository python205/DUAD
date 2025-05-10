#4. Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = [num for num in my_list if num % 2 == 0]

print(my_list)
