
# Primero: definimos las funciones solicitadas

"""
Busca una noticia en la lista de noticias cuyo título sea el texto ingresado o que su
contenido incluya el texto ingresado.
Retorna la posición de esta noticia en la lista, o -1 si no la encuentra.
"""
def buscar_noticia(texto, lista_noticias):
    # Recorremos las posiciones de la lista usando for-in.
    # También se puede usar while
    for posicion_noticia in range(len(lista_noticias)):
        # Obtenemos la noticia en esa posición
        noticia = lista_noticias[posicion_noticia]
        # Preguntamos si el título de la noticia es igual al
        # texto mandado o si este está presente en el contenido
        if noticia["titulo"] == texto or texto in noticia["contenido"]:
            # Si hay match, retornamos la posición de esta noticia
            return posicion_noticia
    # Si recorrí todas las posiciones y en ninguna noticia hizo match, entonces
    # no existe una noticia con ese título o contenido y retornamos -1
    return -1

"""
Muestra por pantalla la noticia de forma amigable para el usuario, imprimiendo por
pantalla cada dato de la noticia por separado.
"""
def mostrar_noticia(noticia):
    print("----------------------------------------------------------")
    print(noticia["titulo"].upper())
    print()
    print("Creada por:", noticia["creador"])
    print()
    print(noticia["contenido"])
    print()
    print(noticia["fecha_creacion"])
    print()

"""
Pide al usuario una fecha hasta que se ingrese una fecha correcta, validando que el
contenido cumpla con el formato dd-mm-aaaa. Pista: usar split.
"""
def pedir_fecha():
    # Haremos esta función de manera similar a las que hemos hecho antes para pedir números
    # Primero, usamos un bucle infinito
    while True:
        # Esta vez no usamos try/except porque no hay error de input.
        fecha = input("Ingrese la fecha (formato dd-mm-aaaa): ")
        # Separamos un string por guión. Esto generará una lista
        fecha_separada = fecha.split("-")
        # Una fecha separada válida tendrá tres valores: una para el día, otra para el mes y otra
        # para el año. Validamos esto
        if len(fecha_separada) == 3:
            # Como es válida, accedemos a los valores de la fecha por posición
            dia = fecha_separada[0]
            mes = fecha_separada[1]
            año = fecha_separada[2]
            # Hacemos la validación de largo y tipo de dato para cada valor
            dia_es_valido = dia.isdigit() and len(dia) == 2 and 1 <= int(dia) <= 31
            mes_es_valido = mes.isdigit() and len(mes) == 2 and 1 <= int(mes) <= 12
            año_es_valido = año.isdigit() and len(año) == 4
            if dia_es_valido and mes_es_valido and año_es_valido:
                # Si se cumple, es una fecha válida y la retornamos, rompiendo el ciclo
                print("La fecha ingresada es válida")
                return fecha
            else:
                #Si no, entonces la fecha no es válida y mostramos un mensaje con las condiciones
                print("La fecha no tiene valores válidos para día, mes y/o año")
        else:
            # Si no se cumple, mostramos que no se ingresó el formato correcto para la fecha
            print("La fecha ingresada debe tener formato válido dd-mm-aaaa")

# Una vez creadas las funciones, partimos con la lógica del programa

# Definimos una lista vacía que irá guardando las noticias creadas

lista_noticias = []

# Creamos la estructura básica de un menú
mostrar_menu = True

while mostrar_menu:
    # Mostramos las opciones del menú
    print("1- Agregar noticia")
    print("2- Buscar noticia")
    print("3- Ver catálogo de noticias")
    print("4- Borrar noticia")
    print("5- Salir")
    # Pedimos una opción al usuario
    opcion_usuario = input("Ingrese una opción: ")
    # Manejamos las opciones con if-elif-else
    if opcion_usuario == "1":
        print("Agregar noticia")
        # Pedimos el título de la noticia
        titulo_noticia = input("Ingrese el título de la noticia: ")
        # Validamos que el largo no sea mayor a 50
        if len(titulo_noticia) > 50:
            print("El largo del título de la noticia no puede superar los 50 caracteres")
        else:
            # Si no lo es, pedimos los demás datos
            contenido_noticia = input("Ingrese el contenido de la noticia: ")
            creador_noticia = input("Ingrese el creador de la noticia: ")
            # Usamos la función pedir_fecha para pedir la fecha de creación
            fecha_noticia = pedir_fecha()
            # Creamos el diccionario con los datos de la noticia
            noticia = {
                "titulo": titulo_noticia,
                "contenido": contenido_noticia,
                "creador": creador_noticia,
                "fecha_creacion": fecha_noticia,
            }
            # Agregamos la noticia a la lista
            lista_noticias.append(noticia)
    elif opcion_usuario == "2":
        print("Buscar noticia")
        # Pedimos el texto para buscar
        texto_busqueda = input("Ingrese título o parte del contenido de la noticia: ")
        # La buscamos usando la función buscar_noticia
        posicion_noticia = buscar_noticia(texto_busqueda, lista_noticias)
        # Validamos que la posición no sea -1
        if posicion_noticia != -1:
            # Si es así, la noticia existe y la mostramos con la función mostrar_noticia
            mostrar_noticia(lista_noticias[posicion_noticia])
        else:
            # Si es -1, la noticia no fue encontrada
            print("No encontramos una noticia que coincida con la búsqueda")
    elif opcion_usuario == "3":
        print("Ver catálogo de noticias")
        # Definimos un correlativo para las noticias
        correlativo = 1
        # Recorremos todas las noticias usando for-in
        for noticia in lista_noticias:
            # Mostramos correlativo y título de noticia
            print("#", correlativo, "-", noticia["titulo"])
            # Aumentamos en 1 el correlativo
            correlativo += 1
    elif opcion_usuario == "4":
        print("Borrar noticia")
        # Pedimos el texto para buscar
        texto_busqueda = input("Ingrese título o parte del contenido de la noticia a borrar: ")
        # La buscamos usando la función buscar_noticia
        posicion_noticia = buscar_noticia(texto_busqueda, lista_noticias)
        # Validamos que la posición no sea -1
        if posicion_noticia != -1:
            # Si no lo es, la noticia y existe y se la mostramos al usuario
            print("Hemos encontrado esta noticia:")
            mostrar_noticia(lista_noticias[posicion_noticia])
            # Pedimos confirmación de borrado al usuario
            confirmacion_borrado = input("Ingrese SI para confirmar su eliminación: ")
            # Validamos si se ingresó si o sus variaciones normalizando a minúscula
            if confirmacion_borrado.lower() == "si":
                # Si es así, borramos la noticia por posición
                lista_noticias.pop(posicion_noticia)
                print("La noticia se ha borrado")
            else:
                # Si no, decimos quie no se borró
                print("Ha decidido no borrar la noticia")
        else:
            # Si es -1, la noticia no fue encontrada
            print("No encontramos una noticia que coincida con la búsqueda")
    elif opcion_usuario == "5":
        print("Saliendo...")
        mostrar_menu = False
    else:
        print("Opción inválida")
