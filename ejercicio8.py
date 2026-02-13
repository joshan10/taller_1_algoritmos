# 8. Venta con descuento por porcentaje: Solicitar el precio de un producto y el porcentaje de descuento. Calcular y mostrar el valor del descuento y el precio final.

print("=====================================")
print("Venta con descuento por porcentaje")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio8():

    try:
        valor_producto = float(input("Ingrese el valor de un producto: "))
        valor_descuento = int(input("Ingrese el porcentaje de descuento: "))

        descuento = valor_producto * valor_descuento
        precio_final = descuento - valor_producto

        print("El precio total del producto con descuento es de: ", precio_final)
        print("El descuento es de: ", descuento)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio8()
