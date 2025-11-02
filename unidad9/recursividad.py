print("TRABAJO PRÁCTICO - RECURSIVIDAD")

"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""

# Función recursiva para Factorial
def factorial(n):
    # Caso base: si el número es 0, devuelve 1
    if n == 0:
        return 1
    # Recursividad: si no, devuelve el factorial
    else:
        return n * factorial(n - 1)
    
print(factorial(6))

# Se solicita un número al usuario
num = int(input("Ingrese un número positivo: "))

# Bucle for para recorrer todos los números entre 1 y num
for i in range(1, num + 1):
    # Se llama a la función para calcular factorial en cada iteración
    resultado = factorial(i)
    # Resultado
    print(resultado)

"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""

# Función recursiva para Fibonacci

def fibonacci(posicion):
    # Caso base: Si la posición es 0, devuelve cero. Si la posición es 1, devuelve 1
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    # Recursividad: Se realiza la suma
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)
    
# Se llama a la función
print(fibonacci(6))

# Se solicita un número al usuario
num_usuario = int(input("Ingrese un número positivo: "))

# Se recorren las posiciones desde el 0 hasta el número ingresado
for i in range(num_usuario + 1):
    # Se imprimen resultados
    print(f"Posición {i}: - Valor Fibonacci: {fibonacci(i)}")

"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1)
. Prueba esta función en un
algoritmo general.
"""
# Función recursiva para Potencia
def calcular_potencia(base, exp):
    #   Caso base: Si el exponente es 0, se devuelve 1. Si es 1, devuelve el mismo número
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    # Recursividad: Se calcula la potencia del número
    else:
        return base * calcular_potencia(base, exp-1)
    
# Algoritmo general

# Se solicita la base al usuario
base = int(input("Ingrese la base: "))

# Se solicita el exponente al usuario
exp = int(input("Ingrese el exponente: "))

# Se llama a la función
print(calcular_potencia(base, exp))

"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
"""

# Función recursiva Decimal a Binario
def conversion_binario(n):

    # Caso base: cuando el número sea 0, se devuelve un string vacío
    if n == 0:
        return ""
    # Recursividad: Se calcula el resto de dividir el número por 2
    # Se llama a la función recursiva, y se concatena el resultado de la recursión con el resto actual
    else:
        resto = n % 2
        return conversion_binario(n // 2) + str(resto)

# Definición de variables
n = 10

# Se llama a la función
print(f"Decimal: {n} - Binario: {conversion_binario(n)}")


"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
"""

# Definición de variables
cadena = input("Ingrese una palabra o frase: ")
cadena_limpia = ""

# Primero, con un bucle for se eliminan espacios y acentos
for letra in (cadena):
    if letra == " ":
        continue
    elif letra == "á":
        cadena_limpia += "a"
    elif letra == "é":
        cadena_limpia += "e"
    elif letra == "í":
        cadena_limpia += "i"
    elif letra == "ó":
        cadena_limpia += "o"
    elif letra == "ú":
        cadena_limpia += "u"
    else:
        cadena_limpia += letra

cadena = cadena_limpia.lower()
    
# Función recursiva para comprobar palíndromo
def palindromo(cadena):
    # Caso base: si tiene 0 o 1 caracter, es Palíndromo
    if len(cadena) <= 1:
        return True
    # Segundo caso base: Si la primera y última letra son diferentes, no es Palíndromo
    elif cadena[0] != cadena[-1]:
        return False
    # Recursividad: Se llama a la función recursiva con la subcadena interna
    else:
        return palindromo(cadena[1:-1])

resultado = palindromo(cadena)

# Se muestra por pantalla
if resultado == True:
    print(f"La cadena {cadena} es Palíndromo.")
else:
    print(f"La cadena {cadena} no es Palíndromo.")


"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
"""

# Función recursiva Palíndromo
def suma_digitos(n):
    # Caso base: si el número tiene un solo dígito, ya no se puede descomponer
    if n < 10:
        return n
    # Recursividad: se obtiene el último dígito y se suma con el resto del número
    else:
        ultimo_digito = n % 10
        return ultimo_digito + suma_digitos(n // 10)
    
# Se llama a la función
print(suma_digitos(1234))

"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
 Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)

"""

def contar_bloques(n):
    # Caso base: Cuando se llegue al último nivel, se devuelve 1
    if n == 1:
        return 1
    else:
        # Recursividad: Se suman los bloques del nivel actual con los de niveles superiores
        return n + contar_bloques(n - 1)
# Se llama a la función
print(contar_bloques(4))


"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
 Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0
"""
def contar_digito(numero, digito):
    # Caso base: cuando el número tenga un solo dígito
    # Si ese dígito es igual al buscado, se devuelve 1. Si no, se devuelve 0
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    # Recursividad: Se obtiene el último dígito del número
    else:
        ultimo = numero % 10
        # Si el último dígito es igual al buscado, se suma 1 y se continúa con el resto del número
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        # Si no coincide, se continúa con el resto sin sumar nada
        else:
            return contar_digito(numero // 10, digito)


# Se llama a la función
print(contar_digito(222335558810, 2))