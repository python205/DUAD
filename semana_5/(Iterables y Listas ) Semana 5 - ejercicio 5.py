#5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

numbers = []

print("Enter 10 numbers")
for index in range(10):
    num = int(input(f"Enter the number {index + 1}: "))
    numbers.append(num)

highest = max(numbers)

print(f"You entered these numbers: {numbers}")
print(f"The highest number is: {highest}")


