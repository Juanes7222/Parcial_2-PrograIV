import re

regex_cedula = '^[0-9]{8,10}$'
regex_name = '^((\w+\s)*\w+){3,50}$'


def validate_cedula(cedula):
    if not re.search(regex_cedula, cedula):
        return False
    else:
        return True


def validate_name(name):
    if not re.search(regex_name, name):
        return False
    else:
        return True
