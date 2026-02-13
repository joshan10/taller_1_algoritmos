# 7. Venta con descuento fijo: Solicitar el valor total de una compra. Si la compra supera los $200.000, aplicar un descuento del 10%. Mostrar el valor final a pagar.

print("=====================================")
print("Venta con descuento fijo")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio7():

    try:
        valor_total = float(input("Ingrese el valor total que va a pagar: "))

        if valor_total > 200.000:
            descuento = valor_total * 0.10
            precio_final = valor_total - descuento
            print("El valor total a pagar es de: ", precio_final)

        else:
            print("El valor total a pagar sin descuento es de: ", valor_total)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio7()
