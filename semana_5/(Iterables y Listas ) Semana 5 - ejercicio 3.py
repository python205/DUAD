#3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.


my_list = [4, 3, 6, 1, 7]


if my_list:  
    for i, value in enumerate(my_list):
        if i == len(my_list) - 1:  
            my_list[0], my_list[i] = my_list[i], my_list[0]

print(my_list)

