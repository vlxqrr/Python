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
                 mileage: float = 0.0,
                 ):
        
        self.mark = mark # jaka marka
        self.model = model # jaki model
        self.caryear = caryear # jaki rocznik
        self.fuel = fuel # ile jest paliwa
        self.capacity = capacity # jaka jest pojemnosc
        self.speed = speed # jaka jest aktualna predkosc
        self.wear = wear # jakie jest zuzycie na 100km
        self.engine_on = engine_on # czy silnik jest wlaczony
        self.mileage = mileage # przejechany dystans w km

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

    def drive(self, distance: float):
            if not self.engine_on:
                print("Odpal silnik")
                return
    
            if distance <= 0:
                print("Dystans musi byc wiekszy niz 0")
    
            fuel_needed = (distance * self.wear) / 100
    
            if self.fuel >= fuel_needed:
                self.fuel -= fuel_needed
                self.mileage += distance
                print(f"Przejechano {distance} km")
                print(f"Spalono: {fuel_needed:.2f} | zostalo: {self.fuel}")
                print(f"Aktualny przebieg auta {self.mileage}")
            else:
                possible_distance = (self.fuel / self.wear)
                self.mileage += possible_distance
                print(f"Brak paliwa, przejechano {possible_distance}")
                self.fuel = 0.0
                self.engine_on = False
                print(f"Silnik zgasl, aktualny przebieg {self.mileage}")

    def acceleration(self):
        if not self.engine_on:
            print("Odpal silnik")
            return
        
        self.speed += 10
        print(f"Jedziesz z predkoscia {self.speed}")
        return self.speed

    def slowingDown(self):
        if not self.engine_on or self.speed == 0:
            print("Nie mozna zwalniac przy 0 predkosci")
            return
        
        self.speed -= 10
        print(f"Jedziesz z predkoscia {self.speed}")
        return self.speed

    def refuel(self):
        if self.engine_on == False:
            refuel = float(input("Ile chcesz zatankowac litrow:? "))
            if refuel <= 0:
                print("Podaj wartosc wieksza od 0")
            elif refuel + self.fuel <= self.capacity:
                self.fuel += refuel
                print(f"Zatankowano {refuel} litrow")
            elif refuel + self.fuel == self.capacity:
                print("Pelny bak")
            else:
                maxSpace = self.capacity - self.fuel
                print(f"Za duzo nie zmiesci sie w baku {self.capacity}, maksymalnie mozesz dolac {maxSpace}")
        else:
            print("Najpierw wylacz silnik!")

    def stopEngine(self):
            if not self.engine_on:
                print("Silnik jest wylaczony!")
                return
            
            if self.speed > 0:
                print(f"Pierw zahamuj do 0, aktualna predkosc {self.speed}")
                return
            
            self.engine_on = False
            print(f"Auto {self.mark} zostalo wylaczone!")

    def run(self):
        self.mark = input("Podaj marke auta: ")
        self.model = input("Podaj model auta: ")
        self.caryear = float(input("Podaj rok wyprodukowania: "))
        self.fuel = float(input("Podaj ile jest paliwa: "))
        self.capacity = float(input("Podaj pojemnosc: "))
        self.wear = float(input("Podaj jakie auto ma spalanie na 100km: "))

        print("Wybierz akcje ktora chcesz zrobic\n"
        "1) Uruchom silnik\n"
        "2) Sprawdz stan pojazdu\n"
        "3) Jedz\n"
        "4) Przyspiesz\n"
        "5) Hamuj\n"
        "6) Tankuj\n" 
        "7) Wylacz silnik\n"
        "8) Zakoncz")

        while True:
            self.action = input("Podaj ktora akcje chcesz wykonac: ")
            if self.action == "1":
                self.startEngine()
            elif self.action == "2":
                self.showState()
            elif self.action == "3":
                self.drive()
            elif self.action == "4":
                self.acceleration()
            elif self.action == "5":
                self.slowingDown()
            elif self.action == "6":
                self.refuel()
            elif self.action == "7":
                self.stopEngine()
            elif self.action == "8":
                print("Dziekujemy za skorzystanie o/")
                break
            else:
                print("Podaj poprawne dane!")

if __name__ == "__main__":
    app = car("", "", "", 0, "", 0, 0, False)
    app.run()
