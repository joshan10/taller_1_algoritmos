# 6. Total de una venta: Solicitar el nombre del producto, el precio unitario y la cantidad comprada. Calcular y mostrar el valor total a pagar.

print("=====================================")
print("Total de una venta")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio6():

    try:
        nombre_del_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("ingrese el precio del producto: "))
        cantidad_comprada = int(input("Ingrese la cantidad comprada: "))

        valorTotalPagar = precio_producto * cantidad_comprada

        print("El total a pagar por ", nombre_del_producto, "es: ", valorTotalPagar)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio6()
