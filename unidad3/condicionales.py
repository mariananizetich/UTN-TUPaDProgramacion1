# TRABAJO PRÁCTICO DE CONDICIONALES - PROGRAMACIÓN 1

# Importación de módulos necesarios
from statistics import mode, median, mean
import random

# Ejercicio 1
print("MAYOR DE EDAD")
# Definición de la constante para mayoría de edad
MAYOR_EDAD = 18

# Se solicita al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Si el usuario es mayor a 18 años, se muestra el mensaje por consola
if edad > MAYOR_EDAD:
    print("Es mayor de edad.")


# Ejercicio 2
print("APROBADO O DESAPROBADO")
# Se solicita al usuario que ingrese su nota
notaUsuario = int(input("Ingrese su nota: "))

# Teniendo en cuenta que se aprueba con 6, se indica por pantalla si está aprobado o desaprobado.
if notaUsuario >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")


# Ejercicio 3
print("NÚMERO PAR")
# Se solicita al usuario que ingrese un número par
numUsuario = int(input("Ingrese un número par: "))

# Se verifica si el número ingresado es par y se comunica por consola.
if (numUsuario % 2 == 0):
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")


# Ejercicio 4
print("CLASIFICACIÓN POR EDAD")
# Definición de constantes
NINIO = 12
ADOLESCENTE = 18
ADULTO = 30

# Se solicita la edad al usuario
edadUsuario = int(input("Ingrese su edad: "))

# Se clasifica la edad en categorías
if edadUsuario < NINIO:
    print("Usted es niño o niña.")
elif edadUsuario >= NINIO and edadUsuario < ADOLESCENTE:
    print("Usted es adolescente.")
elif edadUsuario >= ADOLESCENTE and edadUsuario < ADULTO:
    print("Usted es adulto/a joven.")
elif edadUsuario >= ADULTO:
    print("Usted es adulto o adulta.")


# Ejericio 5
print("CONTRASEÑA ENTRE 8 Y 14 CARACTERES")
# Definición de constantes
MINIMO = 8
MAXIMO = 14

# Se solicita al usuario que ingrese una contraseña
contraseniaUsuario = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

# Se mide la longitud de la contraseña con la función len
longContrasenia = len(contraseniaUsuario)

# Se comprueba si cumple con el rango de caracteres
if longContrasenia >= MINIMO and longContrasenia <= MAXIMO:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.") 


# Ejercicio 6
print("MEDIDAS ESTADÍSTICAS")
# Se crea una lista de 50 números aleatorios entre 1 y 100 utilizando el paquete random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Se muestra la lista por pantalla
print(numeros_aleatorios)

# Se calculan las medidas estadísticas
media = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)

# Se muestran los resultados por pantalla
print(f"MEDIA: {media}")
print(f"MODA: {moda}")
print(f"MEDIANA: {mediana}")

# Se determina el tipo de sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo.")
elif media == mediana and mediana == moda:
    print("Sin sesgo.")


# Ejercicio 7
print("ÚLTIMA LETRA VOCAL")
# Se solicita al usuario que ingrese una palabra o frase.
palabra = input("Ingrese la frase o palabra que desee: ")
# Se obtiene la última letra y se convierte en minúscula
ultimaLetra = palabra[-1].lower()

# Se comprueba si la última letra es una vocal, incluyendo acentos, con el operador 'in'
if ultimaLetra in "aeiou" or ultimaLetra in "áéíóú":
    # Si termina en vocal, se agrega un signo de exclamación al final 
    print(f"{palabra}!")
    # Si no, se imprime tal cual
else:
    print(palabra)


# Ejercicio 8
print("FORMATO DE NOMBRE")
# Se pide el nombre al usuario
nombre = input("Por favor, ingrese su nombre: ")
# Se le da a elegir una opción de formato
eleccion = input("Ingrese la opción que desee:\n 1. Su nombre en mayúsculas.\n 2. Su nombre en minúsculas.\n 3. Su nombre con la primera letra en mayúscula.\n")

