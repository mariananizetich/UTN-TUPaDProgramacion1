import os
print("TRABAJO PRÁCTICO - MANEJO DE ARCHIVOS\n")

"""
1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
"""
# Se crea el archivo productos.txt dentro de la carpeta unidad8

"""
2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
"""


# Obtiene la ruta de la carpeta donde está este archivo .py
# Lo tuve que hacer de esta manera porque no se reconocía la ruta del archivo, y al investigar lo pude resolver así
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Se construye la ruta al archivo productos.txt dentro de esa carpeta
ruta_archivo = os.path.join(BASE_DIR, "productos.txt")

print("PRODUCTOS ACTUALES:\n")
# Se crea una función para leer el archivo de productos
def lectura_archivo():
    # Se abre el archivo en modo 'r' para leerlo
    with open(ruta_archivo, "r") as archivo:
        # Se recorre línea por línea
        for linea in archivo:
            # Se eliminan los espacios y saltos de línea con strip()
            linea = linea.strip()
            # Se ignornan las líneas vacías
            if not linea:
                 continue
            # Se dividen los elementos por coma
            partes = linea.split(",")
            
            # Se crea una tupla con los elementos de cada línea
            producto, precio, cantidad = partes
            # Se muestra por pantalla
            print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}\n")
# Se llama a la función para que se ejecute
lectura_archivo()

"""
3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.
"""

# Se inicia un contador en 0 para el manejo de la cantidad de productos que ingrese el usuario
contador = 0
# Se consulta al usuario cuántos productos quiere agregar
cantidad_productos = int(input("¿Cuántos productos desea agregar? "))

# Se inicia un bucle while 
while contador < cantidad_productos:

    # Se solicita al usuario que ingrese un producto nuevo, el precio y la cantidad
    producto_nuevo = input("Por favor, ingrese el producto que desea agregar: ").title()
    precio = input(f"Por favor, ingrese el precio de {producto_nuevo}: ")
    cantidad = input(f"Por favor, ingrese la cantidad de {producto_nuevo}: ")
    # Se abre el archivo en modo 'a' para agregar contenido al final
    with open(ruta_archivo, "a") as archivo:
        # Se agrega el nuevo producto
        archivo.write(f"{producto_nuevo},{precio},{cantidad}\n")
        # Mensaje
        print("Producto agregado correctamente.\n")
    # Se incrementa el contador
    contador += 1

"""
4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad
"""
# Se crea una lista vacía
productos = []

print("PRODUCTOS ACTUALIZADOS:\n")
# Se abre el archivo en modo 'r' para leerlo
with open(ruta_archivo, "r") as archivo:
        for linea in archivo:
            # Se eliminan los espacios y saltos de línea con strip()
            linea = linea.strip()
            if not linea:
                 continue
            # Se dividen los elementos por coma
            partes = linea.split(",")
            
            # Se crea una tupla con los elementos de cada línea
            producto, precio, cantidad = partes
            # Se muestra por pantalla
            print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}\n")

            # Se crea un diccionario para cada producto
            item = {
                 "nombre": producto,
                 "precio": precio,
                 "cantidad": cantidad
            }

            # Se agrega el diccionario del producto a la lista
            productos.append(item)

"""
5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error
"""
print("BUSCADOR DE PRODUCTOS\n")
# Se solicita al usuario el producto que quiere buscar
buscar_producto = input("Por favor, ingrese el nombre del producto que desea buscar: ").title()
# Se inicia una variable bandera para el manejo del bucle
encontrado = False
# Se recorre la lista de productos
for producto in productos:
     # Se comprueba que el producto ingresado exista dentro de la lista
    if producto["nombre"] == buscar_producto:
         # Si existe, se muestra por pantalla
         print(f"Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}\n")
         encontrado = True
# Si no se encuentra el producto, se muestra el mensaje de error
if not encontrado:
    print("El producto ingresado no existe.")

"""
6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.
"""

print("LISTA DEFINITIVA DE PRODUCTOS:\n")
# Se abre el archivo en modo 'w' para sobreescribir en este
with open(ruta_archivo, "w") as archivo:
     for producto in productos:
          archivo.write(f"{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n")
    
# Se vuelve a llamar a la función para leer el archivo
lectura_archivo()