print("====BIBLIOTECA ESCOLAR====\n")

# Se crean las listas vacías
titulos = []
ejemplares = []

# Se inicia un bucle while para que el usuario elija una opción del menú
eleccion = ""
while eleccion != "8":
    print("MENÚ DE OPCIONES \n")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir\n")
    # Se solicita al usuario que elija una opción del menú, y se guarda en una variable
    eleccion = input("Seleccione la opción del menú que desee realizar: ")
    print("\n")
    # Match case según la elección que haya elegido
    match eleccion:
        # Ingresar títulos
        case "1":
            # Se inicia un contador en 0 para el manejo de la cantidad de títulos
            contador = 0
            # Se solicita al usuario que ingrese la cantidad de títulos a agregar
            cantidadTitulos = input("¿Cuántos títulos desea agregar? ")
            # Se comprueba que ingrese un número
            if cantidadTitulos.isdigit():
                # Se convierte a entero
                cantidadTitulos = int(cantidadTitulos)
                # Se comprueba que la cantidad sea mayor que 0
                if cantidadTitulos > 0:
                    # Se inicia un bucle while hasta que el contador iguale la cantidad ingresada por el usuario
                    while contador < cantidadTitulos:
                        # Se solicita al usuario que ingrese un título
                        # Uso de método strip para evitar espacios en el inicio y final del string
                        # Uso de método title para convertir a mayúsculas la primera letra de cada palabra
                        tituloNuevo = input("Indique el título que desea agregar: ").strip().title()
                        # Se comprueba que el título nuevo no exista en el catálogo
                        if tituloNuevo in titulos:
                            # Mensaje de error
                            print("El título que desea agregar ya existe en el catálogo.\n")
                            continue
                        # Se comprueba que no ingrese un título vacío
                        elif tituloNuevo == "":
                            # Mensaje de error
                            print("No es posible agregar un título vacío.\n")
                            continue
                        # Se agrega el título a la lista
                        else:
                            titulos.append(tituloNuevo)
                            # Se agrega un ejemplar inicializado en 0 para mantener la sincronía entre las listas
                            ejemplares.append(0)
                            # Se muestra en pantalla
                            print(f"El título {tituloNuevo} fue agregado con éxito. Para agregar ejemplares, elija la opción 2 del menú.\n")
                            # Se incrementa el contador
                            contador += 1
                # Mensaje de error si la cantidad es inválida
                else:
                    print("La cantidad ingresada no es válida. Debe ingresar un número entero mayor que 0.\n")
            # Mensaje de error si el formato es inválido.
            else:
                print("Formato inválido. Debe ingresar un número entero mayor que 0.\n")

        
        # Agregar ejemplares
        case "2":
            # Se le consulta al usuario en qué título desea agregar ejemplares
            print("En qué título desea agregar ejemplares?")
            titulo = input().title()
            if titulo not in titulos:
                print("El título ingresado no existe en nuestro catálogo.\n")
            else:
                cantidad = input(f"Ingrese la cantidad de ejemplares para {titulo}: ")
                 # Se comprueba que ingrese un número
                if cantidad.isdigit():
                    # Se convierte a entero
                    cantidad = int(cantidad)
                    # Se comprueba que sea mayor o igual a 0
                    if cantidad >= 0:
                        # Se busca el índice del título
                        indice = titulos.index(titulo)
                        # Se suman los ejemplares al título correspondiente
                        ejemplares[indice] += cantidad
                        print(f"Se agregaron correctamente los {cantidad} ejemplares al título {titulo}.\n")
                    # Mensaje de error
                    else:
                        print("La cantidad de ejemplares ingresada no es válida.\n")
                # Mensaje de error
                else:
                    print("Formato inválido, debe ingresar un número entero mayor o igual que 0.\n")

        # Mostrar catálogo
        case "3":
                print("CATÁLOGO DE LIBROS\n")
                # Se comprueba que el catálogo no esté vacío
                if not titulos:
                        print("El catálogo de libros está vacío.\n")
                else:
                # Se muestra el catálogo de libros con sus respectivos ejemplares
                    for i in range(len(titulos)):
                        print(f"-{titulos[i]}: {ejemplares[i]} ejemplares.\n")

        # Disponibilidad
        case "4":
            # Se solicita al usuario que ingrese el título del que quiere saber la disponibilidad
            titulo = input("Ingrese el título del libro que desea consultar disponibilidad: ").strip().title()
            # Se comprueba que exista en el catálogo
            if titulo in titulos:
                # Se busca el ínidice del título
                indice = titulos.index(titulo)
                # Se muestra por pantalla
                print(f"El libro '{titulos[indice]}' tiene {ejemplares[indice]} ejemplares.\n")
            else:
                print("El título indicado no existe en nuestro catálogo.\n")
            
        # Listado de ejemplares agotados
        case "5":
            # Primero se comprueba que el catálogo no esté vacío
            if not titulos:
                print("El catálogo está vacío.\n")
            else:
                # Se crea una variable booleana que se inicia en False.
                # Esto permitirá que si en el bucle no se encuentra ningún ejemplar agotado, se muestre el mensaje por pantalla al salir del bucle
                agotados = False
                # Se recorre la lista de títulos para comprobar si hay ejemplares agotados
                for i in range(len(titulos)):
                    if ejemplares[i] == 0:
                        # Se muestran los ejemplares agotados en pantalla
                        print(f"TÍTULOS AGOTADOS:\n - {titulos[i]}: 0 ejemplares.\n")
                        # Se actualiza la variable
                        agotados = True
                # Si no hubo ejemplares agotados, se muestra por pantalla
                if not agotados:
                    print("Actualmente no hay libros con stock agotado.\n")

        # Agregar título
        case "6":
            # Se solicita al usuario que ingrese el nuevo título
            tituloNuevo = input("Indique el título que desea agregar: ").strip().title() 
            # Se comprueba que no esté en el catálogo
            if tituloNuevo in titulos: 
                print("El título que desea agregar ya existe en el catálogo.\n")
            # Se comprueba que no ingrese un título vacío
            elif tituloNuevo == "": 
                print("No es posible ingresar un título vacío.\n")
            else:
                # Se agrega el título a la lista
                titulos.append(tituloNuevo)
                # Se solicita al usuario que ingrese la cantidad de ejemplares del nuevo título
                # En este caso se obliga al usuario agregar los ejemplares para sincronizar las listas y hacer el código más dinámico
                cantidadEjemplares = input(f"Ingrese la cantidad de ejemplares para {tituloNuevo}: ")
                # Se comprueba que ingrese un número
                if cantidadEjemplares.isdigit():
                    # Se convierte a entero
                    cantidadEjemplares = int(cantidadEjemplares)
                    # Se comprueba que sea mayor o igual a 0
                    if cantidadEjemplares >= 0:
                        # Se agrega la cantidad a la lista
                        ejemplares.append(cantidadEjemplares)
                        # Se muestra por pantalla
                        print(f"El título '{tituloNuevo}' se agregó correctamente al catálogo con {cantidadEjemplares} ejemplares.\n")
                    else:
                        print("La cantidad de ejemplares ingresada no es válida.\n")
                        
                else:
                    print("La cantidad de ejemplares ingresada no es válida.\n")
                   

        # Actualización de ejemplares
        case "7":
            print("PRÉSTAMOS Y DEVOLUCIONES DE EJEMPLARES\n")
            # Se solicita al usuario que ingrese el título del libro
            titulo = input("Ingrese el título del libro: ").strip().title() 
            # Se comprueba que exista en el catálogo
            if titulo not in titulos: 
                print("El título ingresado no existe en nuestro catálogo.\n")
            # Se busca en índice del título ingresado
            else:
                indice = titulos.index(titulo) 
                
                print("1. Préstamo")
                print("2. Devolución")

                opcion = input("Ingrese la opción que desee realizar: ") # Se solicita al usuario que elija una opción
                # Préstamo
                if opcion == "1":
                    # Se comprueba que haya stock
                    if ejemplares[indice] == 0:
                        print("Lo sentimos. Este libro actualmente está fuera de stock, no es posible realizar un préstamo.\n")

                    else:
                        # Se solicita al usuario que ingrese la cantidad de ejemplares que quiere llevar
                        cantidadPrestamo = input("¿Cuántos ejemplares desea llevar? ")
                        # Se comprueba que haya ingresado un número
                        if cantidadPrestamo.isdigit():
                            # Se convierte a entero
                            cantidadPrestamo = int(cantidadPrestamo)
                            # Se comprueba que el número sea mayor que 0
                            if cantidadPrestamo <= 0:
                                print("El número ingresado no es válido. Debe ser mayor que 0.")
                            # Se comprueba que haya suficientes ejemplares
                            elif cantidadPrestamo > ejemplares[indice]:
                                print("Lamentamos informarle que no hay suficientes ejemplares para realizar el préstamo.\n")
                            else:
                                # Se descuenta la cantidad ingresada por el usuario en la lista de ejemplares
                                ejemplares[indice] -= cantidadPrestamo
                                print(f"Préstamo realizado con éxito. Título: {titulo}, {cantidadPrestamo} ejemplares prestados. ¡Gracias!\n")
                        # Mensaje de error si ingresa un formato inválido  
                        else:
                            print("Formato inválido. Debe ingresar un número entero mayor que 0.\n")

                # Devolución
                elif opcion == "2":
                    # Se solicita al usuario que ingrese la cantidad de ejemplares a devolver
                    cantidadDevolucion = input("¿Cuántos ejemplares desea devolver? ")
                    # Se comprueba que haya ingresado un número
                    if cantidadDevolucion.isdigit():
                        # Se convierte a entero
                        cantidadDevolucion = int(cantidadDevolucion)
                        # Se comprueba que sea mayor que 0
                        if cantidadDevolucion > 0:
                            # Se suma la cantidad de ejemplares a la lista y se muestra por pantalla
                            ejemplares[indice] += cantidadDevolucion
                            print(f"Devolución realizada con éxito. Título {titulo}, {cantidadDevolucion} ejemplares devueltos. ¡Gracias!\n")
                    # Si el número ingresado es menor o igual que 0, no es posible realizar la devolución
                        else:
                            print("La cantidad de ejemplares debe ser superior a 0.\n")
                    else:
                        print("Formato inválido. Debe ingresar un número entero mayor que 0.\n")
                # Opción no válida
                else:
                    print("La opción ingresada no es válida.\n")
                    
        # Salir            
        case "8":
            # Mensaje de despedida
            print("Gracias por visitar nuestra biblioteca escolar. ¡Hasta pronto!")
            # Salida del bucle
            break
        # Opción inválida
        case _:
            print("La opción ingresada no es válida.\n")
        

        

            