# Se transforma el nombre según la opción elegida
if eleccion == "1":
    print(nombre.upper())
elif eleccion == "2":
    print(nombre.lower())
elif eleccion == "3":
    print(nombre.title())
else:
    print("La opción ingresada no es válida.")


# Ejercicio 9
print("ESCALA DE RICHTER")
# Se solicita al usuario que ingrese la magnitud de un terremoto
magnitud = float(input("Por favor, ingrese la magnitud de un terremoto: "))

# Se clasifica el terremoto según rangos de la escala de Richter
if magnitud < 3:
    print(f"Magnitud: {magnitud}. Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print(f"Magnitud: {magnitud}. Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
   print(f"Magnitud: {magnitud}. Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
   print(f"Magnitud: {magnitud}. Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print(f"Magnitud: {magnitud}. Muy fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print(f"Magnitud: {magnitud}. Extremo (puede causar graves daños a gran escala).")


# Ejercicio 10
print("ESTACIÓN DEL AÑO POR HEMISFERIO")

# Definición de constantes
ENERO = 1
FEBRERO = 2
MARZO = 3
ABRIL = 4
MAYO = 5
JUNIO = 6
JULIO = 7
AGOSTO = 8
SEPTIEMBRE = 9
OCTUBRE = 10
NOVIEMBRE = 11
DICIEMBRE = 12
# Se solicita al usuario que ingrese la fecha. Día y mes por separado
dia = int(input("Por favor, ingrese el día (1-31): "))
mes = int(input("Por favor, ingrese el mes (1-12): "))
# Se crea una tupla para agrupar día y mes
fecha_usuario = (dia, mes)

# Se pregunta al usuario en qué hemisferio se encuentra
hemisfero = input("Por favor, indique en qué hemisferio se encuentra (N/S): ").upper()

# Explicación sobre el operador 'in':
# Se utiliza el operador 'in' para comprobar si el mes está dentro de la lista de meses, evitando usar múltiples 'or' como 'mes == ENERO or mes == FEBRERO'

# Hemisferio norte
if hemisfero == "N":
    if (mes == DICIEMBRE and dia >= 21) or (mes in [ENERO, FEBRERO]) or (mes == MARZO and dia <= 20):
        print("Invierno en Hemisferio Norte.")
    elif (mes == MARZO and dia >= 21) or (mes in [ABRIL, MAYO]) or (mes == JUNIO and dia <= 20):
        print("Primavera en Hemisferio Norte.")
    elif (mes == JUNIO and dia >= 21) or (mes in [JULIO, AGOSTO]) or (mes == SEPTIEMBRE and dia <= 20):
        print("Verano en Hemisferio Norte.")
    elif (mes == SEPTIEMBRE and dia >= 21) or (mes in [OCTUBRE, NOVIEMBRE]) or (mes == DICIEMBRE and dia <= 20):
        print("Otoño en Hemisferio Norte.")
# Hemisferio sur
elif hemisfero == "S":
    if (mes == DICIEMBRE and dia >= 21) or (mes in [ENERO, FEBRERO]) or (mes == MARZO and dia <= 20):
        print("Verano en Hemisferio Sur.")
    elif (mes == MARZO and dia >= 21) or (mes in [ABRIL, MAYO]) or (mes == JUNIO and dia <= 20):
        print("Otoño en Hemisferio Sur.")
    elif (mes == JUNIO and dia >= 21) or (mes in [JULIO, AGOSTO]) or (mes == SEPTIEMBRE and dia <= 20):
         print("Invierno en Hemisferio Sur.")
    elif (mes == SEPTIEMBRE and dia >= 21) or (mes in [OCTUBRE, NOVIEMBRE]) or (mes == DICIEMBRE and dia <= 20):
        print("Primavera en Hemisferio Sur.")
else:
    print("La opción ingresada no es válida.")