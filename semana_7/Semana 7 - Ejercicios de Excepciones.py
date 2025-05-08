

def mostrar_menu():
    print("\nSeleccione una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado")
    print("6. Salir")

def main():
    actual = 0  

    while True:
        print(f"\nNumero actual: {actual}")
        mostrar_menu()
        
        try:
            opcion = int(input("Ingrese una opcion (1-6): "))
            
            if opcion == 6:
                print("Hasta luego")
                break

            if opcion not in [1, 2, 3, 4, 5]:
                print("Opcion invalida.")
                continue

            if opcion == 5:
                actual = 0
                print("Resultado borrado.")
                continue

            nuevo = float(input("Ingrese el numero: "))

            if opcion == 1:
                actual += nuevo
            elif opcion == 2:
                actual -= nuevo
            elif opcion == 3:
                actual *= nuevo
            elif opcion == 4:
                if nuevo == 0:
                    print("Error: No se puede dividir entre cero.")
                    continue
                actual /= nuevo

        except ValueError:
            print("Error: Entrada no valida. Ingrese un número.")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")


main()
