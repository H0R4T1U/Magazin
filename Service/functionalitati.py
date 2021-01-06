from datetime import datetime

from Repository.file_repository import FileRepository
from ViewModels.aliment_view_model import AlimentViewModel
from ViewModels.magazine_dupa_nr_alimente_view_model import MagazineDupaNrAlimenteViewModel


class Functionalitati:
    def __init__(self,magazin_repository:FileRepository,aliment_repository:FileRepository):
        self.__magazin_repository = magazin_repository
        self.__aliment_repository = aliment_repository



    def magazine_ordonate_crescator_dupa_nr_alimente(self):
        magazine = self.__magazin_repository.get_all()
        result = []
        for magazin in magazine:
            result.append(MagazineDupaNrAlimenteViewModel(magazin, magazin.nr_alimente))
        return sorted(result, key=lambda x: x.nr_alimente)

    def __search_aliment_id_by_nume(self):
        nume_alimente = self.__alimente_in_magazine().keys()#lista cu numele alimentelor intalnite de cel putin 2 ori
        alimente_repository = self.__aliment_repository.get_all()
        alimente = {}#nume:id
        for aliment in alimente_repository:
            if aliment.nume in nume_alimente:
                if aliment.nume not in alimente.keys():
                    alimente[aliment.nume] = aliment.id_entitate
        return alimente



    def __alimente_in_magazine(self):
        alimente =self.__aliment_repository.get_all()
        alimente_dupa_aparitie={}
        for aliment in alimente:
            if(aliment.nume in alimente_dupa_aparitie.keys()):
                alimente_dupa_aparitie[aliment.nume]+=1
            else:
                alimente_dupa_aparitie[aliment.nume]=1
        #if datetime.strptime(aliment.data_valabilitate,'%d.%m.%Y')>datetime.now():
        alimente_dupa_aparitie_nou = { k:v for k,v in alimente_dupa_aparitie.items() if v>=2 }
        return alimente_dupa_aparitie_nou

    def alimente_to_view_model(self):
        alimente=self.__search_aliment_id_by_nume()
        for k,v in alimente.items():
            print(f"{k},{v}")
        view_models=[]
        for v in alimente.values():
            print("hey")
            aliment=self.__aliment_repository.get_by_id(v)
            if(datetime.strptime(aliment.data_valabilitate,'%d.%m.%Y')>datetime.now()):
                view_models.append(AlimentViewModel(aliment.nume,aliment.data_valabilitate))
        
        return view_models





