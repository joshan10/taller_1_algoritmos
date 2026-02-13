import os # Interactua con el sistema operativo (archivos, directorios, rutas, variables de entorno)
import sys # maneja la configuracion y el entorno del interprete de python (argumentos de lineas de comandos, rutas de modulos)
import subprocess # ejecuta comandos externos y programas, controlando sus entrandas y salidas y errores
from colorama import init, Fore, Style, Back # colorama es una biblioteca que permite imprimir texto con colores y estilos en la terminal

init(autoreset=True) # Inicializa colorama

while True:
    #encabezado
    print(Style.BRIGHT + Fore.CYAN + "=====================================")
    print("Taller 1 - Algoritmos basicos en python")
    print("by joshan ire pereira cabrera")
    print("Menu Principal")
    print("=====================================")

    for i in range(1, 26):
        print(f"{i}. Ejecutar algoritmo {i}")
    print("0. Salir \n")

    opcion = input("Seleciona una opción: ")

    if opcion == "0":
        print("Saliendo...")
        break
    if opcion.isdigit() and 1 <= int(opcion) <= 25:
        archivo = f"ejercicio{opcion}.py"

        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
        else:
            print(f"No existe {archivo}")
    else:
        print("Opcion no válida")



    # 
    input("\n Presiona ENTER para continuar....")