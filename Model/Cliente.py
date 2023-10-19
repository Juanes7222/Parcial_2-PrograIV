
class Cliente:

    def __init__(self, name, dni) -> None:
        self.__name = name
        self.__dni = dni
        self.__bills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, client_name):
        self.__name = client_name

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, client_dni):
        self.__dni = client_dni

    @property
    def bills(self):
        return self.__bills

    @bills.setter

    def bills(self, bill):
        self.__bills.append(bill)
        
    def __dict__(self):
        values = {
            "nombre": self.name,
            "cedula": self.dni,
        }
        return values

    def check_in(self, bill):
        self.bills.append(bill)
