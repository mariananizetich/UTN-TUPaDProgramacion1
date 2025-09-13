print("TRABAJO PRÁCTICO 5 - LISTAS")
# Importación de módulos necesarios
import random

# Ejercicio 1
print("LISTA DE NOTAS")
# Lista de notas
notas = [5, 8, 
         10, 9, 
         9.50, 7.50, 
         8, 9, 
         8.50, 3]
# Se imprime la lista
for nota in notas:
    print(nota)

print("PROMEDIO")
# Se calcula el promedio sumando todas las notas y dividiendo la cantidad de las mismas
promedio = sum(notas) / len(notas)
# Resultado
print(f"El promedio de las notas es {promedio}.")

print("NOTA MÁS ALTA Y NOTA MÁS BAJA")
# Se utilizan los métodos min y max para obtener la nota más baja y la más alta respectivamente
nota_minima = min(notas)
nota_maxima = max(notas)
# Resultado
print(f"Nota más baja: {nota_minima}. Nota más alta: {nota_maxima}.")


# Ejercicio 2
print("LISTA DE PRODUCTOS")
# Se crea una lista vacía
lista = []
# Se solicita al usuario que agregue 5 productos a la lista
for productos in range(5):
    producto = input("Ingrese el producto que desee agregar a la lista: ").lower()
    lista.append(producto)
# Se imprime la lista en orden alfabético
print(sorted(lista))
# Se solicita al usuario que elimine un producto
eliminar_producto = input("Qué producto desea eliminar? ").lower()
# Se comprueba que el producto esté en la lista
if eliminar_producto in lista:
    # Si está, se elimina y se imprime la lista actualizada en orden alfabético
    lista.remove(eliminar_producto)
    print(f"Lista actualizada: {sorted(lista)}.")
# Si no, se le indica por pantalla que no existe.
else:
    print("El producto indicado no aparece en la lista.")


# Ejercicio 3
print("NÚMEROS ALEATORIOS")
# Se crea una lista de números aleatorios, y dos vacías para los números pares e impares
lista_aleatorios = [random.randint(1, 100) for i in range(15)]
lista_pares = []
lista_impares = []
# Bucle for para obtener los números pares e impares
for num in lista_aleatorios:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
# Resultados
print(f"Lista completa: {lista_aleatorios}")
print(f"Lista de números pares: {lista_pares}")
print(f"Lista de números impares: {lista_impares}")
print(f"Cantidad de números pares: {len(lista_pares)}")
print(f"Cantidad de números impares: {len(lista_impares)}")


# Ejercicio 4
print("LISTA SIN REPETICIONES")
# Lista original
datos = [1,3,5,3,7,1,9,5,3]
# Se crea una lista vacía
sin_repeticiones = []
# Bucle for para agregar elementos sin repetir a la nueva lista
for dato in datos:
    if dato not in sin_repeticiones:
        sin_repeticiones.append(dato)
# Resultado
print(f"Lista sin repeticiones: {sin_repeticiones}")


# Ejercicio 5
print("ESTUDIANTES")
# Lista de estudiantes
estudiantes = ["Laura", "Pablo", "Ana", "Pedro", "Juan", "María", "Matías", "Agustina"]
print(f"Lista original: {estudiantes}")
# Se solicita al usuario elegir entre dos opciones
opcion = input("Si desea agregar un estudiante a la lista, ingrese la letra A. Si desea eliminar uno de la lista, ingrese la letra E: ").upper()
# Para agregar un estudiante a la lista
if opcion == "A":
    nuevo_estudiante = input("Ingrese el nuevo estudiante: ")
    # Se comprueba que no esté en la lista. Si no está, se agrega
    if nuevo_estudiante not in estudiantes:
        estudiantes.append(nuevo_estudiante.capitalize())
        print("Lista actualizada:")
        # Se muestra el resultado en bucle for para cumplir con la consigna
        for i in estudiantes:
            print(i)
    else:
        print("El estudiante indicado ya se encuentra en la lista.")
# Para eliminar un estudiante de la lista
elif opcion == "E":
    eliminar_estudiante = input("Qué estudiante desea eliminar de la lista?")
    eliminar_estudiante = eliminar_estudiante.capitalize()
    # Se comprueba que esté en la lista. Si está, se elimina
    if eliminar_estudiante in estudiantes:
        estudiantes.remove(eliminar_estudiante)
        print("Lista actualizada:")
        # Se muestra el resultado en bucle for para cumplir con la consigna
        for i in estudiantes:
            print(i)


# Ejercicio 6
print("NÚMEROS INVERTIDOS")
# Lista de siete números
lista_num = [0, 1, 2, 3, 4, 5, 6]
# Se invierten los números de la lista
lista_num.reverse()
# Resultado
for num in lista_num:
    print(num)

# Ejercicio 7
print("TEMPERATURAS DE LA SEMANA")
# Se crea una matriz con las temperaturas máximas y mínimas de la semana
semana = [
    [18, 4], 
    [17, 12], 
    [20, 8], 
    [21, 9], 
    [24, 13],
    [22, 9],
    [20, 8]
]

minimas = []
maximas = []
# Bucle para obtener las temperaturas y clasificarlas en máximas y mínimas
for dia in semana:
    maxima = dia[0]
    maximas.append(maxima)
    minima = dia[1]
    minimas.append(minima)
