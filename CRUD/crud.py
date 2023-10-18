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