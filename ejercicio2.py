# 2. Área de un rectángulo: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.

print("=====================================")
print("Área de un rectángulo")
print("by joshan ire pereira cabrera")
print("=====================================")
def ejercicio2():

    try:
        base = float(input("ingrese la base del rectangulo: "))
        altura = float(input("ingrese la altura del rectangulo: "))

        area = round(base * altura)

        print("el area de la altura es: ", area)

    except ValueError:
        print("Debe ingresar un numero valido")

if __name__== "__main__":
    ejercicio2()
    