from Model import ProductosControl as producto_control


class ControlFertilizantes(producto_control.ProductosControl):

    def __init__(self, ica, name, freq, value, last_applic):
        self.__last_applic = last_applic
        super().__init__(ica, name, freq, value)

    @property
    def last_applic(self):
        return self.__last_applic

    @last_applic.setter
    def last_applic(self, last_applic):
        self.__last_applic = last_applic
        
    def __str__(self) -> str:
        info = f"ICA: {self.ica}\tNOMBRE: {self.name}\tFRECUENCIA: {self.freq}\n"
        info += f"VALOR: {self.value}\tULTIMA APLICACION: {self.last_applic}"
        return info
