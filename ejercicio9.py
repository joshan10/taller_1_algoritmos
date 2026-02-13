# 9. Venta con IVA: Solicitar el valor de una venta sin impuestos. Calcular el IVA (19%) y mostrar el valor del IVA y el total con impuesto incluido.

print("=====================================")
print("Venta con IVA")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio9():

    try:
        valor_venta_sinInpuesstos = float(input("Ingrese el valor de la venta sin impuestos: "))

        valor_iva = valor_venta_sinInpuesstos * 0.19
        total_con_impuestos = valor_venta_sinInpuesstos + valor_iva

        print("El valor del iva es de: ", valor_iva)
        print("El total del valor con el iva incluido es de: ", total_con_impuestos)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio9()
