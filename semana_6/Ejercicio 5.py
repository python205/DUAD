

#Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

def count_case(text):
    upper_count = sum(1 for char in text if 'A' <= char <= 'Z')  
    lower_count = sum(1 for char in text if 'a' <= char <= 'z')  
    print(f"There’s {upper_count} upper case and {lower_count} lower cases")


def main():
    my_text = "I love video games"  
    count_case(my_text)  


main()

#Investigue de la funcion count en este articulo https://www.shiksha.com/online-courses/articles/how-to-use-count-function-in-python/#:~:text=Python%20string%20count%20()%20method%3A,the%20below%20example%20%2D1).

