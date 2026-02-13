# 24. Factura de servicios públicos: Solicitar el consumo de agua en metros cúbicos y el valor por metro cúbico. Calcular el valor total de la factura.

print("=====================================")
print("Factura de servicios públicos")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio24():

    try:
        consumo_agua = float(input("Ingrese el consumo de agua en metros cúbicos: "))
        valor_metro_cubico = float(input("Ingrese el valor por metros cubicos: "))

        valor_total_factura = consumo_agua * valor_metro_cubico

        print(f"El valor total de la factura es de: {valor_total_factura:,.2f} ")

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio24()
