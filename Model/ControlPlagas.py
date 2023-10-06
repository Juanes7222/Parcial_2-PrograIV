from Model import ProductosControl as producto_control


class ControlPlagas(producto_control.ProductosControl):

    def __init__(self, ica, name, freq, value, grace_period):
        self.__grace_period = grace_period
        super().__init__(ica, name, freq, value)

    @property
    def grace_period(self):
        return self.__grace_period

    @grace_period.setter
    def grace_period(self, period):
        self.__grace_period = period
