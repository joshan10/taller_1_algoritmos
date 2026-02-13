# 14. Nota final ponderada: Solicitar la nota de tres actividades: talleres (30%), examen parcial (30%) y examen final (40%). Calcular la nota definitiva.

print("=====================================")
print("Nota final ponderada")
print("by joshan ire pereira cabrera")
print("=====================================")

def ejercicio14():

    try:
        nota_talleres = float(input("Introduce la nota de los talleres (30%): "))
        nota_parcial = float(input("Introduce la nota del examen parcial (30%): "))
        nota_final = float(input("Introduce la nota del examen final (40%): "))

        nota_ponderada_talleres = nota_talleres * 0.30
        nota_ponderada_parcial = nota_parcial * 0.30
        nota_ponderada_final = nota_final * 0.40

        nota_definitiva = nota_ponderada_talleres + nota_ponderada_parcial + nota_ponderada_final

        print("\nLa nota definitiva es:", nota_definitiva)

    except ValueError:
        print("Debe ingresar un numero valido")


if __name__== "__main__":
    ejercicio14()
