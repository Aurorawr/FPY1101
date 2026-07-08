
entregas = {
  # código: [título, asignatura, alumno, tipo ('P' - Prueba), 'E' - Ensayo) o 'T' - Taller), es grupal, profesor]
  'T001': ['Ecuaciones', 'matematicas', 'Ana Silva', 'T', False, 'Luis Gomez'],
  'T002': ['Revolución Francesa', 'historia', 'Grupo 3', 'E', True, 'Marta Ruiz'],
}

evaluacion = {
  # código: [puntaje máximo, días de atraso]
  'T001': [100, 0],
  'T002': [70, 3],
}

# Pide un número entero
def leer_entero(mensaje_solicitud, mensaje_error):
  return

# Pide opción al usuario
def leer_opcion():
  return

# Muestra el total de días de atraso de una asignatura
def mostrar_dias_atraso(asignatura):
  return

# Muestra las entregas que tengan un puntaje entre el min y el max ingresado
def buscar_por_rango_puntajes(puntaje_min, puntaje_max):
  return

# Verificar si la entrega con el código ingresado existe
def buscar_por_codigo(codigo):
  return

# Actualiza los días de atraso de la entrega con el código ingresado
def actualizar_dias_atraso(codigo, dias_atraso_nuevos):
  return

# Crea una entrega
def crear_entrega(codigo, titulo, asignatura, alumno, tipo, es_grupal, profesor, puntaje_maximo, dias_atraso):
  return

# Elimina una entrega por código
def eliminar_por_codigo(codigo):
  return

# Texto no vacío ni solo espacios
def validar_texto(texto):
  return

# Tipo debe ser P, T o E
def validar_tipo(tipo):
  return

# es_grupo debe ser s o n
def validar_es_grupo(es_grupo):
  return

# Debe ser mayor a 0
def validar_nota_max(nota_max):
  return

# Debe ser igual o mayor a 0
def validar_dias_atraso(dias_atraso):
  return

mostrar_menu = True

while mostrar_menu:
  print("1- Días de atraso por asignatura")
  print("2- Búsqueda por rango de nota máxima")
  print("3- Actualizar días de atraso")
  print("4- Registrar nueva entrega")
  print("5- Eliminar entrega")
  print("6- Salir")

  opcion = leer_opcion()

  if opcion == 1:
    asignatura_a_buscar = input("Ingrese la asignatura: ")
    mostrar_dias_atraso(asignatura_a_buscar)
  elif opcion == 2:
    puntaje_min = leer_entero("Ingrese el puntaje mínimo: ", "El puntaje mínimo debe ser un número entero.")
    puntaje_max = leer_entero("Ingrese el puntaje máximo: ", "El puntaje máximo debe ser un número entero.")
    buscar_por_rango_puntajes(puntaje_min, puntaje_max)
  elif opcion == 3:
    reintentar_actualizacion = True
    while reintentar_actualizacion:
      codigo_a_actualizar = input("Ingrese el código que desea actualizar: ")
      existe = buscar_por_codigo(codigo_a_actualizar)
      if existe:
        nuevos_dias_atraso = leer_entero("Ingrese los nuevos días de atraso: ", "Los días de atraso debe ser un número entero")
        actualizar_dias_atraso(codigo_a_actualizar, nuevos_dias_atraso)
      else:
        print("No existe una entrega con ese código")
      desea_repetir = input("¿Desea repetir? (SI o NO): ")
      if desea_repetir.strip().upper() == "NO":
        reintentar_actualizacion = False
  elif opcion == 4:
    # codigo, titulo, asignatura, alumno, tipo, es_grupal, profesor, puntaje_maximo, dias_atraso
    codigo = input("Ingrese el código: ")
    if validar_texto(codigo) == False:
      print("Código no puede ser vacío ni solo espacios")
      continue
    if buscar_por_codigo(codigo) == True:
      print("Ya existe una entrega con ese código")
      continue
    titulo = input("Ingrese el título: ")
    if validar_texto(titulo) == False:
      print("Título no puede ser vacío ni solo espacios")
      continue
    asignatura = input("Ingrese la asignatura: ")
    if validar_texto(asignatura) == False:
      print("Asignatura no puede ser vacío ni solo espacios")
      continue
    alumno = input("Ingrese el alumno: ")
    if validar_texto(alumno) == False:
      print("Alumno no puede ser vacío ni solo espacios")
      continue
    tipo = input("Ingrese el tipo (P, T o E): ")
    if validar_tipo(tipo) == False:
      print("El tipo solo puede ser P, T o E")
      continue
    es_grupal = input("Ingrese si es grupal (s para SI, n para NO): ")
    if validar_es_grupo(es_grupal) == False:
      print("Solo puede ingresar s o n")
      continue
    profesor = input("Ingrese el profesor: ")
    if validar_texto(profesor) == False:
      print("Profesor no puede ser vacío ni solo espacios")
      continue
    puntaje_max = leer_entero("Ingrese el puntaje máximo: ", "El puntaje máximo solo pueden ser enteros.")
    if validar_nota_max(puntaje_max) == False:
      print("El puntaje debe ser un número entero mayor a 0")
      continue
    dias_atraso = leer_entero("Ingrese los días de atraso: ", "Los días de atraso solo pueden ser enteros.")
    if validar_dias_atraso(dias_atraso) == False:
      print("Los días de atraso deben ser un número entero mayor o igual a 0")
      continue
    crear_entrega(codigo, titulo, asignatura, alumno, tipo, es_grupal, profesor, puntaje_max, dias_atraso)
  elif opcion == 5:
    codigo_a_eliminar = input("Ingrese el código que desea eliminar: ")
    existe = buscar_por_codigo(codigo_a_eliminar)
    if existe:
      eliminar_por_codigo(codigo_a_eliminar)
      print("Entrega eliminada con éxito")
    else:
      print("No existe una entrega con ese código")
  elif opcion == 6:
    print("Saliendo...")
    mostrar_menu = False

