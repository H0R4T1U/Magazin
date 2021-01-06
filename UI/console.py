

from Service.functionalitati import Functionalitati
from Service.aliment_service import AlimentService
from Service.excel_service import ExcelService
from Service.magazin_service import MagazinService


class Consola:
    def __init__(self, magazin_service: MagazinService,aliment_service: AlimentService,functionalitati:Functionalitati,excel_service :ExcelService):
        self.__magazin_service = magazin_service
        self.__aliment_service = aliment_service
        self.__functionalitati =functionalitati
        self.__excel_service =excel_service


    def run_menu(self):
        while True:
            print("1. CRUD magazine")
            print("2. CRUD alimente")
            print("3. Functionalitati")
            print("x. Iesire")
            optiune = input("Dati optiunea")
            if optiune == "1":
                self.run_crud_magazine()
            elif optiune == "2":
                self.run_crud_alimente()
            elif optiune == "3":
                self.run_functionalitati_menu()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida!")

    def run_crud_magazine(self):
        while True:
            print("1. Adaugare magazin")
            print("a. Afiseaza toate magazinele")
            print("x. Inapoi")
            optiune = input("Dati optiunea")
            if optiune == "1":
                self.ui_adaugare_magazin()
            elif optiune == "a":
                self.ui_afisare_magazine()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida")

    def ui_adaugare_magazin(self):
        try:
            id_magazin = input("Dati id-ul magazinului: ")
            nume = input("Dati numeul magazinului: ")
            nr_alimente =int(input("Dati numarul de alimente:"))
            categorie =input("Dati categoria magazinului: ")


            self.__magazin_service.adaugare(id_magazin, nume,nr_alimente, categorie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_afisare_magazine(self):
        magazine = self.__magazin_service.get_all()
        for magazin in magazine:
            print(magazin)


    def run_crud_alimente(self):
        while True:
            print("1. Adaugare aliment")
            print("a. Afiseaza toate alimentele")
            print("x. Inapoi")
            option = input("Dati optiunea: ")
            if option == "1":
                self.ui_add_aliment()
            elif option == "a":
                self.ui_show_all_aliment()
            elif option == "x":
                break
            else:
                print("aliment invalid!")

    def ui_add_aliment(self):
        try:
            id_aliment = input('ID-ul alimenti: ')
            id_magazin = input('ID-ul magazinului: ')
            nume=input("Numele alimentului:")
            data_valabilitate =input('Data de valabilitate a alimentului: ')


            self.__aliment_service.adaugare(id_aliment, id_magazin,nume, data_valabilitate)

            print('Aliment a fost adaugata cu succes!')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_show_all_aliment(self):
        for aliment in self.__aliment_service.get_all():
            print(aliment)

    def run_functionalitati_menu(self):
        while True:
            print("1. Afisarea magazinelor ordonate crescator dupa nr alimentelor")
            print("2.Afisarea tuturor alimentelor care se gasesc in mai multe magazine:")
            print("x. Inapoi")
            option = input("optiune: ")
            if option =="1":
                self.ui_magazine_ordonate_crescator_dupa_nr_alimente()
            if option == "2":
                self.ui_alimente_to_view_model()
            if option =="s":
                self.ui_alimente_to_view_model()
            elif option == "x":
                break

    def ui_magazine_ordonate_crescator_dupa_nr_alimente(self):
        result = self.__functionalitati.magazine_ordonate_crescator_dupa_nr_alimente()
        for magazin in result:
            print(magazin)

    def ui_alimente_to_view_model(self):
        result = self.__functionalitati.alimente_to_view_model()
        for aliment in result:
            print(aliment)