# Se calculan los promedios de cada lista
promedio_minima = sum(minimas) / 7
promedio_maxima = sum(maximas) / 7
print(f"Promedio de las mínimas: {round(promedio_minima,2)}. Promedio de las máximas: {round(promedio_maxima,2)}")
# Se obtiene la amplitud térmica
amplitud = 0
lista_amplitud = []
for dia in semana:
    maxima = dia[0]
    minima = dia[1]
    amplitud = maxima - minima
    lista_amplitud.append(amplitud)
# Se obtiene la máxima
amplitud_maxima = max(lista_amplitud)
# Obtengo el índice de la máxima para luego asociarlo con el día de la semana
indice_max = lista_amplitud.index(amplitud_maxima)
# Se crea una lista con los días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# Resultado
print(f"El día de mayor amplitud térmica fue el {dias[indice_max]}")


# Ejercicio 8
print("MATERIAS")
# Matriz de notas. Cada fila corresponde a cada estudiante, y cada columna a cada materia
matriz_notas = [
                [6, 8, 9],
                [10, 9, 7],
                [9, 10, 7],
                [6, 8, 10],
                [5, 8, 6]
                ]
# Lista de materias
materias = ["Matemática", "Biología", "Ciencias Sociales"]

print("---PROMEDIO DE CADA ESTUDIANTE---")
# Se recorre cada fila de la matriz con un bucle for para calcular el promedio de cada estudiante
# Con enumerate se obtiene tanto el índice (número de estudiante) como la fila (sus notas)
for i, fila in enumerate(matriz_notas, start=1):
    promedio = sum(fila) / len(fila)
    # Resultado
    print(f"Promedio Estudiante {i}: {round(promedio,2)}.")

print("---PROMEDIO DE CADA MATERIA---")
# Se recorren las columnas de la matriz con un bucle for para calcular el promedio de cada materia
# Con enumerate se recorre a la vez el índice (posición de la materia) y su nombre
for j, materia in enumerate(materias):
    suma = 0
    for fila in matriz_notas:
        suma += fila[j]
    promedio_materias = suma / len(matriz_notas)
    # Resultado
    print(f"Promedio de {materia}: {round(promedio_materias,2)}.")


# Ejercicio 9
print("TA-TE-TI")

tateti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

turno = 0
ganador = False

# Bucle while hasta 9 jugadas o que haya un ganador
while turno < 9 and not ganador:
    # Se muestra el tablero
    for fila in tateti:
        print(" ".join(fila))

    # Se determina el jugador. Si el turno es par, le toca al jugador 1. Si es impar, al jugador 2
    if turno % 2 == 0:
        simbolo = "X"
        jugador = 1
    else:
        simbolo = "O"
        jugador = 2
    
    # Se solicita al jugador que elija la casilla
    fila = int(input(f"Jugador {jugador} {simbolo}. Seleccione la fila (0-2): "))
    columna = int(input(f"Jugador {jugador} {simbolo}. Seleccione la columna (0-2): "))

    # Se comprueba que la casilla esté libre
    if tateti [fila][columna] == "-":
            tateti[fila][columna] = simbolo
            turno += 1

            # Se muestra el tablero después de la jugada
            for f in tateti:
                print(" ".join(f))

            # Se comprueban las filas
            for f in tateti:
                 if f[0] == f[1] == f[2] != "-":
                      ganador = True
            # Se comprueban las columnas
            for c in range(3):
                 if tateti[0][c] == tateti[1][c] == tateti[2][c] != "-":
                      ganador = True
            # Se comprueban las diagonales
            if tateti[0][0] == tateti[1][1] == tateti[2][2] != "-" or tateti[0][2] == tateti[1][1] == tateti[2][0] != "-":
                 ganador = True
            
            if ganador:
                 print(f"Ganó el jugador {jugador}!")
    else:
        print("La casilla está ocupada, elija otra.")
    
if not ganador:
    print("Se completaron las jugadas, hubo un empate.")



# Ejercicio 10
print("VENTA DE PRODUCTOS")

# Matriz de ventas. Las filas representan los productos, las columnas los días de semana
ventas = [
    [80, 20, 30, 50, 25, 15, 62],
    [12, 71, 36, 20, 18, 38, 49],
    [8, 31, 15, 28, 19, 10, 50],
    [18, 42, 35, 40, 26, 11, 80]
]

print("----Total vendido por producto----")

# Se crea una lista vacía para guardar la suma de ventas de cada producto
total_producto = []

# Bucle for para sumar las ventas de cada producto. Se suma el total de cada fila
for i in range(4):
    total = sum(ventas[i])
    # Se agregan los totales a la lista
    total_producto.append(total)
    # Resultado
    print(f"Producto {i+1}: {total}")

print("----Producto más vendido de la semana----")

# Mayor total de ventas de un producto
valor_maxproducto = max(total_producto)
# Índice del producto más vendido
producto_max = total_producto.index(valor_maxproducto)
# Resultado. Se suma 1 para contabilizar correctamente cada uno
print(f"El producto más vendido de la semana fue el {producto_max + 1} con {valor_maxproducto} ventas.")

print("----Día con mayores ventas totales----")

# Se crea una lista vacía para guardar la suma de ventas por día
totales_dias = []
# Bucle for para recorrer cada columna, que representa cada día de la semana
for j in range(7):
    #Acumulador de cada día
    total_dia = 0
    # Se suman las ventas de todos los productos de ese día
    for i in range(4):
        total_dia += ventas[i][j]
    # Se guarda el total de cada día en la lista
    totales_dias.append(total_dia)

# Mayor total de ventas en un día
venta_max = max(totales_dias)
# Índice del día con más ventas
dia_max = totales_dias.index(venta_max)

# Resultado
print(f"El día de mayores ventas fue el día {dia_max + 1} con {venta_max} ventas.")