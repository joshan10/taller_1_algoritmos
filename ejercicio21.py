# 21. Cálculo de intereses compuestos: Solicitar el capital inicial, la tasa de interés y el número de períodos. Calcular el monto final.

print("=====================================")
print("Cálculo de intereses compuestos")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio21():

    try:
        capital_inicial = float(input("Ingrese el capital inicial: "))
        tasa_interes = float(input("Ingrese la tasa de interés (ej. 0.05 para 5%): "))
        numero_periodos = int(input("Ingrese el número de períodos: "))

        monto_final = capital_inicial * (1 + tasa_interes) ** numero_periodos

        print(f"\n--- Resultado ---")
        print(f"Capital inicial: {capital_inicial:,.2f}")
        print(f"Tasa de interés: {tasa_interes:.2%}")
        print(f"Número de períodos: {numero_periodos}")
        print(f"Monto final (capital + intereses): {monto_final:,.2f}")

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio21()
