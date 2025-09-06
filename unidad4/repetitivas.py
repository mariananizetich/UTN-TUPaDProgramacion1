print("TRABAJO PRÁCTICO 4 - REPETITIVAS")
# Importación de módulos necesarios
import random


# Ejercicio 1
print("NÚMEROS DEL 0 AL 100")
# Se utiliza un bucle for para imprimir todos los números del 0 al 100
for i in range (0, 101):
    print (i)


# Ejercicio 2
print("CANTIDAD DE DÍGITOS DE UN NÚMERO ENTERO")
# Se solicita al usuario que ingrese un número entero, utilizando el método int para asegurarnos de que lo haga correctamente
num_usuario = int(input("Por favor, ingrese un número entero: "))
# Se convierte el número en string; se utiliza el método abs para el manejo de números negativos, y se cuentan los caracteres
num = str(abs(num_usuario))
cant_digitos = len(num)
# Resultado
print(f"La cantidad de dígitos del número {num_usuario} es de {cant_digitos}.")


# Ejercicio 3
print("SUMA DE NÚMEROS ENTRE DOS VALORES")
# Se solicita al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0
# Se utilizan los métodos min y max para el manejo de valores
inicio = min(num1, num2)
fin = max(num1, num2)
# Bucle for para sumar todos los números comprendidos entre los dos valores ingresados, excluyendo los extremos
for i in range(inicio + 1, fin):
    suma += i
# Resultado
print(f"La suma de los números entre {num1} y {num2} es: {suma}")


# Ejercicio 4
print("SUMA EN SECUENCIA")
# Se inicia una variable en 0
suma_numeros = 0
# Se solicita al usuario que ingrese un número
numero = int(input("Ingrese un número entero (0 para finalizar y mostrar la suma): "))
# Se utiliza un bucle while hasta que el usuario ingrese el 0
while numero != 0:
    suma_numeros += numero
    numero = int(input("Ingrese el siguiente número: "))
# Resultado
print(f"El total de la suma es {suma_numeros}")


# Ejercicio 5
print("NÚMEROS ALEATORIOS")
# Número aleatorio entre 0 y 9
aleatorio = random.randint(0, 9)
# Se solicita al usuario que adivine el número
num_usuario = int(input("Adivine el número aleatorio entre 0 y 9: "))
# Se empiezan a contabilizar los intentos
intentos = 1
# Bucle hasta que adivine el número
while num_usuario != aleatorio:
    intentos += 1
    num_usuario = int(input("No es correcto! Intentalo de nuevo: "))
# Se muestra la cantidad de intentos
print(f"Muy bien! Necesitaste {intentos} para adivinarlo.")


# Ejercicio 6
print("NÚMEROS PARES ENTRE 0 Y 100")
# Se utiliza el bucle for para mostrar los números pares en orden decreciente
for i in range(100, 0, -2):
    print(i)


# Ejercicio 7
print("SUMA")
# Se solicita al usuario que ingrese un número
numero_usuario = int(input("Ingrese un número: "))
# Variable para realizar la suma
suma_numeros = 0
# Bucle para sumar los números desde 0 hasta el número ingresado inclusive
for i in range(0, numero_usuario + 1):
    suma_numeros += i
# Resultado
print(f"El total de la suma entre 0 y {numero_usuario} es {suma_numeros}")


# Ejercicio 8
print("NÚMEROS PARES O IMPARES, POSITIVOS O NEGATIVOS.")
# Se inicializan las variables en 0 para contabilizar
num_par = 0
num_impar = 0
num_positivo = 0
num_negativo = 0
# Bucle for para solicitar 100 números al usuario y clasificarlos
for i in range (1,101):
    num = int(input("Ingrese un número: "))
    # Positivo o negativo
    if num > 0:
        num_positivo += 1
    elif num < 0:
        num_negativo += 1
    # Par o impar
    if num % 2 == 0:
        num_par += 1
    else:
        num_impar += 1
# Resultado
print(f"Hay {num_positivo} números positivos; {num_negativo} números negativos; {num_par} números pares; y {num_impar} números impares.")


# Ejercicio 9
print("MEDIA")
cantidad = 100
suma = 0
# Bucle for para leer los números ingresados y acumular su suma, para luego calcular la media
for i in range(cantidad):
    numIngresado = int(input("Ingrese un número: "))
    # Suma de los números ingresados
    suma += numIngresado
# Cálculo de la media
media = suma / cantidad
# Resultado
print(f"La media de los números ingresados es de {media}")


# Ejercicio 10
print("INVERSIÓN DE DÍGITOS")
# Se valida la entrada como número entero
num_original = int(input("Ingrese un número entero: "))
# Se vuelve a convertir en string
num_string = str(num_original)
num_invertido = ""
# Bucle for para recorrer los dígitos en orden inverso y formar el número invertido
for digito in reversed(num_string):
    # Se agrega el dígito al número invertido
    num_invertido += digito
# Resultado
print(f"El número {num_original} invertido es {num_invertido}")