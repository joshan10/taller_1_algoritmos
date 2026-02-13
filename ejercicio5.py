# 5. Salario con horas extra: Solicitar horas trabajadas y valor por hora. Si el empleado trabajó más de 40 horas, las horas adicionales se pagan al 150%. Calcular el salario total.

print("=====================================")
print("Salario con horas extra")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio5():

    try:
        horas_trabajadas = int(input("Ingrese las horas trabajas en la semana: "))
        valor_hora = float(input("Ingrese el valor por hora: "))
        salario_semanal = horas_trabajadas * valor_hora

        aumento = 1 + 1.50
        monto_final = salario_semanal * aumento 

        if salario_semanal > 40 :
            aumento = 1 + 1.50
            monto_final = salario_semanal * aumento 
            print("su salario semanal con horas extras es de: ", monto_final)

        else:
            print("su salario semanal sin horas extras es de: ", salario_semanal)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio5()
