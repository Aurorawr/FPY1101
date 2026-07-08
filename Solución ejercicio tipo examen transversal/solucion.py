
# Crear los diccionarios con la información
peliculas = {
    # Nombre - género - director - formato (V-VHS, D-DVD o B-Bluray) - es estreno - distribuidora
    'P001': ['Matrix', 'ciencia ficcion', 'Hermanas Wachowski', 'V', False, 'Warner']
}
inventario = {
    # precio - cantidad de stock
    'P001': [1500, 3]
}

# Paso 2: definir esqueleto de funciones

# Pide una opción al usuario hasta que sea un número entero válido
# y lo retorna
def leer_entero(mensaje_solicitud, mensaje_error):
    while True:
        try:
            entero = int(input(mensaje_solicitud))
            return entero
        except ValueError:
            print(mensaje_error)

# Pide una opción al usuario. Debe ser un número entero entre 1 y 6
def leer_opcion():
    opcion = leer_entero("Seleccione una opción (1 a 6): ", "La opción debe ser un número entero.")
    if 1 <= opcion <= 6:
        return opcion
    else:
        print("La opción debe ser entre 1 y 6")
        return -1

# Busca las películas que tengan el formato ingresado, suma
# su cantidad de stock y la muestra por pantalla
def mostrar_stock(formato):
    # Definir acumulador de stock
    total_stock = 0
    # Recorrer los códigos de las películas con for-in
    for codigo in peliculas:
        # Acceder a la película por el código
        pelicula = peliculas[codigo]
        # Verificar si la película tiene el formato ingresado
        if pelicula[3] == formato.upper():
            # Acceder al inventario de la película
            inventario_pelicula = inventario[codigo]
            # Sumar el stock de ese inventario
            total_stock += inventario_pelicula[1]
    # Mostramos la información del stock por pantalla
    print("Stock total para el formato", formato, ":", total_stock)
    
# Busca las películas que tengan un precio entre precio_min y
# precio_max y las muestra por pantalla en el formato "Título--Código"
def buscar_por_precio(precio_min, precio_max):
    # Recorrer los códigos de las películas con for-in
    for codigo in inventario:
        # Acceder al inventario
        inventario_pelicula = inventario[codigo]
        # Verificamos que el precio esté entre precio_min y el precio_max
        if precio_min <= inventario_pelicula[0] <= precio_max:
            # Accedemos a la película por su código
            pelicula = peliculas[codigo]
            # Mostramos la información en el formato solicitado
            print(pelicula[0],"--",codigo)

# Busca si una película con el código ingresado existe, retornando
# True o False
def buscar_por_codigo(codigo):
    if codigo in peliculas:
        return True
    else:
        return False

# Busca la película con el código (usando la función buscar_por_codigo)
# y le actualizamos el precio por el precio_nuevo. Retonamos True si existe
# y False si no
def actualizar_precio_arriendo(codigo, precio_nuevo):
    # Buscamos si existe la película
    existe = buscar_por_codigo(codigo)
    if existe:
        # Accedemos al inventario de la película
        inventario_pelicula = inventario[codigo]
        # Actualizamos el precio
        inventario_pelicula[0] = precio_nuevo
        return True
    else:
        return False

# Agrega una película con todos sus datos al diccionario de peliculas,
# pero si el código existe, retornar False. Retornar True si no existía
# y después de agregarla.
def crear_pelicula(codigo, nombre, genero, director, formato, es_estreno, distribuidora, precio, cantidad):
    # Verificamos si la película existe
    existe = buscar_por_codigo(codigo)
    if existe:
        return False
    else:
        # Definimos un valor por defecto para el estreno
        es_estreno_boolean = False
        # Verificamos si el valor es el contrario
        if es_estreno.lower() == "s":
            es_estreno_boolean = True
        # Definimos la nueva película
        nueva_pelicula = [nombre, genero, director, formato.upper(), es_estreno_boolean, distribuidora]
        # Defininmos el nuevo inventario
        nuevo_inventario = [precio, cantidad]
        # Agregamos la película al diccionario de películas
        peliculas[codigo] = nueva_pelicula
        # Agregamos el inventario al diccionario de inventarios
        inventario[codigo] = nuevo_inventario
        return True

