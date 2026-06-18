"""
Cree un programa en Python que permita a un usuario calcular la comisión que obtendrá un
vendedor en base a las ventas realizadas durante el día. Para esto, se le pedirá al usuario
la cantidad de ventas realizadas, y por cada una de ellas, se preguntará por el precio y el
tipo del producto para calcular la comisión obtenida y el total vendido.

Para el cálculo de la comisión, cree y use una función que reciba el precio de un producto y
el tipo de este como argumentos, y en base a esto, calcule la comisión que se le da al
vendedor de este producto en base a los siguientes tipos:
● Alimentos: 5% de comisión
● Aseo: 8% de comisión
● Ropa: 10% de comisión
● Tecnología: 17% de comisión.
● Cualquier otro: 0% de comisión
Por ejemplo: si el precio del producto es 10000 y su tipo es “Aseo”, se calcula el 8% de
10000 = 10000 * 0.08 = 800.
Una vez calculadas todas las comisiones, se debe mostrar al usuario la suma de estas y el
total vendido.
"""

def calcular_comision(precio_producto, tipo_producto):
    porcentaje_comision = 0
     # Pasar a minúscula y quitar espacios para comparar
    tipo_producto_normalizado = tipo_producto.lower().strip()
    if tipo_producto_normalizado == "alimentos":
        porcentaje_comision = 0.05
    elif tipo_producto_normalizado == "aseo":
        porcentaje_comision = 0.08
    elif tipo_producto_normalizado == "ropa":
        porcentaje_comision = 0.1
    elif tipo_producto_normalizado == "tecnología":
        porcentaje_comision = 0.17
    # Calculamos y retornamos la comisión
    return precio_producto * porcentaje_comision

# Función para pedir un número entero correcto
def pedir_numero_entero(mensaje_solicitud, mensaje_error):
    while True:
        try:
            # Pedimos y convertimos un número
            numero = int(input(mensaje_solicitud))
            # Si no falla, el número es correcto, así que lo retornamos
            return numero
        except ValueError:
            # Si falla, mostramos mensaje de error
            print(mensaje_error)

# Entrada: Cantidad de ventas

cantidad_ventas = pedir_numero_entero("Ingrese la cantidad de ventas: ", "La cantidad de ventas debe ser un número entero")
# Definir el total de comisión y de venta
total_comision = 0
total_venta = 0

# Proceso: preguntar datos por cada venta y calcular comisión

for i in range(cantidad_ventas):
    precio_producto = pedir_numero_entero("Ingrese el precio del producto: ", "El precio debe ser un número entero.")
    tipo_producto = input("Ingrese el tipo del producto: ")
    comision_producto = calcular_comision(precio_producto, tipo_producto)
    total_comision += comision_producto
    total_venta += precio_producto

# Salida: mostrar total de comisión y total de venta
print("Total de ventas: $", total_venta)
print("Total de comisión: $", total_comision)
