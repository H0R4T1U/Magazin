class MagazinValidator:
    def valideaza(self, magazin):
        erori = []
        if not(magazin.nume != ""):
            erori.append("numele  nu este valid ")
        if not(magazin.nr_alimente > 0):
            erori.append("Numarul alimentelor nu este valid:")
        if len(erori) > 0:
            raise ValueError(erori)