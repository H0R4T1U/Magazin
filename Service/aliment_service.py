from Domain.aliment import Aliment
from Domain.aliment_validator import AlimentValidator
from Repository.file_repository import FileRepository
from ViewModels.aliment_view_model import AlimentViewModel


class AlimentService:
    def __init__(self, alimente_repository: FileRepository, alimente_validator:AlimentValidator,magazine_repository: FileRepository):
        self.__alimente_repository = alimente_repository
        self.__alimente_validator = alimente_validator
        self.__magazine_repository = magazine_repository


    def get_all(self):
        view_models = []
        for aliment in self.__alimente_repository.get_all():
            magazin = self.__magazine_repository.get_by_id(aliment.id_magazin)

            view_models.append(AlimentViewModel(aliment.id_entitate,magazin, aliment.nume,
                                                aliment.data_valabilitate))

        return view_models

    def adaugare(self, id_aliment, id_magazin, nume, data_valabilitate):
        '''
        :return:
        '''

        aliment = Aliment(id_aliment, id_magazin, nume, data_valabilitate)
        self.__alimente_validator.valideaza(aliment)
        self.__alimente_repository.adaugare(aliment)

