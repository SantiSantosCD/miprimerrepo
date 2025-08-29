# filas= 3
# columnas= 3

# matriz=[]
# for i in range(filas):
#     fila=[]
#     for j in range(columnas):
#         fila.append(0)
#     matriz.append(fila)

# # Imprimir la matriz
# for fila in matriz:
#     print(fila)


#ACTIVIDAD A DESARROLLAR
# Desarrollar:
# 1. Crear un método para encapsular el algoritmo que crea una matriz mxn.
# 2. Crea un menú interactivo que tenga las siguientes opciones:
# 	* Restar matrices: Te solicitara la dimensión de la matriz 1 y matriz 2, crear las validaciones necesarias 	de acuerdo a las consideraciones para la suma de matrices.
# 	* Multiplicar matrices: Te solicitara la dimensión de la matriz 1 y matriz 2, crear las validaciones 	necesarias de acuerdo a las consideraciones para la multiplicación de matrices.
# 	* Salir
# En ambas opciones imprimirá las matrices y su matriz resultado. El llenado de los datos de las matrices puede ser un número aleatorio entre 0 y 50 múltiplo de 3.

import random

#Funcion para crear la matriz
def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz

#Funcion para llenar las matrices, con numero aleatorios
def llenar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = random.randint(0, 10) * 5

# Funcion para imprimir matrices
def imprimir_matriz(matriz, nombre):
    print(f"\n{nombre} ({len(matriz)}x{len(matriz[0])}):")
    for fila in matriz:
        print(fila)

#Funcion para restar matrices
def restar_matrices(a, b):
    filas = len(a)
    columnas = len(a[0])
    resultado = crear_matriz(filas, columnas)
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = a[i][j] - b[i][j]
    return resultado

#Funcion para multiplicar matrices
def multiplicar_matrices(a, b):
    filas_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    resultado = crear_matriz(filas_a, cols_b)
    for i in range(filas_a):
        for j in range(cols_b):
            suma = 0
            for k in range(cols_a):  
                suma += a[i][k] * b[k][j]
            resultado[i][j] = suma
    return resultado

def solicitar_entero(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val <= 0:
                print("Ingresa un número entero positivo mayor que 0.")
                continue
            return val
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def menu():

    print("=== MENÚ ===")
    print("1) Restar matrices")
    print("2) Multiplicar matrices")
    print("3) Salir")

    while True:
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            print("\n--- RESTA DE MATRICES ---")
            print("Dimensiones de la matriz A:")
            f1 = solicitar_entero("  Filas : ")
            c1 = solicitar_entero("  Columnas : ")
            print("Dimensiones de la matriz B:")
            f2 = solicitar_entero("  Filas : ")
            c2 = solicitar_entero("  Columnas : ")

            # Validación: para resta deben ser iguales
            if f1 != f2 or c1 != c2:
                print("Error: para restar, ambas matrices deben tener las mismas dimensiones.")
                continue

            m1 = crear_matriz(f1, c1)
            m2 = crear_matriz(f2, c2)
            llenar_matriz(m1)
            llenar_matriz(m2)

            imprimir_matriz(m1, "Matriz A")
            imprimir_matriz(m2, "Matriz B")
            res = restar_matrices(m1, m2)
            imprimir_matriz(res, "Resultado (A - B)")

        elif opcion == "2":
            print("\n--- MULTIPLICACIÓN DE MATRICES ---")
            print("Dimensiones de la matriz A:")
            fa = solicitar_entero("  Filas : ")
            ca = solicitar_entero("  Columnas : ")
            print("Dimensiones de la matriz B:")
            fb = solicitar_entero("  Filas : ")
            cb = solicitar_entero("  Columnas : ")

            # Validación: para multiplicar columnas(A) == filas(B)
            if ca != fb:
                print("Error: para multiplicar A x B necesitas que columnas(A) == filas(B).")
                continue

            A = crear_matriz(fa, ca)
            B = crear_matriz(fb, cb)
            llenar_matriz(A)
            llenar_matriz(B)

            imprimir_matriz(A, "Matriz A")
            imprimir_matriz(B, "Matriz B")
            R = multiplicar_matrices(A, B)
            imprimir_matriz(R, "Resultado (A x B)")

        elif opcion == "3":
            print("Saliste")
            break
        else:
            print("Opción no válida. Elige 1, 2 o 3.")

if __name__ == "__main__":
    menu()

