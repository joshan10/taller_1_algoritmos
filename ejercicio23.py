# 23. Costo de envío: Solicitar el peso de un paquete. Si pesa hasta 5 kg, el envío cuesta $10.000; si pesa más, cuesta $20.000. Mostrar el valor del envío.

print("=====================================")
print("Costo de envío")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio23():

    try:
        peso_paquete = float(input("Ingrese el peso del paquete: "))

        if peso_paquete <= 5:
            print(f"el paquete pesa {peso_paquete}, el envío cuesta $10.000")
        else:
            print(f"el paquete pesa {peso_paquete}, el envío cuesta $20.000")

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio23()
