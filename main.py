

from Domain.aliment_validator import AlimentValidator
from Domain.magazin_validator import MagazinValidator
from Service.excel_service import ExcelService

#from Service.functionalitati import Functionalitati
from Service.aliment_service import AlimentService
from Service.functionalitati import Functionalitati
from Service.magazin_service import MagazinService
#from Tests.run_all import run_all_tests
from UI.console import Consola
from Repository.file_repository import FileRepository


def main():
    magazin_repository = FileRepository('magazine.txt')
    magazin_validator = MagazinValidator()
    aliment_repository = FileRepository('alimente.txt')
    aliment_validator = AlimentValidator(magazin_repository)

    magazin_service = MagazinService(magazin_repository, magazin_validator)
    aliment_service = AlimentService(aliment_repository,aliment_validator,magazin_repository)

    functionalitati = Functionalitati(magazin_repository,aliment_repository)
    excel_service = ExcelService(magazin_service)
    console = Consola(magazin_service, aliment_service,functionalitati,excel_service)
    console.run_menu()

#run_all_tests()
main()
