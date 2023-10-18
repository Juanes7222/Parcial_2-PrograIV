import re

regex_cedula = '^[0-9]{8,10}$'
regex_nombre = '^((\w+\s)*\w+){3,50}$'


def validar_cedula(cedula):
    if not re.search(regex_cedula, cedula):
        return False
    else:
        return True


def validad_nombre(nombre):
    if not re.search(regex_nombre, nombre):
        return False
    else:
        return True
