
# Primero: definimos las funciones solicitadas

"""
Busca un contacto en la lista de contactos cuyo nombre sea el nombre a buscar.
Retorna la posición de ese contacto en la lista, o -1 si no lo encuentra.
"""
def buscar_contacto(nombre_a_buscar, lista_contactos):
    # Recorremos las posiciones de la lista usando for-in.
    # También se puede usar while
    for posicion_contacto in range(len(lista_contactos)):
        # Obtenemos el contacto en esa posición
        contacto = lista_contactos[posicion_contacto]
        # Preguntamos si el nombre del contacto es igual a nombre_a_buscar
        if contacto["nombre"] == nombre_a_buscar:
            # Si hay match, retornamos la posición de este contacto
            return posicion_contacto
    # Si recorrí todas las posiciones y en ningún contacto hizo match, entonces
    # no existe un contacto con ese nombre y retornamos -1
    return -1

"""
Muestra por pantalla el contacto de forma amigable para el usuario, imprimiendo por
pantalla cada dato por separado.
"""
def mostrar_contacto(contacto):
    print("----------------------------------------------------------")
    print("- Nombre:", contacto["nombre"].title())
    print()
    print("- Teléfono:", contacto["telefono"])
    print()
    print("- Correo:", contacto["correo"])
    print()

"""
Pide al usuario un correo hasta que ingrese uno válido (que contenga "@").
Retorna el correo válido.
"""
def pedir_correo():
    # Haremos esta función de manera similar a las que hemos hecho antes para pedir números
    # Primero, usamos un bucle infinito
    while True:
        # Esta vez no usamos try/except porque no hay error de input.
        correo = input("Ingrese el correo (debe tener @): ")
        # Validamos que tengan un @
        if '@' in correo:
            # Si lo tiene, es un correo válido y lo retornamos
            return correo
        else:
            # Si no lo tiene, lo indicamos al usuario y no rompemos el bucle para que siga preguntando
            print("El correo ingresado debe tener un @")

# Una vez creadas las funciones, partimos con la lógica del programa

# Definimos una lista vacía que irá guardando los contactos creados

lista_contactos = []

# Creamos la estructura básica de un menú
mostrar_menu = True

while mostrar_menu:
    # Mostramos las opciones del menú
    print("1- Agregar contacto")
    print("2- Buscar contacto")
    print("3- Ver todos los contactos")
    print("4- Borrar contacto")
    print("5- Salir")
    # Pedimos una opción al usuario
    opcion_usuario = input("Ingrese una opción: ")
    # Manejamos las opciones con if-elif-else
    if opcion_usuario == "1":
        print("Agregar contacto")
        # Pedimos el nombre del contacto
        nombre_contacto = input("Ingrese el nombre del contacto: ")
        # Validamos que el largo no sea mayor a 30
        if len(nombre_contacto) > 30:
            print("El largo del nombre del contacto no puede superar los 30 caracteres")
        else:
            # Si no lo es, pedimos los demás datos
            telefono_contacto = input("Ingrese el teléfono del contacto (de 8 dígitos): ")
            # Validamos que sea de largo 8 y números
            if telefono_contacto.isdigit() and len(telefono_contacto) == 8:
                # Si lo es, es válido y podemos continuar pidiendo datos
                correo_contacto = pedir_correo()
                # Creamos el diccionario con los datos del contacto
                contacto = {
                    "nombre": nombre_contacto,
                    "telefono": telefono_contacto,
                    "correo": correo_contacto,
                }
                # Agregamos el contacto a la lista
                lista_contactos.append(contacto)
            else:
                print("El teléfono debe ser un número de 8 dígitos")
    elif opcion_usuario == "2":
        print("Buscar contacto")
        # Pedimos el nombre a buscar
        nombre_a_buscar = input("Ingrese el nombre del contacto a buscar: ")
        # La buscamos usando la función buscar_contacto
        posicion_contacto = buscar_contacto(nombre_a_buscar, lista_contactos)
        # Validamos que la posición no sea -1
        if posicion_contacto != -1:
            # Si es así, el contacto existe y lo mostramos con la función mostrar_noticia
            mostrar_contacto(lista_contactos[posicion_contacto])
        else:
            # Si es -1, la el contacto no fue encontrada
            print("No encontramos un contacto con ese nombre")
    elif opcion_usuario == "3":
        print("Ver todos los contactos")
        # Definimos un correlativo para los contactos
        correlativo = 1
        # Recorremos todos los contactos usando for-in
        for contacto in lista_contactos:
            # Mostramos correlativo y título del contacto
            print("#", correlativo, "-", contacto["nombre"], ":", contacto["telefono"])
            # Aumentamos en 1 el correlativo
            correlativo += 1
    elif opcion_usuario == "4":
        print("Borrar contacto")
        # Pedimos el nombre a buscar
        nombre_a_buscar = input("Ingrese el nombre del contacto a buscar: ")
        # La buscamos usando la función buscar_contacto
        posicion_contacto = buscar_contacto(nombre_a_buscar, lista_contactos)
        # Validamos que la posición no sea -1
        if posicion_contacto != -1:
            # Si no lo es, el contacto existe y pedimos confirmación para borrarlo
            contacto = lista_contactos[posicion_contacto]
            confirmacion_borrado = input(f"¿Seguro que desea borrar a {contacto["nombre"]}?")
            # Validamos si se ingresó si o sus variaciones normalizando a minúscula
            if confirmacion_borrado.lower() == "si":
                # Si es así, borramos el contacto por posición
                lista_contactos.pop(posicion_contacto)
                print("El contacto se ha borrado")
            else:
                # Si no, decimos quie no se borró
                print("Ha decidido no borrar el contacto")
        else:
            # Si es -1, el contacto no fue encontrada
            print("No encontramos un contacto con ese nombre")
    elif opcion_usuario == "5":
        print("Saliendo...")
        mostrar_menu = False
    else:
        print("Opción inválida")
