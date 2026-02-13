# 16. Número par o impar: Solicitar un número entero e indicar si es par o impar.

print("=====================================")
print("Número par o impar")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio16():

    try:
        num = int(input("Ingrese un numero: "))

        if num % 2 == 0:
            print("El num ", num, " es par" )
        else:
            print("El num ", num, " es impar" )

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio16()
