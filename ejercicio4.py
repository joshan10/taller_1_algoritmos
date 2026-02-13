# 4. Salario semanal: Solicitar la cantidad de horas trabajadas en la semana y el valor por hora. Calcular y mostrar el salario semanal.

print("=====================================")
print("Salario semanal")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio4():

    try:
        horas_trabajadas = int(input("Ingrese las horas trabajas en la semana: "))
        valor_hora = float(input("Ingrese el valor por hora"))

        salario_semanal = horas_trabajadas * valor_hora

        print("su salario semanal es: ", salario_semanal)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio4()


    