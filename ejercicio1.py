
print("ejercicio1")
print("by joshan ire pereira cabrera")

def ejercicio1():

    try:
        #entrada
        num1 = int(input("ingresa un numero entero: "))
        num2 = int(input("ingresa un numero entero: "))
        num3 = int(input("ingresa un numero entero: "))

        # proceso
        suma = num1 + num2 + num3
        promedio = suma / 35


        #salidas
        print("El resultado de la suma es:", suma)
        print("El resultado del promedio es:", promedio)

    except ValueError:
        print("Debe ingresar un numero valido")

if __name__== "__main__":
    ejercicio1()
