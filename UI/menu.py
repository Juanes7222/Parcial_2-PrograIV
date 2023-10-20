from .mensajes import show_header as header
from .mensajes import show_errors as show_error
from .validations import validate_cedula
from .validations import validate_name


def show_options():
    header("BIENVENIDO A NUESTRO NEGOCIO")
    print("1. Hacer nueva compra")
    print("2. Buscar cliente por cédula")
    print("3. Agregar un producto")
    print("4. Salir")
    print("\n")


def stock_product(product):
    while True:
        numeration = 1
        header("ARTÍCULOS A LA VENTA")
        for name, info in product.items():
            print(f"{numeration}. {name} ", end="")
            for arg, value in info.items():
                print(f"{arg}: {value}  ", end="")
            print("\n")
            numeration += 1
        command = int(input("\n¿Qué desea comprar?: "))
        if 0 < command <= len(product):
            return list(product)[command - 1]
        else:
            show_error(1)


def main_menu():
    while True:
        show_options()
        try:
            command = int(input("¿Qué desea hacer?: "))
            if command > 4 or command < 1:
                raise ValueError
            else:
                return command
        except ValueError:
            show_error(1)


def user_info_ingress():
    header("DATOS DE CLIENTE")
    while True:
        dni = input("\nIngrese la cédula (sin puntos, comas ni guiones): ")
        if validate_cedula(dni):
            return dni
        show_error(2)


def user_ingress_name():
    while True:
        name = input("\nNombre completo (mínimo 3 caracteres y máximo 50): ").lower()
        if validate_name(name):
            return name
        show_error(3)


def show_purchase_options(__case=1):
    while True:
        header("ARTÍCULOS A LA VENTA")
        print("1. Antibióticos")
        print("2. Fertilizantes")
        print("3. Control de plagas")
        message = "\n¿Qué desea comprar?: " if __case == 1 else "\n¿Qué desea agregar?: "
        command = int(input(message))
        if 1 <= command <= 3:
            return command
        show_error(1)


def get_params(params):
    header("Ingrese los valores")
    values = {}
    for param in params:
        value = input(f"{param}: ")
        values[param] = value
    return values


def show_info_products(products):
    for product in products:
        print(product, '\n')


def show_info_bills(bills):
    for number, bill in enumerate(bills, 1):
        header(f"FACTURA #{number} - Fecha: {bill.date}:")
        show_info_products(bill.objects)
        header(f"VALOR TOTAL: {bill.total_value()}")


def show_info_client(client):
    if isinstance(client, bool):
        show_error(4)
    else:
        header(f"BÚSQUEDA POR CÉDULA - CLIENTE: {client.name.title()}  CEDULA: {client.dni}")
        show_info_bills(client.bills)
