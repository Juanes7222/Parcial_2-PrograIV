from ..Model.Cliente import Cliente
from ..Model.Factura import Factura 
from ..Model.ProductosControl import ProductosControl 
from ..Model.ControlFertilizantes import ControlFertilizantes 
from ..Model.ControlPlagas import ControlPlagas 
from ..Model.Antibioticos import Antibioticos

def create_product_antibiotic(**kwargs):
    return Antibioticos(**kwargs)

def create_product_fertilizer(**kwargs):
    return ControlFertilizantes(**kwargs)

def create_product_pests(**kwargs):
    return ControlPlagas(**kwargs)

def create_client(**kwargs):
    return Cliente(**kwargs)

def create_bill():
    return Factura()

def append_product_bill(product: ControlPlagas | ControlFertilizantes | Antibioticos, bill: Factura):
    bill.objects = product

def append_bill_client(client: Cliente, bill: Factura):
    client.bills = bill

def append_client_list(client: Cliente, client_list: list):
    client_list.append(client)
    
def client_exists(dni: str, clients: list[Cliente]):
    for client in clients:
        if dni == client.dni:
            return client
            
    return False

#Pequeños test
client: list[Cliente] = []
ant1 = create_product_antibiotic(name="antibiotico_1", dose="10ml", animal_type="bovino",
                                                      value=12000)
fact1 = create_bill()

client1 = create_client(dni="111", name="juan")

append_product_bill(ant1, fact1)
append_product_bill(ant1, fact1)

append_client_list(client1, client)

append_bill_client(client1, fact1)

print(client)
print(client[0].bills[0].objects)
print(client[0].bills[0].valor_total())

