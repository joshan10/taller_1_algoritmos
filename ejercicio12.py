# 12. Comisión escalonada: Solicitar el valor de ventas mensuales. Si las ventas son mayores a $1.000.000, la comisión es del 10%; de lo contrario, es del 5%. Mostrar la comisión.

print("=====================================")
print("Comisión escalonada")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio12():

    try:
        ventas_mensuales = float(input("Ingrese el valor de las ventas mensuales: "))
        tasa_comision1 = 0.10 
        tasa_comision2 = 0.05 

        if ventas_mensuales > 1000000:
            comision1 = ventas_mensuales * tasa_comision1
            print("su comision por las ventas es de: ", comision1)

        else:
            comision2 = ventas_mensuales * tasa_comision2
            print("su comision por las ventas es de: ", comision2)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio12()
