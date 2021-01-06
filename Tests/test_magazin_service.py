
from Domain.magazin_validator import MagazinValidator
from Repository.file_repository import FileRepository

from Tests.utils import clear_file

from Service.magazin_service import MagazinService


def test_adauga_magazin():
    clear_file("magazine-test.txt")
    magazin_repository = FileRepository("magazin-test.txt")
    magazin_validator = MagazinValidator()

    magazin_service = MagazinService(magazin_repository, magazin_validator)

    magazin_service.adaugare('1', "La doi pasi", "2","comercial")
    assert len(magazin_service.get_all()) == 1
    added = magazin_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.nume == "La doi pasi"
    assert added.nr_alimente == "2"
    assert added.categorie =="comercial"

    try:
        magazin_service.adaugare('1', "Penny", "3","alimentar")
        assert False
    except Exception:
        assert True