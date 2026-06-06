
lista = []

# CRUD lista (Create, Read, Update y Delete)
# Crear (insertar)

lista.append("Hola buenas")
print(lista)
lista.append(12)
lista.append("Chao chao")
print(lista)

# Read
# Acceder al tercer elemento (posición 2) de la lista
print(lista[2])

# Acceder al quinto elemento. Como no existe,
# produce IndexError y se debe validar con try/except
try:
    print(lista[4])
except IndexError:
    print(f"No se puede acceder a la quinta posición. Largo de lista: {len(lista)}")
# También se puede validar con if
if len(lista) >= 5:
    print(lista[4])
else:
    print(f"No se puede acceder a la quinta posición. Largo de lista: {len(lista)}")

# Update (actualizar)

# Actualizamos el valor de la posición 1
lista[1] = "Saludos cordiales"
print(lista)

# Delete

# Borramos por coincidencia el elemento con valor "Hola buenas"
lista.remove("Chao chao")
print(lista)

# Borramos el primer elemento
lista.pop(0)
print(lista)

# Tanto remove como pop puede fallar si se les entrega
# un elemento o posición respectivamente que no
# exista en la lista. Manejar con try/except
try:
    lista.remove("No existe")
except ValueError:
    print("Elemento no existe. No se puede borrar.")

# También lo podemos validar con if/else buscando la presencia
# en la lista
if "No existe" in lista: # Preguntamos si "No existe" está en la lista
    # Si está, lo podemos borrar
    lista.remove("No existe")
else:
    # Si no está, no se puede borrar
    print("Elemento no existe. No se puede borrar.")

try:
    lista.pop(5)
except IndexError:
    print("Elemento no se puede borrar porque es mayor al largo.")

# pop se puede hacer co  if/else, igual que al acceder a una posición
if len(lista) >= 6:
    lista.pop(5)
else:
    print("Elemento no se puede borrar porque es mayor al largo.")

diccionario = {}

# CRUD diccionario (Create, Read, Update y Delete)
# Crear (insertar)

diccionario["nombre"] = "Rubén"
print(diccionario)
diccionario["apellido"] = "Baez"
diccionario["edad"] = 37
diccionario["esta_casado"] = False
print(diccionario)

# Read
print(diccionario["nombre"])
print(diccionario["edad"])
# Habrá errores cuando intento acceder a una clave
# que no existe en el diccionario. Validar con
# try/except
try:
    print(diccionario["sueldo"])
except KeyError:
    print("Clave no existe en el diccionario")

# Esto también lo puedo hacer validando la presenci
# del elemento con in y if/else
if "sueldo" in diccionario: # revisan si "sueldo" está como clave en el diccionario
    print(diccionario["sueldo"])
else:
    print("Clave no existe en el diccionario")

# Update
# La actualización se hace igual al insert, pero
# si la clave ya existe en el diccionario, se actualiza

diccionario["esta_casado"] = True
print(diccionario)
diccionario["edad"] += 1
print(diccionario)

# Delete

# Borramos la clave "esta_casado" del diccionario
del diccionario["esta_casado"]
print(diccionario)
