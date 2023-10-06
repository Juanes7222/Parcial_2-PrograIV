import unittest
from Model import Cliente as cliente
from Model import Antibioticos as antibiotico
from Model import ControlFertilizantes as control_fertilizante
from Model import ControlPlagas as control_plagas
from Model import Factura as factura

class TestClientes(unittest.TestCase):

    def setUp(self):
        self.cliente = cliente.Cliente("Sebastian Cacante", "1091272102")
        self.antibiotico_1 = antibiotico.Antibioticos("antibiotico_1", "10ml", "bovino",
                                                      "12000")
        self.antibiotico_2 = antibiotico.Antibioticos("antibiotico_2", "60ml", "caprino",
                                                      "50000")
        self.antibiotico_3 = antibiotico.Antibioticos("antibioticos_3", "20ml", "porcino",
                                                      "1000000")
        self.fertilizante = control_fertilizante.ControlFertilizantes("ABC123", "fertilizante_1",
                                                                      "2 días", "500000",
                                                                      "4/10/2023")
        self.plaga = control_plagas.ControlPlagas("DEF456", "plaga_1", "8 días", "120000",
                                                  "15")

        self.factura_1 = factura.Factura()
        self.factura_2 = factura.Factura()
        
        self.factura_1.objects = self.antibiotico_1
        self.factura_1.objects = self.antibiotico_2
        self.factura_1.objects = self.antibiotico_2
        
        self.factura_2.objects = self.antibiotico_2
        self.factura_2.objects = self.antibiotico_3
        self.factura_2.objects = self.fertilizante
        

    def test_facturar(self):
        self.cliente.check_in(self.factura_1)
        self.cliente.check_in(self.factura_2)
        


if __name__ == '__main__':
    unittest.main()
