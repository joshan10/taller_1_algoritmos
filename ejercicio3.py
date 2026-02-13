# 3. Conversión de temperatura: Solicitar una temperatura en grados Celsius y convertirla a grados Fahrenheit.

print("=====================================")
print("Conversión de temperatura")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio3():

    try:

        temperatura = float(input("ingrese una temperatura en grados celsius: "))

        fahrenheit = (temperatura * 9/5) + 32

        print("los grados celcius convertidos a fahrenheit son: ", fahrenheit)

    except ValueError:
        print("Debe ingresar un numero valido")

if __name__== "__main__":
    ejercicio3()