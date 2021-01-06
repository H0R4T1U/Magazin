class MagazineDupaNrAlimenteViewModel:
    def __init__(self,magazin,nr_alimente):
        self.magazin = magazin
        self.nr_alimente = nr_alimente
    def __str__(self):
        return f"Magazinul{self.magazin}cu {self.nr_alimente} alimente in categoria:{self.magazin.categorie}"