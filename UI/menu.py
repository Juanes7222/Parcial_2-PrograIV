import sys
import os
from mensajes import show_header as header
from mensajes import show_errors as show_error
from validations import validate_cedula
from validations import validate_name
from CRUD.crud import (append_bill_client, append_client_list, append_product_bill, create_bill,
                       create_product_antibiotic, create_product_fertilizer, create_product_pests, create_client,
                       client_exists)

antibiotics = {"Oxitrat": ["400ml", "Bovino", 114000], "Edo Benpropen": ["550ml", "Caprino", 200000],
               "Aurotilmicosin": ["500ml", "Porcinos", 150000]}


def show_options():
    header("BIENVENIDO A NUESTRO NEGOCIO")
    print("1. Hacer nueva compra")
    print("2. Buscar cliente por cédula")
    print("3. Salir")
    print("\n")


def stock_antibioticos():
    checker = True
    while checker:
        numeration = 1
        for antibiotic_name, info in antibiotics.items():
            print(f"{numeration}. {antibiotic_name} {info[0]} - {info[1]}/ Precio: ${info[2]}")
            numeration += 1
        command = int(input("\n¿Qué desea comprar?: "))
        if 0 < command <= len(antibiotics):
            product = list(antibiotics)[command - 1]
            created_antibiotic = create_product_antibiotic(name=product,
                                                           dose=antibiotics[product][0],
                                                           animal_type=antibiotics[product][1],
                                                           value=antibiotics[product][2])
            checker = False
        else:
            show_error(1)
    return created_antibiotic


def main_menu():
    show_options()
    command = str(input("¿Qué desea hacer?: "))
    os.system("cls")
    if command == '1':
        user_info_ingress()
    elif command == '2':
        search_client()
    elif command == '3':
        header("HASTA PRONTO")
        sys.exit()
    else:
        show_error(1)
    main_menu()


def user_info_ingress():
    header("DATOS DE CLIENTE")
    name = input("\nNombre completo (mínimo 3 caracteres y máximo 50): ").lower()
    if validate_name(name):
        dni = input("\nIngrese la cédula (sin puntos, comas ni guiones): ")
        os.system("cls")
        if validate_cedula(dni):
            client = create_client(name, dni)
            bill = make_purchase()
            append_bill_client(client, bill)
            header("FACTURACIÓN TERMINADA CON ÉXITO")
        else:
            show_error(2)
            user_info_ingress()
    else:
        os.system("cls")
        show_error(3)
        user_info_ingress()


def make_purchase():
    checker = True
    total_cost = 0
    bill = create_bill()
    while checker:
        header("ARTÍCULOS A LA VENTA")
        print("Total = " + str(total_cost))
        print("1. Antibióticos")
        print("2. Productos de control")
        command = str(input("\n¿Qué desea comprar?: "))
        os.system("cls")
        if command == '1':
            antibiotic_purchased = stock_antibioticos()
            total_cost += antibiotic_purchased.value
            append_product_bill(antibiotic_purchased, bill)
            os.system("cls")
            print("Total = " + str(total_cost))
            command = input("\nPulsa N para salir o cualquier otra letra para continuar: ")
            if command.lower() == 'n':
                checker = False
                os.system("cls")
        elif command == '2':
            print("PENDIENTE")
        else:
            show_error(1)
            make_purchase()
    return bill


def search_client():
    header("BÚSQUEDA POR CÉDULA")
    print("\nIngrese el cédula del cliente sin puntos, comas ni guiones: ")
    cedula = input("\n  -> ")
    os.system("cls")
    if validate_cedula(cedula):
        print("PENDIENTE")
    else:
        show_error(2)
        search_client()


if __name__ == "__main__":
    main_menu()
