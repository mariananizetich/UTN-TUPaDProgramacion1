print("TRABAJO PRÁCTICO - DATOS COMPLEJOS\n")

"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

print("FRUTAS\n")
precios_frutas = {"Banana": 1200, 
                  "Ananá": 2500, 
                  "Melón": 3000, 
                 "Uva": 1450

}
# Se agregan las frutas con sus respectivos precios al diccionario
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
# Se muestra por pantalla
print(precios_frutas)

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
# Actualización de precios
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
# Resultado por pantalla
print(precios_frutas)

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""
# Se utiliza keys para mostrar solamente las frutas del diccionario
frutas_sinprecio = precios_frutas.keys()
# Se muestran por pantalla
print(frutas_sinprecio)

"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""
print("---CONTACTOS TELEFÓNICOS---\n")
# Se inicia un diccionario vacío
contactos = {}
# Bucle for para agregar 5 contactos
for i in range(5):
    nombre = input("Por favor, ingrese el nombre del contacto que desea agregar: ").title()
    telefono = input(f"Por favor, ingrese el teléfono de {nombre}: ")
    # Se agrega el nombre y teléfono al diccionario
    contactos[nombre] = telefono
 
# Buscador
buscar_nombre = input("Ingrese el nombre del contacto que desea buscar: ").title()
# Se comprueba que el nombre ingresado esté en el diccionario
if buscar_nombre in contactos:
    # Se muestra el teléfono por pantalla
    print(f"Nombre: {buscar_nombre}\nTeléfono: {contactos[buscar_nombre]}")
else:
    # Si no existe el nombre ingresado, se comunica por pantalla
    print(f"El nombre {buscar_nombre} no existe en la lista de contactos.")

"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra
"""
print("---FRASE---\n")
# Se solicita la frase al asuario
frase_usuario = input("Por favor, ingrese una frase: ").lower()
# Se usa el método split para separar la frase en palabras individuales
palabras = frase_usuario.split()
# Se usa set para obtener las palabras únicas
palabras_unicas = set(palabras)
# Se muestran por pantalla
print(f"PALABRAS ÚNICAS\n {palabras_unicas}\n")

# Contador de palabras
# Se crea un diccionario vacío
contador = {}
# Se recorre el diccionario para obtener la cantidad de veces que aparece cada palabra
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
# Se muestra por pantalla
print("CONTADOR DE PALABRAS\n")
for palabra, cantidad in contador.items():
    print(f"{palabra}: {cantidad}")


"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""
print("---NOTAS DE ALUMNOS---\n")
# Se crea un diccionario vacío para almacenar los alumnos
alumnos = {

}
# Se inicia un bucle for para pedir hasta tres alumnos al usuario
for a in range(3):
        alumno = input("Por favor, ingrese el nombre del almumno/a: ").title()
        # Se crea una lista vacía para guardar las tres notas del alumno
        notas = []
        # Se inicia otro bucle for para pedir hasta tres notas al usuario
        for n in range(3):
            nota = float(input(f"Por favor, ingrese las tres notas de {alumno}: "))
            notas.append(nota)
            # Se convierte la lista en una tupla
            alumnos[alumno] = tuple(notas)
# Se muestran las notas por pantalla
print(f"NOTAS:\n")
print(alumnos)

print("PROMEDIOS:\n")
# Cálculo de promedio

# Se recorre el diccionario y la tupla para obtener los alumnos con sus respectivas notas
for alumno, notas in alumnos.items():
      # Se calcula el promedio de cada uno
      promedio = sum(notas) / len(notas)
      # Se muestra por pantalla
      print(f"ALUMNO/A: {alumno} - PROMEDIO: {round(promedio)}\n")


"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""
print("---ESTUDIANTES APROBADOS---\n")
# Sets de parciales aprobados
parcial1 = {4, 6, 8, 9}
parcial2 = {6, 8, 10, 9}

# Estudiantes que aprobaron ambos parciales
ambos_parciales = parcial1 & parcial2
# Se muestra por pantalla
print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")

# Estudiantes que aprobaron solo un parcial
solo_unparcial = parcial1 ^ parcial2
# Se muestra por pantalla
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {solo_unparcial}")

# Lista total de estudiantes que aprobaron al menos un parcial
almenos_unparcial = parcial1 | parcial2
# Se muestra por pantalla
print(f"Estudiantes que aprobaron al menos uno de los dos parciales: {almenos_unparcial}")


"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""

print("---CATÁLOGO DE PRODUCTOS---\n")
# Diccionario de productos y stock
productos = {
    "Remeras": 5,
    "Jeans": 6,
    "Camisas": 1,
}

# Consulta de stock
# Se solicita al usuario que ingrese un producto
producto = input("Por favor, ingrese el nombre del producto que desea consultar: ").title()
# Se comprueba si está en el diccionario
if producto in productos:
    # Se muestra el stock
    print(f"Stock de {producto}: {productos[producto]}")

    # Agregar unidades al stock
    # Se consulta al usuario cuántas unidades desea agregar
    unidades = int(input(f"¿Cuántas unidades de {producto} desea agregar? "))
    # Se suman las unidades ingresadas al stock del producto
    productos[producto] += unidades
    # Se muestra por pantalla
    print(f"¡Gracias por agregar {unidades} unidades al producto {producto}! Stock actualizado: {productos[producto]}.")
# Si el producto no está, se da la opción al usuario de agregarlo
else:
    opcion = input("El producto ingresado no existe, ¿desea agregarlo? S/N: ").upper()
    if opcion == "S":
        # Si desea agregar, se solicita que ingrese las unidades
        stock = int(input(f"Por favor, ingrese la cantidad de unidades del producto {producto}: "))
        # Se agrega el producto a la lista con el stock correspondiente
        productos[producto] = stock
        # Se muestra por pantalla
        print(f"¡Gracias por agregar {stock} unidades al producto {producto}!")
        print("Stock actualizado de productos\n")
        for prod, cant in productos.items():
            print(f"{prod}: {cant} unidades.")
    # Se agradece al usuario si no desea agregar nada
    else:
        print("¡Gracias por consultar nuestro catálogo!")


"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.
"""
print("---AGENDA---\n")

# Se crea la agenda
agenda = {
    ("Lunes", "10:30"): "Matemática I",
    ("Martes", "11:00"): "Programación I",
    ("Miércoles", "11:00"): "Lógica I",
    ("Jueves", "11:30"): "Matemática II",
    ("Viernes", "10:30"): "Programación II"
}
# Se solicita al usuario que ingrese el día y hora que quiere consultar
dia = input("Por favor, ingrese el día que desee consultar: ").strip().title()
hora = input("Por favor, ingrese la hora: ").strip()
# Se crea una tupla con el día y la hora
clave = (dia, hora)
# Se comprueba que el día y hora ingresados estén en la agenda
if clave in agenda:
    # Se muestra en pantalla
    print(f"EVENTO: {agenda[clave]}")
# Mensaje si no hay ningún evento
else:
    print("No hay ningún evento programado para esa fecha y hora.")



"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""
print("---PAÍSES---")
# Diccionario de países con sus capitales
paises = {
    "Argentina": "Buenos Aires",
    "Uruguay": "Montevideo",
    "Brasil": "Brasillia",
    "Chile": "Santiago de Chile",
    "Bolivia": "Sucre",
    "Perú": "Lima"    
}

# Diccionario invertido
# Con un bucle for se recorre el diccionario de manera inversa y se crea uno nuevo
invertido = {valor: clave for clave, valor in paises.items()}
# Se muestra por pantalla
print(invertido)