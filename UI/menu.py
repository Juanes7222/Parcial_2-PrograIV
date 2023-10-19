import sys
import os
from mensajes import mostrar_encabezado as encabezado
from mensajes import mostrar_errores as mostrar_error
from validations import validar_cedula
from validations import validad_nombre
from CRUD.crud import *

antibioticos = {"Oxitrat": ["400ml", "Bovino", 114000], "Edo Benpropen": ["550ml", "Caprino", 200000],
                "Aurotilmicosin": ["500ml", "Porcinos", 150000]}

def mostrar_opciones():
    encabezado("BIENVENIDO A NUESTRO NEGOCIO")
    print("1. Hacer nueva compra")
    print("2. Buscar cliente por cédula")
    print("3. Salir")
    print("\n")


def stock_antibioticos():
    numeracion = 1
    for antibiotico_nombre, info in antibioticos.items():
        print(str(numeracion) + ". " + str(antibiotico_nombre) + " " + str(info[0]) + " - " + str(info[1]) +
              "/ Precio: $" + str(info[2]))
        numeracion += 1
    try:
        comando = int(input("\n¿Qué desea comprar?: "))
        if 0 < comando <= len(antibioticos):
            producto = list(antibioticos)[comando-1]
            antibiotico_creado = create_product_antibiotic(name=producto,
                                                           dose=antibioticos[producto][0],
                                                           animal_type=antibioticos[producto][1],
                                                           value=antibioticos[producto][2])
            return antibiotico_creado
        else:
            raise NameError
    except NameError:
        mostrar_error(1)
        stock_antibioticos()



def menu_principal():
    mostrar_opciones()
    comando = str(input("¿Qué desea hacer?: "))
    os.system("cls")
    if comando == '1':
        ingresar_info_usuario()
    elif comando == '2':
        buscar_cliente()
    elif comando == '3':
        encabezado("HASTA PRONTO")
        sys.exit()
    else:
        mostrar_error(1)
    menu_principal()


def ingresar_info_usuario():
    encabezado("DATOS DE CLIENTE")
    nombre = input("\nNombre completo (mínimo 3 caracteres y máximo 50): ").lower()
    if validad_nombre(nombre):
        cedula = input("\nIngrese la cédula (sin puntos, comas ni guiones): ")
        os.system("cls")
        if validar_cedula(cedula):
            cliente = create_client(nombre, cedula)
            factura = realizar_compra()
            cliente.check_in(factura)
            encabezado("FACTURACIÓN TERMINADA CON ÉXITO")
        else:
            mostrar_error(2)
            ingresar_info_usuario()
    else:
        os.system("cls")
        mostrar_error(3)
        ingresar_info_usuario()


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
    menu_principal()
