# 25. Venta diaria de un almacén: Solicitar el número de ventas realizadas en el día y el valor de cada venta. Calcular el total vendido y el promedio por venta.

print("=====================================")
print("Venta diaria de un almacén")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio25():

    try:
        numero_ventas_dia = int(input("Ingrese el numero de ventas realizadas en el dia: "))
        cantidad = []

        for i in range(numero_ventas_dia):
            ventas_dia = int(input("Ingrese el valor de la venta realizadas en el dia: "))
            cantidad.append(ventas_dia)
            total_vendido = sum(cantidad)
            promedio_venta = total_vendido / len(cantidad)

        print(f"\n El total de ventas es de {total_vendido} y el promedio fue de {promedio_venta}")

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio25()
