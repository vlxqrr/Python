class car:
    def __init__(self, mark, model, caryear, fuel, capacity, speed, wear, engine_on):
        self.mark = "" # jaka marka
        self.model = "" # jaki model
        self.caryear = "" # jaki rocznik
        self.fuel = 0 # ile jest paliwa
        self.capacity = "" # jaka jest pojemnosc
        self.speed = 0 # jaka jest aktualna predkosc
        self.wear = 0 # jakie jest zuzycie na 100km
        self.engine_on = False # czy silnik jest wlaczony

    def turnOn(self):
        self.engine_on = True

    def showState(self):
        print("Status:")
        print(f"Marka auta {self.mark}")
        print(f"Model auta {self.model}")
        print(f"Rocznik auta {self.caryear}")
        print(f"Ilosc paliwa {self.fuel}")
        print(f"Pojemnosc auta {self.capacity}")
        print(f"Aktualna predkosc {self.speed}")
        print(f"Zuzycie na 100km {self.wear}")
        print(f"Czy silnik jest wlaczony {self.turnOn()}")
        
    def speedUp(self):
        pass

    def speedDown(self):
        pass

    def refuel(self):
        pass

    def run(self):
        self.mark = input("Podaj marke auta: ")
        self.model = input("Podaj model auta: ")
        self.caryear = int(input("Podaj rok wyprodukowania: "))
        self.fuel = 0
        self.capacity = int(input("Podaj pojemnosc: "))
        self.speed = 0
        self.engine_on = False

        print("Wybierz akcje ktora chcesz zrobic\n"
        "1) Uruchom silnik\n"
        "2) Sprawdz stan pojazdu\n"
        "3) Przyspiesz\n"
        "4) Hamuj\n"
        "5) Tankuj\n" \
        "6) Zakoncz")

        while True:
            self.action = input("Podaj ktora akcje chcesz wykonac: ")
            if self.action == "1":
                self.turnOn()
                print("Wlaczono silnik")
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
