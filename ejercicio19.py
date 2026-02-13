# 19. Conversión de moneda: Solicitar un valor en pesos colombianos y convertirlo a dólares, usando una tasa de cambio ingresada por el usuario.

print("=====================================")
print("Conversión de moneda")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio19():

    try:
        monedaCOP = float(input("Ingrese un valor en pesos colombiando: "))
        tasa_cambio_actual = float(input("Ingrese la tasa de cambio actual (ej. 3800 si 1 USD = 3800 COP): "))

        cambio = monedaCOP / tasa_cambio_actual

        print(f"el cambio de pesos a dolar es de {round(cambio,2)}")

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio19()
