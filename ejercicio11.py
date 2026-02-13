# 11. Comisión por ventas: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.

print("=====================================")
print("Comisión por ventas")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio11():

    try:
        valor_ventas = float(input("Ingrese el valor total de ventas realizadas: "))
        tasa_comision = 0.05

        comision_ventas = valor_ventas * tasa_comision

        print("el total a recibir con comision es de ", comision_ventas)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio11()
