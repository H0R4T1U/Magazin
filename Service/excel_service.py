import pandas as pd

from Service.magazin_service import MagazinService

class ExcelService:
    def __init__(self,magazin_service:MagazinService,file_name="magazine.xlsx"):
        self.__magazin_service = magazin_service
        self.__file_name = file_name

    def export_to_excel(self):
        magazine= self.__magazin_service.get_all()
        df = pd.DataFrame({
            "ID":[magazin.id_entitate for magazin in magazine],
            "nume":[magazin.nume for magazin in magazine],
            "nr_alimente":[magazin.nr_alimente for magazin in magazine],
            "categorie":[magazin.categorie for magazin in magazine ]

        })
        df.to_excel(f"./{self.__file_name}",index=False)