from datetime import datetime


class AlimentValidator:
    def __init__(self,magazin_repository):
        self.__magazin_repository = magazin_repository
    def valideaza(self, aliment):
        erori = []
        try:
            datetime.strptime(aliment.data_valabilitate,'%d.%m.%Y')
        except ValueError:
                erori.append("Trebuie sa existe alimente care nu mai sunt valabile:")
        if not(aliment.nume != ""):
            erori.append("numele  nu este valid ")
        if not(self.__magazin_repository.get_by_id(aliment.id_magazin)):
            erori.append("Id-urile magazinelor trebuie sa existe:")
        if not(aliment.id_entitate):
            erori.append("Trebuie sa introduci macar un id")
        if len(erori) > 0:
            raise ValueError(erori)
