# 13. Promedio de notas: Solicitar tres notas de un estudiante. Calcular el promedio e indicar si aprueba (promedio mayor o igual a 3.0).

print("=====================================")
print("Promedio de notas")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio13():

    try:
        nota1 = float(input("ingrese nota 1: "))
        nota2 = float(input("ingrese nota 2: "))
        nota3 = float(input("ingrese nota 3: "))

        sumaNotas = (nota1 + nota2 + nota3) / 3
        promedio = 3.0

        if sumaNotas >= promedio:
            print("su promedio es de", sumaNotas, "Si aprobo")
        else:
            print("su promedio es de", sumaNotas, "Desaprobo")

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio13()
