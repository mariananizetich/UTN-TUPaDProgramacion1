# Trabajo Práctico - Estructuras Secuenciales

# Ejercicio 1
# Se muestra por consola el mensaje indicado
print("Hola Mundo!")


# Ejercicio 2
print("SALUDO")
# Ingreso de datos
nombre = input("Indique su nombre: ")
# Se muestra el saludo por consola
print(f"Hola {nombre}!")


# Ejercicio 3
print("DATOS DEL USUARIO")
# Ingreso de datos
nombreUsuario = input("Indique su nombre: ")
apellido = input("Indique su apellido: ")
edad = int(input("Indique su edad: "))
residencia = input("Indique su lugar de residencia: ")
# Se muestra el mensaje con los datos del usuario por consola
print(f"Soy {nombreUsuario} {apellido}, tengo {edad} años, y vivo en {residencia}.")


# Ejercicio 4
print("ÁREA Y PERÍMETRO DE UN CÍRCULO")
# Ingreso de datos
radio = float(input("Ingrese el radio de un círculo: "))
pi = 3.14
area = pi * radio ** 2
perimetro = 2 * pi * radio
# Se muestra área y perímetro por consola, redondeando el resultado de cada uno
print(f"El área del círculo es {round(area, 2)} y el perímetro es {round(perimetro, 2)}.")


# Ejercicio 5
print("CÁLCULO DE HORAS CON SEGUNDOS")
# Ingreso de datos
segundos = int(input("Indique una cantidad de segundos para calcular las horas: "))
# Una hora tiene 3600 segundos; por tanto, se dividen los segundos ingresados por 3600 para hacer el cálculo
cantidadHoras = segundos / 3600
# Se muestra el resultado por consola
print(f"{segundos} segundos equivalen a {round(cantidadHoras, 2)} horas.")


# Ejercicio 6
print("TABLA DE MULTIPLICAR")
# Ingreso de datos
numero = int(input("Ingrese un número:"))
# Se usa un bucle for del el 1 al 10 para calcular la tabla de multiplicar del número ingresado
for i in range (1, 11):
    # Se muestra el resultado por consola
    print(f"{numero} x {i} = {numero * i}")


# Ejercicio 7
print("SUMA, RESTA, MULTIPLICACIÓN Y DIVISIÓN ENTRE DOS NÚMEROS")
# Ingreso de datos
num1 = int(input("Ingrese el primer operando: "))
num2 = int(input("Ingrese el segundo operando: "))
# Si los números ingresados son distintos a cero, se hacen las operaciones y se muestran por pantalla
if num1 !=0 and num2 != 0:
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
# Si no, se le indica al usuario que los datos no son correctos
else:
    print("Alguno de los números ingresados no es correcto.")



# Ejercicio 8
print("CÁLCULO DE MASA CORPORAL")
# Ingreso de datos

altura = float(input("Indique su altura en m: "))
peso = float(input("Ingrese su peso en kg: "))
imc = 0
# Se calcula la masa corporal
imc = (peso / (altura ** 2))
# Se muestra el resultado por consola
print(f"Su masa corporal es de {round(imc, 2)}")


# Ejercicio 9
print("CONVERSIÓN DE GRADOS CELSIUS A GRADOS FAHRENHEIT")
# Ingreso de datos
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
# Se muestra la conversión por consola
print(f"El equivalente de {celsius}°C en grados Fahrenheit es de: {fahrenheit}°F")

# Ejercicio 10
print("CÁLCULO DE PROMEDIO")
# Ingreso de datos
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
promedio = 0
# Se calcula el promedio
promedio = (numero1 + numero2 + numero3) / 3
# Se muestra por pantalla
print(f"El promedio es de {round(promedio)}")

