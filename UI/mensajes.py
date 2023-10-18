def mostrar_encabezado(mensaje):
    encabezado = "+"
    longitud = len(mensaje)
    for contador in range(1, longitud + 3):
        encabezado += "-"
    encabezado += "+"
    encabezado = encabezado + "\n| " + mensaje + " |\n" + encabezado
    print(encabezado)


def mostrar_errores(identificador):
    if identificador == 1:
        mostrar_encabezado(' -> ERROR: Comando inválido <- ')
    elif identificador == 2:
        mostrar_encabezado(' -> ERROR: El formato de la cédula es incorrecto <- ')
    elif identificador == 3:
        mostrar_encabezado(' -> ERROR: Formato de nombre inválido <- ')
