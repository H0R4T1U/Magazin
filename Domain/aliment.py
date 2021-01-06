from Domain.entitate import Entitate


class Aliment(Entitate):
    def __init__(self, id_aliment, id_magazin, nume, data_valabilitate):
        super().__init__(id_aliment)
        self.__id_magazin = id_magazin
        self.__nume = nume
        self.__data_valabilitate = data_valabilitate


    @ property
    def id_magazin(self):
        return self.__id_magazin

    @id_magazin.setter
    def id_magazin(self, id_magazin_nou):
        self.__id_magazin = id_magazin_nou

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, nume_nou):
        self.__nume = nume_nou

    @property
    def data_valabilitate(self):
        return self.__data_valabilitate

    @data_valabilitate.setter
    def data_valabilitate(self, data_valabilitate_noua):
        self.__data_valabilitate = data_valabilitate_noua

