class car:
    def __init__(self, 
                 mark: str = "", 
                 model: str = "", 
                 caryear: int = "", 
                 fuel : float = 0.0, 
                 capacity: str = "", 
                 speed: float = 0.0, 
                 wear: float = 0.0, 
                 engine_on: bool = False,
                 ):
        
        self.mark = mark # jaka marka
        self.model = model # jaki model
        self.caryear = caryear # jaki rocznik
        self.fuel = fuel # ile jest paliwa
        self.capacity = capacity # jaka jest pojemnosc
        self.speed = speed # jaka jest aktualna predkosc
        self.wear = wear # jakie jest zuzycie na 100km
        self.engine_on = engine_on # czy silnik jest wlaczony

    def car(self):
        car = self.mark

    def startEngine(self):
        if self.fuel > 0:
            self.engine_on = True
            print(f"Auto {self.mark} wlaczone!")
        else:
            print("Nie ma paliwa")


    def showState(self):
        print("Status:")
        print(f"Marka auta {self.mark}")
        print(f"Model auta {self.model}")
        print(f"Rocznik auta {self.caryear}")
        print(f"Ilosc paliwa {self.fuel}")
        print(f"Pojemnosc auta {self.capacity}")
        print(f"Aktualna predkosc {self.speed}")
        print(f"Zuzycie na 100km {self.wear}")
        print(f"Czy silnik jest wlaczony {self.engine_on}")
        
    def speedUp(self):
        pass

    def speedDown(self):
        pass

    def refuel(self):
        pass

    def run(self):
        self.mark = input("Podaj marke auta: ")
        self.model = input("Podaj model auta: ")
        self.caryear = float(input("Podaj rok wyprodukowania: "))
        self.fuel = float(input("Podaj ile jest paliwa"))
        self.capacity = float(input("Podaj pojemnosc: "))

        print("Wybierz akcje ktora chcesz zrobic\n"
        "1) Uruchom silnik\n"
        "2) Sprawdz stan pojazdu\n"
        "3) Przyspiesz\n"
        "4) Hamuj\n"
        "5) Tankuj\n" 
        "6) Zakoncz")

        while True:
            self.action = input("Podaj ktora akcje chcesz wykonac: ")
            if self.action == "1":
                self.startEngine()
            elif self.action == "2":
                self.showState()
            elif self.action == "3":
                self.speedUp()
            elif self.action == "4":
                self.speedDown()
            elif self.action == "5":
                self.refuel()
            elif self.action == "6":
                print("Dziekujemy za skorzystanie o/")
                break
            else:
                print("Podaj poprawne dane!")

if __name__ == "__main__":
    app = car("", "", "", 0, "", 0, 0, False)
    app.run()
