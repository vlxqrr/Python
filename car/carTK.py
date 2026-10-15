import tkinter as tk

class car:
    def __init__(self, root):
        self.root = root
        self.mark = ""
        self.model = ""
        self.caryear = 0
        self.fuel = 0.0
        self.capacity = 0.0
        self.speed = 0.0
        self.wear = 0.0
        self.engine_on = False
        self.mileage = 0.0

        self.lbl_mark = tk.Label(self.root, text="Podaj marke")
        self.lbl_mark.pack()
        self.mark_entry = tk.Entry(self.root)
        self.mark_entry.pack()

        self.lbl_model = tk.Label(self.root, text="Podaj model")
        self.lbl_model.pack()
        self.model_entry = tk.Entry(self.root)
        self.model_entry.pack()

        self.lbl_year = tk.Label(self.root, text="Podaj rok wyprodukowania")
        self.lbl_year.pack()
        self.caryear_entry = tk.Entry(self.root)
        self.caryear_entry.pack()

        self.lbl_fuel = tk.Label(self.root, text="Podaj ile jest paliwa")
        self.lbl_fuel.pack()
        self.fuel_entry = tk.Entry(self.root)
        self.fuel_entry.pack()

        self.lbl_cap = tk.Label(self.root, text="Podaj pojemnosc baku")
        self.lbl_cap.pack()
        self.capacity_entry = tk.Entry(self.root)
        self.capacity_entry.pack()

        self.lbl_wear = tk.Label(self.root, text="Podaj spalanie na 100km")
        self.lbl_wear.pack()
        self.wear_entry = tk.Entry(self.root)
        self.wear_entry.pack()

        self.submit_button = tk.Button(self.root, text="Zatwierdz", command=self.menu)
        self.submit_button.pack(pady=5)

        self.required_entries = [
            self.mark_entry,
            self.model_entry,
            self.caryear_entry,
            self.fuel_entry,
            self.capacity_entry,
            self.wear_entry,
        ]

        self.form_widgets = [
            self.lbl_mark,
            self.mark_entry,
            self.lbl_model,
            self.model_entry,
            self.lbl_year,
            self.caryear_entry,
            self.lbl_fuel,
            self.fuel_entry,
            self.lbl_cap,
            self.capacity_entry,
            self.lbl_wear,
            self.wear_entry,
            self.submit_button,
        ]

        self.menu_label = tk.Label(
            self.root,
            text="1) Uruchom silnik\n 2) Sprawdz stan pojazdu\n 3) Jedz\n 4) Przyspiesz\n 5) Hamuj\n 6) Tankuj\n 7) Wylacz silnik\n 8) Zakoncz",
        )

        self.choice_label = tk.Label(self.root, text="Wybierz numer opcji (1-8)")
        self.choice_entry = tk.Entry()
        self.choice_button = tk.Button(
            self.root, text="Wybierz", command=self.chooseOption
        )

        self.result_label = tk.Label(self.root, text="")
        self.engineStatus = ""

        self.refuel_label = tk.Label(self.root, text="Ile litrów chcesz dolać?")
        self.refuel_entry = tk.Entry(self.root)
        self.refuel_button = tk.Button(
            self.root, text="Zatankuj", command=self.submitRefuel
        )

        self.km_label = tk.Label(self.root, text="Ile km chcesz przejechac?")
        self.km_entry = tk.Entry(self.root)
        self.km_button = tk.Button(self.root, text="Jedz", command=self.submitDistance)

        self.message_label = tk.Label(self.root, text="")

    def menu(self):
        # Sprawdzenie czy ktorekolwiek z pol nie jest puste
        if not all(entry.get().strip() for entry in self.required_entries):
            self.message_label.config(text="Wszystkie pola muszą zostać uzupełnione!")
            return

        # Walidacja formatow liczbowych
        try:
            self.mark = self.mark_entry.get().strip()
            self.model = self.model_entry.get().strip()
            self.caryear = float(self.caryear_entry.get().strip())
            self.fuel = float(self.fuel_entry.get().strip())
            self.capacity = float(self.capacity_entry.get().strip())
            self.wear = float(self.wear_entry.get().strip())
            self.message_label.config(text="Wszystkie pola zostaly poprawnie podane")
            self.menu_label.pack(pady=5)
            self.choice_label.pack(pady=2)
            self.choice_entry.pack(pady=2)
            self.choice_button.pack(pady=2)
            self.result_label.pack(pady=5)
            for widget in self.form_widgets:
                widget.pack_forget()

        except ValueError:
            self.message_label.config(
                text="Błąd formatu: Rok, paliwo, pojemność i spalanie muszą być poprawnymi liczbami!"
            )

    def chooseOption(self):
        action = self.choice_entry.get().strip()

        self.choice_entry.delete(0, tk.END)

        if action == "1":
            self.startEngine()

        elif action == "2":
            self.showState()

        elif action == "3":
            self.drive()

        elif action == "4":
            self.acceleration()

        elif action == "5":
            self.slowingDown()

        elif action == "6":
            self.refuel()

        elif action == "7":
            self.stopEngine()

        elif action == "8":
            self.result_label.config(text="Dziękujemy za skorzystanie o/")
            self.root.destroy()

        else:
            self.result_label.config(text="Podaj poprawny numer akcji (1-8)!")

    def startEngine(self):
        if self.fuel > 0:
            self.engine_on = True
            self.result_label.config(text="Auto wlaczone")
        else:
            self.result_label.config(text="Nie ma paliwa")

    def showState(self):
        self.engineStatus = "wlaczony" if self.engine_on else "wylaczony"
        stan = (
            f"Pojazd: {self.mark} {self.model} ({self.caryear})\n"
            f"Pojazd jest {self.engineStatus}\n"
            f"Paliwo: {self.fuel:.1f}/{self.capacity:.1f} l\n"
            f"Aktualna predkosc: {self.speed}"
            f"Przebieg: {self.mileage:.1f} km"
        )
        self.result_label.config(text=f"Stan pojazdu {stan}\n")

    def drive(self):
        if not self.engine_on:
            self.result_label.config(text="Odpal silnik")
            return
        self.km_label.pack(pady=2)
        self.km_entry.pack(pady=2)
        self.km_button.pack(pady=5)
        self.result_label.config(text="Wpisz dystans do przejechania w km")

    def submitDistance(self):
        distance_value = self.km_entry.get().strip()

        try:
            distance = float(distance_value)
        except ValueError:
            self.result_label.config(text="Wpisz poprawna liczbe")
            if distance <= 0:
                self.result_label.config(text="Podaj wartosc wieksza od 0")
            return

        fuel_needed = (distance * self.wear) / 100
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            self.mileage += distance
            result = f"Przejechano {distance:.2f} km\n"
            result += f"Spalony {fuel_needed:.2f} | zostalo {self.fuel:.2f}\n"
            result += f"Aktualny przebieg auta {self.mileage:.2f}"
            self.result_label.config(text=result)
        else:
            possible_distance = (self.fuel / self.wear) * 100
            self.mileage += possible_distance
            self.fuel = 0.0
            self.engine_on = False
            result = f"Brak paliwa, przejechano {possible_distance:.2f} \n"
            result += f"Silnik zgasl, aktualny przebieg {self.mileage:.2f}"
            self.result_label.config(text=result)

        self.km_entry.delete(0, tk.END)
        self.km_label.pack_forget()
        self.km_entry.pack_forget()
        self.km_button.pack_forget()

    def acceleration(self):
        if not self.engine_on:
            self.result_label.config(text="Odpal silnik")
        self.speed += 10
        self.result_label.config(text=f"Jedziesz z predkoscia {self.speed}")
        return self.speed

    def slowingDown(self):
        if not self.engine_on:
            self.result_label.config(text="Nie mozna zwalniac z wylaczonym silnikiem")
            return
        if self.speed <= 0:
            self.result_label.config(text="Nie mozna zwalniac przy predkosci 0")
            return
        self.speed -= 10

        self.result_label.config(text=f"Jedziesz z predkoscia {self.speed}")
        return self.speed

    def refuel(self):
        if self.engine_on:
            self.result_label.config(text="Najpierw wylacz silnik")
            return
        self.refuel_label.pack(pady=2)
        self.refuel_entry.pack(pady=2)
        self.refuel_button.pack(pady=5)
        self.result_label.config(text="Wpisz ilość paliwa")

    def submitRefuel(self):
        value = self.refuel_entry.get().strip()

        try:
            refuel_value = float(value)
        except ValueError:
            self.result_label.config(text="Wpisz poprawna liczbe")
        if refuel_value <= 0:
            self.result_label.config(text="Podaj wartosc wieksza od 0")
            return

        if refuel_value + self.fuel > self.capacity:
            maxSpace = self.capacity - self.fuel
            self.result_label.config(
                text=f"Za duzo, nie zmiesci sie w baku ({self.capacity} l). Maksymalnie mozesz dolac: {maxSpace:.2f} l"
            )
            return
        self.fuel += refuel_value
        if self.fuel >= self.capacity:
            self.result_label.config(text="Bak jest pelny!")
        else:
            self.result_label.config(
                text=f"Zatankowano {refuel_value} l. Aktualny stan {self.fuel:.2f} l"
            )

        self.refuel_entry.delete(0, tk.END)
        self.refuel_label.pack_forget()
        self.refuel_entry.pack_forget()
        self.refuel_button.pack_forget()

    def stopEngine(self):
        if not self.engine_on:
            self.result_label.config(text="Silnik jest wylaczony")
            return

        if self.speed > 0:
            self.result_label.config(
                text=f"Pierw zahamuj do 0, aktualna predkosc {self.speed} km/h"
            )
            return
        self.engine_on = False
        self.result_label.config(text="Auto zostalo wylaczone")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Car")
    app = car(root)
    app.run()
