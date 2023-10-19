import sys
from UI import menu
from CRUD.crud import (append_bill_client, append_client_list, append_product_bill, create_bill, create_product_antibiotic, 
                  create_product_fertilizer, create_product_pests, create_client, client_exists)

antibiotics = {"Oxitrat": {"dose": "400ml", "animal_type": "Bovino", "value": 114000}, 
               "Edo Benpropen": {"dose": "550ml", "animal_type": "Caprino", "value": 200000},
               "Aurotilmicosin": {"dose": "500ml", "animal_type": "Porcinos", "value": 150000}}

fertilizers = {"Sulfato amónico": {"ica": "AVH1239", "freq": "15 días", "value": 55000, "last_applic": "19/10/2023"},
               "Cloruro potásico": {"ica": "BZD6935", "freq": "30 días", "value": 70000, "last_applic": "15/10/2023"},
               "Superfosfato simple": {"ica": "PLT9531", "freq": "7 días", "value": 45000, "last_applic": "12/10/2023"}}

pests = {}

antibiotic_params = ["name", "dose", "animal_type", "value"]
fertilizer_params = ["ica", "name", "freq", "value", "last_applic"]
pests_params = ["ica", "name", "freq", "value", "grace_period"]

clients = []

def buy(client):
    bill = create_bill()    
    while True:
        command = menu.show_purchase_options()
        # os.system("cls")
        if command == 1:
            product = menu.stock_product(antibiotics)
            product_purchased = create_product_antibiotic(name=product, **antibiotics.get(product))
            # total_cost += product_purchased.value
        elif command == 2:
            product = menu.stock_product(fertilizers)
            product_purchased = create_product_fertilizer(name=product, **fertilizers.get(product))
        elif command == 3:
            product = menu.stock_product(pests)
            product_purchased = create_product_pests(name=product, **pests.get(product))
            
        append_product_bill(product_purchased, bill)
        command = input("\nPulsa N para salir o cualquier otra letra para continuar: ")
        if command.lower() == 'n':
            append_bill_client(client, bill)
            menu.header("FACTURACIÓN TERMINADA CON ÉXITO") 
            break
        
def norm_params(params):
    name = params.get("name")
    del params["name"]
    return name

def create_product():
    command = menu.show_purchase_options(2)
    if command == 1:
        params = menu.get_params(antibiotic_params)
        name = norm_params()
        antibiotics[name] = params
    elif command == 2:
        params = menu.get_params(fertilizer_params)
        name = norm_params(params)
        fertilizers[name] = params
    elif command == 3:
        params = menu.get_params(pests_params)
        name = norm_params(params)
        pests[name] = params
    
    
def main():
    while True:
        command = menu.main_menu()
        if command == 1:
            dni = menu.user_info_ingress()
            client = client_exists(dni, clients)
            if not client:
                name = menu.user_ingress_name()
                client = create_client(dni=dni, name=name)
                append_client_list(client, clients)
            buy(client)
        elif command == 2:
            dni = menu.user_info_ingress()
            client = client_exists(dni, clients)
            menu.show_info_client(client)
        elif command == 3:
            create_product()
        elif command == 4:
            sys.exist()
        print("\n\n")
        


if __name__ == "__main__":
    main()

