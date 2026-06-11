
# Tipo 1: sin argumentos y sin retorno
def dividir1():
    a = 5
    b = 2
    print("El resultado es ", a/b)

# Tipo 2: sin argumento y con retorno
def dividir2():
    a = 5
    b = 2
    return a / b

# Tipo 3: con argumentos y sin retorno
def dividir3(a, b):
    print("El resultado es ", a/b)

# Tipo 4: con argumentos y con retorno
def dividir4(a, b):
    # En vez de validar esto cada vez que quiero dividir,
    # lo hago solo una vez en la función
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por 0"

dividir1()
print(dividir2())
dividir3(2837, 12)
print(dividir4(23376, 456))

a = float(input("Ingrese un número: "))
b = float(input("Ingrese otro número: "))

print("El resultado de la división es:", dividir4(a, b))
