
def pedir_numero(mensaje_solitud, mensaje_error):
    while True:
        try:
            numero = int(input(mensaje_solitud))
            return numero
        except ValueError:
            print(mensaje_error)

def validar_rut(rut):
    if "-" not in rut:
        print("El rut debe tener guión")
        return False
    
    return True

lista_integrantes = []
# Preguntar cantidad de integrantes
cantidad_integrantes = pedir_numero("Ingrese la cantidad de integrantes (mínimo 4): ", "La cantidad de integrantes debe ser un número entero")

if cantidad_integrantes >= 4:
    for i in range(cantidad_integrantes):
        rut = input("Ingrese su RUT: ")
        if validar_rut(rut):
            nombre = input("Ingrese su nombre: ")
            cargo = input("Ingrese su cargo (Desarrollador, QA, Diseñador o DevOps): ")
            cargo_minus = cargo.lower()
            if cargo_minus == "desarrollador" or cargo_minus == "qa" or cargo_minus == "diseñador" or cargo_minus == "devops":
                años_experiencia = pedir_numero("Ingrese sus años de experiencia: ", "Los años de experiencia deben ser un número entero")
                if 0 <= años_experiencia <= 3:
                    seniority = "junior"
                elif 3 < años_experiencia <= 6:
                    seniority = "semi-senior"
                elif 6 < años_experiencia <= 10:
                    seniority = "senior"
                elif años_experiencia > 10:
                    seniority = "specialist"
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

    print("Integrantes ingresados:")
    print(lista_integrantes)