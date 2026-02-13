# 15. Mayor de dos números: Solicitar dos números enteros y mostrar cuál de ellos es mayor o si son iguales.

print("=====================================")
print("Mayor de dos números")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio15():

    try:
        num1 = int(input("Ingrese un numero entero"))
        num2 = int(input("Ingrese un segundo numero entero"))

        if num1 > num2:
            print(f"El número mayor es: {num1}") 
        elif num2 > num1:
            print(f"El número mayor es: {num2}")
        else:
            print("Ambos números son iguales.") 

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio15()
