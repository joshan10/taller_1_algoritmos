# 18. Clasificación por edad: Solicitar la edad de una persona e indicar si es menor de edad, adulto o adulto mayor.

print("=====================================")
print("Clasificación por edad")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio18():

    try:
        edad = int(input("Ingrese su edad: "))

        if edad < 18:
            print(f"Su edad es de {edad}, usted es menor de edad")

        elif edad >= 18 and edad <= 59:
            print(f"Su edad es de {edad}, usted es un adulto")
        else:
            print(f"Su edad es de {edad}, usted es un adulto mayor")

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio18()
