# 22. Control de inventario: Solicitar la cantidad inicial de un producto en inventario, la cantidad vendida y la cantidad recibida. Calcular el inventario final.

print("=====================================")
print("Control de inventario")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio22():

    try:
        cantidad_inicial_productos = int(input("Ingrese la cantidad inicial de un producto en inventario: "))
        cantidad_vendida = int(input("Ingrese la cantidad vendida del producto: "))
        cantidad_recibida = int(input("Ingrese la cantidad recibida del producto: "))

        calculo_inventario_final = (cantidad_inicial_productos - cantidad_vendida) + cantidad_recibida

        print(f"El inventario final del producto es de {calculo_inventario_final}")

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio22()
