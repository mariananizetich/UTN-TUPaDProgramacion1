print("TRABAJO PRÁCTICO 5 - LISTAS")
# Importación de módulos necesarios
import random

# Ejercicio 1
print("LISTA DE NOTAS")
# Notas de 10 estudiantes
estudiante1 = 5
estudiante2 = 8
estudiante3 = 10
estudiante4 = 9
estudiante5 = 9.50
estudiante6 = 7.50
estudiante7 = 8
estudiante8 = 9
estudiante9 = 8.50
estudiante10 = 3
# Lista de notas
notas = [estudiante1, estudiante2, 
         estudiante3, estudiante4, 
         estudiante5, estudiante6, 
         estudiante7, estudiante8, 
         estudiante9, estudiante10]
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
# Se solicita al usuario elegir entre dos opciones
opcion = input("Si desea agregar un estudiante a la lista, ingrese la letra A. Si desea eliminar uno de la lista, ingrese la letra R: ").upper()
# Para agregar un estudiante a la lista
if opcion == "A":
    nuevo_estudiante = input("Ingrese el nuevo estudiante: ")
    # Se comprueba que no esté en la lista. Si no está, se agrega
    if nuevo_estudiante not in estudiantes:
        estudiantes.append(nuevo_estudiante.capitalize())
        # Se muestra el resultado en bucle for para cumplir con la consigna
        for i in estudiantes:
            print(i)
    else:
        print("El estudiante indicado ya se encuentra en la lista.")
# Para eliminar un estudiante de la lista
elif opcion == "R":
    eliminar_estudiante = input("Qué estudiante desea eliminar de la lista?")
    eliminar_estudiante = eliminar_estudiante.capitalize()
    # Se comprueba que esté en la lista. Si está, se elimina
    if eliminar_estudiante in estudiantes:
        estudiantes.remove(eliminar_estudiante)
        # Se muestra el resultado en bucle for para cumplir con la consigna
        for i in estudiantes:
            print(i)

# Si el usuario ingresa otra letra, se muestra la lista original
else:
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


