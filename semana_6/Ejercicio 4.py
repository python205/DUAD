#4. Cree una función que le de la vuelta a un string y lo retorne.



def reverse_string(text):
    return text and text[-1] + reverse_string(text[:-1])


def main():
    my_text = "The Last of Us"  
    reversed_text = reverse_string(my_text)  
    print(f"Original: {my_text}")
    print(f"Reversed: {reversed_text}")


main()


