import sys
import os
from mensajes import mostrar_encabezado as encabezado
from mensajes import mostrar_errores as mostrar_error
from validations import validar_cedula
from validations import validad_nombre
from CRUD.crud import append_bill_client, append_client_list, append_product_bill, create_bill, create_product_antibiotic, create_product_fertilizer, create_product_pests, create_client, client_exists

antibiotics = {"Oxitrat": ["400ml", "Bovino", 114000], "Edo Benpropen": ["550ml", "Caprino", 200000],
                "Aurotilmicosin": ["500ml", "Porcinos", 150000]}

def show_options():
    encabezado("BIENVENIDO A NUESTRO NEGOCIO")
    print("1. Hacer nueva compra")
    print("2. Buscar cliente por cédula")
    print("3. Salir")
    print("\n")


def stock_antibioticos():
    numeration = 1
    for antibiotic_name, info in antibiotics.items():
        # print(str(numeration) + ". " + str(antibiotic_name) + " " + str(info[0]) + " - " + str(info[1]) +
            #   "/ Precio: $" + str(info[2]))
        #Otra manera de presentar la informacion, las f-strings, muy utiles
        print(f"{numeration}. {antibiotic_name} {info[0]} - {info[1]}/ Precio: ${info[2]}")
        numeration += 1
    while True:
        command = int(input("\n¿Qué desea comprar?: "))
        if 0 < command <= len(antibiotics):
            product = list(antibiotics)[command-1]
            created_antibiotic = create_product_antibiotic(name=product,
                                                        dose=antibiotics[product][0],
                                                        animal_type=antibiotics[product][1],
                                                        value=antibiotics[product][2])
            return created_antibiotic
        else:
            mostrar_error(1)



def main_menu():
    show_options()
    command = str(input("¿Qué desea hacer?: "))
    os.system("cls")
    if command == '1':
        user_info_ingress()
    elif command == '2':
        buscar_cliente()
    elif command == '3':
        encabezado("HASTA PRONTO")
        sys.exit()
    else:
        mostrar_error(1)
    main_menu()


def user_info_ingress():
    encabezado("DATOS DE CLIENTE")
    name = input("\nNombre completo (mínimo 3 caracteres y máximo 50): ").lower()
    if validad_nombre(name):
        dni = input("\nIngrese la cédula (sin puntos, comas ni guiones): ")
        os.system("cls")
        if validar_cedula(dni):
            client = create_client(name, dni)
            bill = realizar_compra()
            client.check_in(bill)
            encabezado("FACTURACIÓN TERMINADA CON ÉXITO")
        else:
            mostrar_error(2)
            user_info_ingress()
    else:
        os.system("cls")
        mostrar_error(3)
        user_info_ingress()


def realizar_compra():
    verificador = True
    total_compra = 0
    factura = create_bill()
    while verificador:
        encabezado("ARTÍCULOS A LA VENTA")
        print("Total = " + str(total_compra))
        print("1. Antibióticos")
        print("2. Productos de control")
        comando = str(input("\n¿Qué desea comprar?: "))
        os.system("cls")
        if comando == '1':
            antibiotico_comprado = stock_antibioticos()
            total_compra += antibiotico_comprado.value
            factura.check_in(antibiotico_comprado)
            os.system("cls")
            print("Total = " + str(total_compra))
            comando = input("\nPulsa N para salir o cualquier otra letra para continuar: ")
            if comando.lower() == 'n':
                verificador = False
            os.system("cls")
        elif comando == '2':
            print("PENDIENTE")
        else:
            mostrar_error(1)
            realizar_compra()
    return factura


def buscar_cliente():
    encabezado("BÚSQUEDA POR CÉDULA")
    print("\nIngrese el cédula del cliente sin puntos, comas ni guiones: ")
    cedula = input("\n  -> ")
    os.system("cls")
    if validar_cedula(cedula):
        print("PENDIENTE")
    else:
        mostrar_error(2)
        buscar_cliente()


if __name__ == "__main__":
    main_menu()
