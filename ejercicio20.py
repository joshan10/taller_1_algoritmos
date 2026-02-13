# 20. Cálculo de intereses simples: Solicitar el capital, la tasa de interés y el tiempo en meses. Calcular el interés simple y el valor total a pagar.

print("=====================================")
print("Cálculo de intereses simples")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio20():

    try:
        capital = float(input("Ingrese el capital: "))
        tasa_interes = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
        tiempo_meses = int(input("Ingrese el tiempo en meses: "))

        tasa_interes_mensual = tasa_interes / 12 / 100

        interes_simple = capital * tasa_interes_mensual * tiempo_meses

        valor_total = capital + interes_simple

        print(f"El interés simple es: {interes_simple:.2f}")
        print(f"El valor total a pagar es: {valor_total:.2f}")

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio20()
