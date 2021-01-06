from Domain.magazin import Magazin


class AlimentViewModel:
    def __init__(self,nume,data_valabilitate):
        self.nume=nume
        self.data_valabilitate=data_valabilitate
    def __str__(self):
        return f"nume:{self.nume} data de valabilitate:{self.data_valabilitate}"
