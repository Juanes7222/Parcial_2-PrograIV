def show_header(message):
    header = "+"
    message_lenght = len(message)
    for counter in range(1, message_lenght + 3):
        header += "-"
    header += "+"
    header = header + "\n| " + message + " |\n" + header
    print(header)


def show_errors(identifier):
    if identifier == 1:
        show_header(' -> ERROR: Comando inválido <- ')
    elif identifier == 2:
        show_header(' -> ERROR: El formato de la cédula es incorrecto <- ')
    elif identifier == 3:
        show_header(' -> ERROR: Formato de nombre inválido <- ')
    elif identifier == 4:
        show_header(' -> ERROR: Cliente no existe <- ')
