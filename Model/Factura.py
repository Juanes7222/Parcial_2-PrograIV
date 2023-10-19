from datetime import date

class Factura:

    def __init__(self) -> None:
        self.__date = date.today()
        self.__objects = []

    @property
    def date(self):
        return self.__date

    @property
    def objects(self):
        return self.__objects
    
    @objects.setter
    def objects(self, new_object):
        self.__objects.append(new_object)
    
    def check_in(self, value):
        self.objects.append(value)

    def total_value(self):
        total = 0
        for article in self.objects:
            total += article.value
        return total
