print("TRABAJO PRÁCTICO 2 - FUNCIONES")

# Importación de módulos necesarios
import math

"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""
# Se crea la función
def  imprimir_hola_mundo():
    print("Hola Mundo!")
# Se llama a la función para que se ejecute
imprimir_hola_mundo()

"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
# Se crea la función
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
# Se solicita al usuario que ingrese su nombre
nombre = input("Por favor, ingrese su nombre: ").title()
# Se llama a la función
saludar_usuario(nombre)

"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

"""
# Se crea la función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre.title()} {apellido.title()}, tengo {edad} años y vivo en {residencia.title()}.")
# Se solicitan los datos al usuario
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
residencia = input("Por favor, ingrese su lugar de residencia: ")
# Se llama a la función
informacion_personal(nombre, apellido, edad, residencia)

"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""
# Se crean las funciones
def calcular_area_circulo(radio):
    # Se realiza el cálculo del área
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    # Se realiza el cálculo del perímetro
    return 2 * math.pi * radio
# Se solicita al usuario que ingrese el radio
radio = float(input("Por favor, ingrese el radio de un cículo. Vamos a calcular el área y el perímetro: "))
# Se guardan las funciones en las variables correspondientes para luego mostrar los resultados por pantalla
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
# Resultado
print(f"El área del círculo es: {round(area, 2)} y el perímetro: {round(perimetro, 2)}.")


"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

"""
# Se crea la función para hacer el cálculo
def segundos_a_horas(segundos):
    return segundos / 3600
# Se solicita al usuario que ingrese la cantidad de segundos
segundos = input("Por favor, ingrese la cantidad de segundos para calcular a cuántas horas equivalen: ")
# Se comprueba que haya ingresado un número
if segundos.isdigit():
    # Se convierte en entero
    segundos = int(segundos)
    # Se guarda la función del cálculo en una variable para luego mostrar el resultado por pantalla
    cantidad_horas = segundos_a_horas(segundos)
    # Resultado
    print(f"{segundos} equivalen a {round(cantidad_horas, 2)} horas.")
# Mensaje de error
else:
    print("El formato ingresado no es válido. Debe ingresar un número.")


"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función
"""
# Se crea la función
def tabla_multiplicar(numero):
    # Bucle for para multiplicar el número ingresado del 1 al 10
    for i in range(1,11):
        print(f"{numero} x {i} = ", numero * i)
# Se solicita un número al usuario
numero = input("Por favor, ingrese un número para saber su tabla de multiplicar: ")
# Se comprueba que haya ingresado un número
if numero.isdigit():
    # Se convierte en entero
    numero = int(numero)
    # Resultado por pantalla
    print(f"TABLA DE MULTIPLICAR DEL {numero}:\n")
    tabla_multiplicar(numero)
# Mensaje de error
else:
    print("El formato ingresado no es válido. Debe ingresar un número.")


"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara.
"""
# Se crea la función
def  operaciones_basicas(a, b):
    # Suma
    suma = a + b
    # Resta
    resta = a - b
    # Multiplicación
    multiplicacion = a * b
    # Manejo de la división por cero
    if b != 0:
        # División
        division = a / b
    else:
        division = "No es posible dividir por cero."
    # Tupla con las operaciones
    return(suma, resta, multiplicacion, division)

# Se solicitan los operandos al usuario y se convierten a decimales para evitar errores en el programa
a = float(input("Por favor, ingrese el primer operando: "))
b = float(input("Por favor, ingrese el segundo operando: "))

# Se llama a la función
suma, resta, multiplicacion, division = operaciones_basicas(a, b)

# Se muestran los resultados
print(f"SUMA: {a} + {b} = {suma}")
print(f"RESTA: {a} - {b} = {resta}")
print(f"MULTIPLICACIÓN: {a} x {b} = {multiplicacion}")
print(f"DIVISIÓN: {a} / {b} = {division}")


"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

"""
# Se crea la función
def calcular_imc(peso, altura):
    # Se realiza el cálculo
    return peso / altura ** 2
# Se solicita al usuario peso y altura y se convierte cada dato en decimal
peso = float(input("Por favor, ingrese su peso: "))
altura = float(input("Por favor, ingrese su altura: "))
# Se llama a la función
imc = calcular_imc(peso, altura)
# Se muestra el resutado por pantalla
print(f"El índice de masa corporal es: {round(imc, 2)}.")


"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
# Se crea la función
def celsius_a_fahrenheit(celsius):
    # Se realiza la conversión
    return celsius * 9/5 + 32
# Se solicita al usuario que ingrese una temperatura en °C
celsius = float(input("Por favor, ingrese una temperatura en grados Celsius: "))
# Se llama a la función
fahrenheit = celsius_a_fahrenheit(celsius)
# Resultado por pantalla
print(f"{celsius}°C es {round(fahrenheit, 2)}°F.")


"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.

""" 
# Se crea la función
def calcular_promedio(a, b, c):
    # Se realiza el cálculo
    suma = a + b + c
    return round(suma / 3, 2)
# Se solicita al usuario que ingrese los tres números, y se convierten a decimales
print("---CÁLCULO DE PROMEDIO---\n")
a = float(input("Por favor, ingrese el primer número: "))
b = float(input("Por favor, ingrese el segundo número: "))
c = float(input("Por favor, ingrese el tercer número: "))
# Se llama a la función
promedio = calcular_promedio(a, b, c)
# Resultado
print(f"El promedio de los tres números ingresados es {promedio}.")