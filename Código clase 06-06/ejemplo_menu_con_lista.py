
# Menú con las siguientes opciones:
#   1- Agregar persona a una lista, sin repetir
#   2- Quitar persona
#   3- Ver lista de personas
#   4- Salir

# Definir la lista de personas
listaPersonas = []
# Definir estructura básica de menú
mostrarMenu = True
while mostrarMenu:
    # Mostrar opciones al usuario
    print("1- Agregar persona")
    print("2- Quitar persona")
    print("3- Ver personas")
    print("4- Salir")
    # Pedir opción al usuario
    opcion_usuario = input("Ingrese una opción: ")
    # Validar opción con if/else
    if opcion_usuario == "1":
        print("Agregar persona")
        # Pedir el nombre de la persona a agregar
        nombre_persona = input("Ingrese el nombre de la persona: ")
        # Preguntamos si la persona existe en la lista
        if nombre_persona in listaPersonas:
            # Si está, decimos que no se puede agregar
            print(nombre_persona, "ya se encuentra en la lista")
        else:
            # Si no está, la agregamos a la lista
            listaPersonas.append(nombre_persona)
            print(nombre_persona, "agregado/a")
    elif opcion_usuario == "2":
        print("Quitar persona")
        # Pedimos el nombre de la persona a eliminar
        nombre_persona = input("Ingrese el nombre de la persona: ")
        # Intentamos borrar a la persona. Como puede fallar, usamos try/except
        try:
            listaPersonas.remove(nombre_persona)
            print(nombre_persona, "eliminado/a")
        except ValueError:
            print("No se pudo borrar persona porque no existe en la lista.")
    elif opcion_usuario == "3":
        print("Mostrar personas")
        print("Personas registradas hasta ahora:", listaPersonas)
    elif opcion_usuario == "4":
        print("Saliendo...")
        mostrarMenu = False
    else:
        print("Ingrese una opción válida (1, 2, 3 o 4)")

print("Personas registradas:", listaPersonas)
