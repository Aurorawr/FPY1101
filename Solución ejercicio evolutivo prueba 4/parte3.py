

def pedir_numero(mensaje_solitud, mensaje_error):
    while True:
        try:
            numero = int(input(mensaje_solitud))
            return numero
        except ValueError:
            print(mensaje_error)

def validar_rut(rut):
    return True

def mostrar_integrante(integrante):
    print("- RUT:", integrante["rut"])
    print("- Nombre:", integrante["nombre"])
    print("- Cargo:", integrante["cargo"])
    print("- Años de experiencia:", integrante["anios_experiencia"], "años")
    print("- Seniority:", integrante["seniority"])
    print("--------------------------------------------------------------")

def buscar_integrante_por_rut(rut_a_buscar, lista):
    for posicion_integrante in range(len(lista)):
        integrante = lista[posicion_integrante]
        if integrante["rut"] == rut_a_buscar:
            return posicion_integrante
        
    return -1

def definir_seniority(años_experiencia):
    if 0 <= años_experiencia <= 3:
        seniority = "junior"
    elif 3 < años_experiencia <= 6:
        seniority = "semi-senior"
    elif 6 < años_experiencia <= 10:
        seniority = "senior"
    elif años_experiencia > 10:
        seniority = "specialist"
    return seniority


lista_integrantes = []

mostrar_menu = True

while mostrar_menu:
    print("1- Agregar integrante")
    print("2- Ver integrantes")
    print("3- Ver integrante")
    print("4- Actualizar integrante")
    print("5- Eliminar integrante")
    print("6- Salir")

    opcion_usuario = input("Seleccione una opción: ")

    if opcion_usuario == "1":
        print("Crear integrante")
        rut = input("Ingrese su RUT: ")
        if validar_rut(rut):
            nombre = input("Ingrese su nombre: ")
            cargo = input("Ingrese su cargo (Desarrollador, QA, Diseñador o DevOps): ")
            cargo_minus = cargo.lower()
            if cargo_minus == "desarrollador" or cargo_minus == "qa" or cargo_minus == "diseñador" or cargo_minus == "devops":
                años_experiencia = pedir_numero("Ingrese sus años de experiencia: ", "Los años de experiencia deben ser un número entero")
                seniority = definir_seniority(años_experiencia)
                integrante = {
                    "rut": rut,
                    "nombre": nombre,
                    "cargo": cargo,
                    "anios_experiencia": años_experiencia,
                    "seniority": seniority,
                }
                lista_integrantes.append(integrante)
            else:
                print("El cargo solo puede ser Desarrollador, QA, Diseñador o DevOps")
        else:
            print("El RUT es inválido")
    elif opcion_usuario == "2":
        print("Ver integrantes")
        for integrante in lista_integrantes:
            mostrar_integrante(integrante)
    elif opcion_usuario == "3":
        print("Ver integrante")
        rut_a_buscar = input("Ingrese el RUT del usuario a ver: ")
        posicion_integrante = buscar_integrante_por_rut(rut_a_buscar, lista_integrantes)
        if posicion_integrante == -1:
            print("El integrante con ese RUT no fue encontrado")
        else:
            integrante = lista_integrantes[posicion_integrante]
            mostrar_integrante(integrante)
    elif opcion_usuario == "4":
        print("Actualizar integrante")
        rut_a_buscar = input("Ingrese el RUT del usuario a actualizar: ")
        posicion_integrante = buscar_integrante_por_rut(rut_a_buscar, lista_integrantes)
        if posicion_integrante == -1:
            print("El integrante con ese RUT no fue encontrado")
        else:
            cargo = input("Ingrese el nuevo cargo del integrante: ")
            años_experiencia = pedir_numero("Ingrese los nuevos años de experiencia: ", "Los años de experiencia debe ser un número entero")
            seniority = definir_seniority(años_experiencia)
            integrante = lista_integrantes[posicion_integrante]
            integrante["cargo"] = cargo
            integrante["anios_experiencia"] = años_experiencia
            integrante["seniority"] = seniority
    elif opcion_usuario == "5":
        print("Eliminar integrante")
        rut_a_buscar = input("Ingrese el RUT del usuario a eliminar: ")
        posicion_integrante = buscar_integrante_por_rut(rut_a_buscar, lista_integrantes)
        if posicion_integrante == -1:
            print("El integrante con ese RUT no fue encontrado")
        else:
            lista_integrantes.pop(posicion_integrante)
            print("El integrante fue borrado")
    elif opcion_usuario == "6":
        print("Saliendo...")
        mostrar_menu = False
    else:
        print("Opción inválida")