# 17. Edad de una persona: Solicitar el año de nacimiento y el año actual. Calcular y mostrar la edad de la persona.

print("=====================================")
print("Edad de una persona")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio17():

    try:
        fecha_nacimiento = int(input("Ingrese el año en el que nacio: "))
        fecha_actual = int(input("Ingrese el año actual: "))

        fecha_user = fecha_actual - fecha_nacimiento

        print("Su edad es de ", fecha_user)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio17()
