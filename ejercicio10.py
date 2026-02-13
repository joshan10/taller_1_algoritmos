# 10. Compra de varios productos: Solicitar la cantidad de productos comprados y el precio de cada uno. Calcular el total de la compra.

print("=====================================")
print("Compra de varios productos")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio10():

    try:
        productos_comprados = int(input("Ingrese la cantidad de productos compradros: "))

        cantidad = []

        for i in range(productos_comprados):
            precio_cada_uno = float(input("Ingrese el precio por el producto: "))

            cantidad.append(precio_cada_uno)
            total_compra = sum(cantidad)

        print("El total de la compra es: ", total_compra)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio10()
