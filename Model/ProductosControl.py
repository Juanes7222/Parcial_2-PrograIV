class ProductosControl:

    def __init__(self, ica, name, freq, value) -> None:
        self.__ica = ica
        self.__name = name
        self.__freq = freq
        self.__value = value

    @property
    def ica(self):
        return self.__ica

    @ica.setter
    def ica(self, ica):
        self.__ica = ica

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def freq(self):
        return self.__freq

    @freq.setter
    def freq(self, freq):
        self.__freq = freq

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, cost):
        self.__value = cost
