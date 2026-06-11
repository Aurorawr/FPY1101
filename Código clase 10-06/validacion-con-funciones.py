
# Función que pide un número entero y que no retorna hasta que
# se ingrese uno válido
def pedir_numero_entero(mensaje_solicitud, mensaje_error):
    while True:
        try:
            numero_pedido = int(input(mensaje_solicitud))
            # El return, al hacer que nos salgamos de la función,
            # ROMPE EL while
            return numero_pedido
        except ValueError:
            print(mensaje_error)

edad = pedir_numero_entero("Ingrese su edad en años: ", "Su edad debe ser un número entero válido")
estatura = pedir_numero_entero("Ingrese su estatura en cm: ",  "Su estatura debe ser un número entero válido")
print("Su edad es", edad)
print("Su estatura es", estatura)