# Elimina la película con el código ingresado del diccionario de películas
def eliminar_por_codigo(codigo):
    # Borramos la película con el código del diccionario películas
    del peliculas[codigo]
    # Borramos la película con el código del diccionario inventario
    del inventario[codigo]

# Paso 3: crear esqueleto de funciones de validación

# Validar que el texto no esté vacío ni sea solo espacios
def validar_texto(texto):
    if len(texto.strip()) > 0:
        return True
    else:
        return False

# Validar que el formato sea solo V, D o B
def validar_formato(formato):
    # if formato.upper() == "V" or formato.upper() == "D" or formato.upper() == "B":
    if formato.upper() in ["V", "D", "B"]:
        return True
    else:
        return False

# Validar que estreno solo sea s o n
def validar_estreno(estreno):
    if estreno.lower() == "s" or estreno.lower() == "n":
        return True
    else:
        return False

# Paso 4: crear esqueleto de menú

mostrar_menu = True

while mostrar_menu:
    # Mostrar las opciones
    print("1- Copias por formato")
    print("2- Búsquedas por rango de precio")
    print("3- Actualizar precio de arriendo")
    print("4- Agregar película")
    print("5- Eliminar película")
    print("6- Salir")
    # Pedir opción al usuario
    opcion_usuario = leer_opcion()
    # Evaluar la opción con if-elif-else
    if opcion_usuario == 1:
        # Pedir formato
        formato_a_buscar = input("Ingrese el formato a buscar: ")
        # Usar la función mostrar_stock
        mostrar_stock(formato_a_buscar)
    elif opcion_usuario == 2:
        # Pedimos el rango de precio
        precio_minimo = leer_entero("Ingrese el precio mínimo: ", "El precio mínimo debe ser un número entero")
        precio_maximo = leer_entero("Ingrese el precio máximo: ", "El precio máximo debe ser un número entero")
        # Usar la función buscar_por_precio
        buscar_por_precio(precio_minimo, precio_maximo)
    elif opcion_usuario == 3:
        seguir_actualizando = True
        while seguir_actualizando:
            codigo = input("Ingrese el código de la película: ")
            nuevo_precio = leer_entero("Ingrese el nuevo precio: ", "El precio debe ser un número entero.")
            fue_actualizado = actualizar_precio_arriendo(codigo, nuevo_precio)
            if fue_actualizado == True:
                print("Precio actualizado")
            else:
                print("El código no existe")
            desea_repetir = input("¿Desea repetir? (SI o NO): ")
            if desea_repetir.lower() == "no":
                seguir_actualizando = False
    elif opcion_usuario == 4:
        codigo = input("Ingrese el código: ")
        titulo = input("Ingrese el título: ")
        if validar_texto(titulo) == False:
            print("Título no es válido")
            continue
        genero = input("Ingrese el género: ")
        if validar_texto(genero) == False:
            print("Género no es válido")
            continue
        director = input("Ingrese el director: ")
        if validar_texto(director) == False:
            print("Director no es válido")
            continue
        formato = input("Ingrese el formato: ")
        if validar_formato(formato) == False:
            print("Formato solo puede ser V para VHS, D para DVD o B para Bluray")
            continue
        estreno = input("Ingrese si es estreno: ")
        if validar_estreno(estreno) == False:
            print("Estreno solo puede ser s para SI o n para NO")
            continue
        distribuidora = input("Ingrese la distribuidora: ")
        if validar_texto(distribuidora) == False:
            print("Distribuidora no puede estar vacía ni tener solo espacios")
            continue
        precio = leer_entero("Ingrese un precio: ", "El precio debe ser un número entero")
        cantidad = leer_entero("Ingrese la cantidad: ", "La cantidad debe ser un número entero.")

        #Usar la función para crear película
        crear_pelicula(codigo, titulo, genero, director, formato, estreno, distribuidora, precio, cantidad)
    elif opcion_usuario == 5:
        codigo_a_eliminar = input("Ingrese el código de la película a eliminar: ")
        existe = buscar_por_codigo(codigo_a_eliminar)
        if existe:
            eliminar_por_codigo(codigo_a_eliminar)
            print("Película eliminada")
        else:
            print("No existe película con ese código")
    elif opcion_usuario == 6:
        print("Saliendo...")
        mostrar_menu = False

