from Domain.magazin import Magazin

from Domain.magazin_validator import MagazinValidator
from Repository.file_repository import FileRepository


class MagazinService:
    def __init__(self, magazine_repository: FileRepository, magazin_validator: MagazinValidator):
        self.__magazine_repository = magazine_repository
        self.__magazin_validator = magazin_validator

    def get_all(self):
        return self.__magazine_repository.get_all()

    def adaugare(self, id_magazin, nume, nr_alimente,categorie):
        '''
        adauga un magazin in dicitonarul cu magazine
        :param id_magazin: numar intreg
        :param nume: string
        :param nr_alimente: numar intreg
        :param categorie:string

        :return:
        '''

        magazin = Magazin(id_magazin, nume, nr_alimente,categorie)
        self.__magazin_validator.valideaza(magazin)
        self.__magazine_repository.adaugare(magazin)

    def stergere(self, id_magazin):
        '''

        :param id_magazin:
        :return:
        '''
        self.__magazine_repository.stergere(id_magazin)


