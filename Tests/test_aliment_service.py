
from Tests.utils import clear_file

from Domain.aliment_validator import AlimentValidator
from Domain.magazin import Magazin
from Repository.file_repository import FileRepository
from Service.aliment_service import AlimentService


def test_aliment_service():
    clear_file("magazin-test.txt")
    clear_file("aliment-test.txt")
    magazin_repository = FileRepository("magazin-test.txt")

    aliment_repository = FileRepository("rute-test.txt")
    aliment_validator = AlimentValidator()

    aliment_service = AlimentService(aliment_repository, aliment_validator, magazin_repository)

    magazin_repository.adaugare(Magazin('1', "La doi pasi","2","comercial"))
    magazin_repository.adaugare(Magazin('2', "Penny","3", "alimentar"))

    aliment_service.adaugare('1',"1" "pepsi", "15.10.2021")
    assert len(aliment_repository.get_all()) == 1
    added = aliment_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.id_magazin == "1"
    assert added.nume == "pepsi"
    assert added.data_valabilitate == "15.10.2021"

    try:
        aliment_service.adaugare('2', "2", "cola","16.10.2021")
        assert False
    except Exception:
        assert True

'''magazine_ordonate = functionalitati.magazine_ordonate_crescator_dupa_nr_alimente()
    assert len(magazine_ordonate) == 2
    assert magazine_ordonate[0][0].id_entitate == "2"
    assert magazine_ordonate[0][1] == 0
    assert magazine_ordonate[1][0].id_entitate == "1"
    assert magazine_ordonate[1][1] == 1
'''

''' ruta_service.adauga('2', "2", "1", 10,"true")
    rute_in_municipiu = ruta_service.rute_care_se_opresc_in_municipiu()
    assert len(rute_in_municipiu) == 1
    assert rute_in_municipiu[0][0].id_entitate == '2'
    assert rute_in_municipiu[0][1] == "Fagaras"
'''