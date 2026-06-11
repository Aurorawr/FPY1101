
# Crear un menú que permita calcular un promedio de notas ponderas.
# Las opciones de este serán:
#   1- Agregar nota con su ponderación. Esta debe ser agregada a una
#      o dos listas
#   2- Ver las notas actuales y sus ponderaciones
#   3- Salir
# Al salir, se debe mostrar la nota final, verificando que la
# suma de las ponderación sea 100%

def pedir_numero(mensaje_solicitud, mensaje_error):
    while True:
        try:
            numero = float(input(mensaje_solicitud))
            return numero
        except ValueError:
            print(mensaje_error)

# Crear la lista de datos
notas = []
# Crear variable para la suma de ponderaciones
total_ponderacion = 0

# Creamos while para el menú
mostrarMenu = True
while mostrarMenu:
    # Mostrar opciones
    print("1- Agregar nota")
    print("2- Ver notas actuales")
    print("3- Salir")
    # Pedir opción al usuario
    opcion_usuario = input("Ingrese una opción: ")
    # Validar con if-elif-else y hacer acciones
    if opcion_usuario == "1":
        print("Agregar nota")
        nota = pedir_numero("Ingrese la nota: ", "La nota debe ser un valor numérico")
        ponderacion = pedir_numero("Ingrese la ponderación (0 a 1): ", "La ponderación debe ser un valor numérico")
        datos_nota = {
            "nota": nota,
            "ponderacion": ponderacion
        }
        notas.append(datos_nota)
        total_ponderacion += ponderacion
    elif opcion_usuario == "2":
        print("Ver notas actuales")
        for datos_nota in notas:
            print("Nota: ", datos_nota["nota"], " - ponderación: ", datos_nota["ponderacion"])
    elif opcion_usuario == "3":
        print("Saliendo...")
        mostrarMenu = False
    else:
        print("Ingrese una opción válida (1, 2 o 3)")

# Preguntamos si la ponderación es 1 (100%)
if total_ponderacion == 1:
    # Si lo es, calculamos promedio
    promedio = 0
    # Usamos for para recorrer la lista de notas
    for datos_nota in notas:
        promedio += datos_nota["nota"] * datos_nota["ponderacion"]
    print("El promedio es:", promedio)
else:
    # Si no lo es, mostrar que no es correcto calcular el promedio
    print("No se puede calcular el promedio porque la ponderación total es", total_ponderacion)
