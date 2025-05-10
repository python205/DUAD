#Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def sort_hyphen_string(text):
    word_list = text.split("-")  
    word_list.sort()  
    return "-".join(word_list) 


def main():
    my_text = "banana-apple-cherry-date"  
    sorted_text = sort_hyphen_string(my_text)  
    print(f"Original: {my_text}")
    print(f"Sorted: {sorted_text}")


main()

#Investigue respecto a join https://www.w3schools.com/python/ref_string_join.asp
#Referencia del uso de sort https://www.geeksforgeeks.org/sort-in-python/
#Referencia del uso de split https://www.geeksforgeeks.org/python-string-split/