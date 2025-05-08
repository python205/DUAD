#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.



def is_prime(n):
    if n < 2:
        return False  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False  
    return True  


def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]  


def main():
    num_list = [1, 4, 6, 7, 13, 9, 67]  
    prime_numbers = filter_primes(num_list)  
    print(f"Números primos en la lista: {prime_numbers}")


main()







#Investigue de los numeros primos en este articulo https://geekflare.com/dev/prime-number-in-python/