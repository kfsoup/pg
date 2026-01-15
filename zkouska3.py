from abc import ABC, abstractmethod

class Zamestnanec(ABC):
    def __init__(self, jmeno, zakladni_mzda):
        self.jmeno = jmeno
        self.zakladni_mzda = zakladni_mzda
        self.pocet_odpracovanych_let = 0

    def pridej_rok(self):
        self.pocet_odpracovanych_let += 1

    @abstractmethod
    def vypocitej_mzdu(self):
        bonus = 1000 * self.pocet_odpracovanych_let
        return self.zakladni_mzda + bonus

    def __str__(self):
        return f"Zamestnanec {self.jmeno}, odpracovanych let {self.pocet_odpracovanych_let}, zakladni mzda {self.zakladni_mzda} Kc"

class Programator(Zamestnanec):
    def vypocitej_mzdu(self):
        return super().vypocitej_mzdu() * 1.1

class Manazer(Zamestnanec):
    def __init__(self, jmeno, zakladni_mzda, pocet_podrizenych):
        super().__init__(jmeno, zakladni_mzda)
        self.pocet_podrizenych = pocet_podrizenych

    def vypocitej_mzdu(self):
        return super().vypocitej_mzdu() + (self.pocet_podrizenych * 1000)

if __name__ == "__main__":
    p1 = Programator("Alice", 40000)
    m1 = Manazer("Bob", 50000, 5)

    zamestnanci = [p1, m1]

    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)
    
    for zamestnanec in zamestnanci:
        zamestnanec.pridej_rok()
        zamestnanec.pridej_rok()

    print("Po pripocteni odpracovanych let:")
    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)