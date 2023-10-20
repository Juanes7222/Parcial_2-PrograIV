import unittest
from Model import Cliente as cliente
from Model import Antibioticos as antibiotico
from Model import ControlFertilizantes as control_fertilizante
from Model import ControlPlagas as control_plagas
from Model import Factura as factura
from CRUD import crud
from UI import validations


class TestClientes(unittest.TestCase):

    def setUp(self):
        self.client = cliente.Cliente("Sebastian Cacante", "1091272102")
        self.antibiotic_1 = antibiotico.Antibioticos("antibiotic_1", "10ml", "bovino",
                                                     12000)
        self.antibiotic_2 = antibiotico.Antibioticos("antibiotic_2", "60ml", "caprino",
                                                     50000)
        self.antibiotic_3 = antibiotico.Antibioticos("antibiotic_3", "20ml", "porcino",
                                                     1000000)
        self.fertilizer = control_fertilizante.ControlFertilizantes("ABC123", "fertilizer_1",
                                                                    "2 días", 500000,
                                                                    "4/10/2023")
        self.pest = control_plagas.ControlPlagas("DEF456", "pest_1", "8 días", 120000,
                                                 "15")
        self.bill_1 = factura.Factura()
        self.bill_2 = factura.Factura()

        self.client_crud = crud.create_client(name="Juan Esteban Cardona", dni="43381789")
        self.antibiotic_crud_1 = crud.create_product_antibiotic(name="antibiotic_1", dose="500ml",
                                                                animal_type="bovino", value=12000)
        self.antibiotic_crud_2 = crud.create_product_antibiotic(name="antibiotic_2", dose="400ml",
                                                                animal_type="caprino", value=50000)
        self.antibiotic_crud_3 = crud.create_product_antibiotic(name="antibiotic_3", dose="570ml",
                                                                animal_type="porcino", value=120000)
        self.fertilizer_crud = crud.create_product_fertilizer(ica="GHI789", name="fertilizer_1", freq="7 días",
                                                              value=128000, last_applic="18/10/2023")
        self.pest_crud = crud.create_product_pests(ica="JKL123", name="pest_1", freq="5 días", value=200000,
                                                   grace_period="4")
        self.bill_crud_1 = crud.create_bill()
        self.bill_crud_2 = crud.create_bill()

    def test_check_in(self):
        self.bill_1.check_in(self.antibiotic_1)
        self.bill_1.check_in(self.antibiotic_2)
        self.bill_1.check_in(self.antibiotic_3)
        self.bill_1.check_in(self.fertilizer)
        self.bill_1.check_in(self.pest)

        self.bill_2.check_in(self.antibiotic_1)
        self.bill_2.check_in(self.antibiotic_2)
        self.bill_2.check_in(self.antibiotic_3)
        self.bill_2.check_in(self.fertilizer)
        self.bill_2.check_in(self.pest)

        self.client.check_in(self.bill_1)
        self.client.check_in(self.bill_2)

        self.assertEqual(self.client.bills[0].total_value(), 1682000)
        self.assertEqual(self.client.bills[1].total_value(), 1682000)

    def test_crud(self):
        crud.append_product_bill(self.antibiotic_crud_1, self.bill_crud_1)
        crud.append_product_bill(self.antibiotic_crud_2, self.bill_crud_1)
        crud.append_product_bill(self.antibiotic_crud_3, self.bill_crud_1)
        crud.append_product_bill(self.fertilizer_crud, self.bill_crud_1)
        crud.append_product_bill(self.pest_crud, self.bill_crud_1)

        crud.append_product_bill(self.antibiotic_crud_1, self.bill_crud_2)
        crud.append_product_bill(self.antibiotic_crud_2, self.bill_crud_2)
        crud.append_product_bill(self.antibiotic_crud_3, self.bill_crud_2)
        crud.append_product_bill(self.fertilizer_crud, self.bill_crud_2)
        crud.append_product_bill(self.pest_crud, self.bill_crud_2)

        crud.append_bill_client(self.client_crud, self.bill_crud_1)
        crud.append_bill_client(self.client_crud, self.bill_crud_2)

        self.assertEqual(self.client_crud.bills[0].total_value(), 510000)
        self.assertEqual(self.client_crud.bills[1].total_value(), 510000)

    def test_input_validations(self):
        self.assertTrue(validations.validate_name("Sebastian"))
        self.assertTrue(validations.validate_name("Sebastian Cacante"))
        self.assertTrue(validations.validate_name("Sebastian Cacante Salazar"))
        self.assertTrue(validations.validate_name("Mañe"))
        self.assertFalse(validations.validate_name("$eb?stian"))
        self.assertFalse(validations.validate_name("Se"))

        self.assertTrue(validations.validate_cedula("1091272102"))
        self.assertTrue(validations.validate_cedula("43381789"))
        self.assertFalse(validations.validate_cedula("ABCDEF123456"))
        self.assertFalse(validations.validate_cedula("123"))
        self.assertFalse(validations.validate_cedula("1.091.272.102"))
        self.assertFalse(validations.validate_cedula("1-091-272-102"))
        self.assertFalse(validations.validate_cedula("1 091 272 102"))


if __name__ == '__main__':
    unittest.main()
