from Domain.entitate import Entitate


class Magazin(Entitate):
    '''
    descrie entitatea magazin
    '''

    def __init__(self, id_magazin, nume, nr_alimente,categorie):
        super().__init__(id_magazin)
        self.__nume = nume
        self.__nr_alimente = nr_alimente
        self.__categorie = categorie
    def __str__(self):
        return f"id: {self.id_entitate}, nume: {self.nume}, nr_alimente: {self.nr_alimente},categorie{self.categorie}"

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, nume_nou):
        self.__nume = nume_nou

    @property
    def nr_alimente(self):
        return self.__nr_alimente

    @nr_alimente.setter
    def nr_alimente(self, nr_alimente_nou):
        self.__nr_alimente = nr_alimente_nou

    @property
    def categorie(self):
        return self.__categorie

    @categorie.setter
    def categorie(self, categorie_noua):
        self.__categorie = categorie_noua


