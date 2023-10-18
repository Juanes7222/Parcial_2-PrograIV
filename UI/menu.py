import sys
import os
from mensajes import mostrar_encabezado as encabezado
from mensajes import mostrar_errores as mostrar_error
from validations import validar_cedula
from validations import validad_nombre


def mostrar_opciones():
    encabezado("BIENVENIDO A NUESTRO NEGOCIO")
    print("1. Hacer nueva compra")
    print("2. Buscar cliente por cédula")
    print("3. Salir")
    print("\n")


def menu_principal():
    mostrar_opciones()
    comando = str(input("¿Qué desea hacer?> "))
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
        if validar_cedula(cedula):
            print("esta bien")
        else:
            os.system("cls")
            mostrar_error(2)
            ingresar_info_usuario()
    else:
        os.system("cls")
        mostrar_error(3)
        ingresar_info_usuario()


def buscar_cliente():
    encabezado("BÚSQUEDA POR CÉDULA")
    print("\nIngrese el cédula del cliente sin puntos, comas ni guiones: ")
    cedula = input("\n  -> ")
    os.system("cls")
    if validar_cedula(cedula):
        print("Mostrar facturas disponibles")
    else:
        mostrar_error(2)
        buscar_cliente()


if __name__ == "__main__":
    menu_principal()

