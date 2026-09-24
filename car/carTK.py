import tkinter as tk


class car:
    def __init__(
        self,
        mark: str = "",
        model: str = "",
        caryear: int = "",
        fuel: float = 0.0,
        capacity: str = "",
        speed: float = 0.0,
        wear: float = 0.0,
        engine_on: bool = False,
        mileage: float = 0.0,
    ):
        self.root = root
        self.mark = mark  # jaka marka
        self.model = model  # jaki model
        self.caryear = caryear  # jaki rocznik
        self.fuel = fuel  # ile jest paliwa
        self.capacity = capacity  # jaka jest pojemnosc
        self.speed = speed  # jaka jest aktualna predkosc
        self.wear = wear  # jakie jest zuzycie na 100km
        self.engine_on = engine_on  # czy silnik jest wlaczony
        self.mileage = mileage  # przejechany dystans w km

        tk.Label(self.root, text="Podaj marke").pack()
        self.mark_entry = tk.Entry().pack()
        
        tk.Label(self.root, text="Podaj model").pack()
        self.model_entry = tk.Entry().pack()
        
        tk.Label(self.root, text="Podaj rok wyprodukowania").pack()
        self.caryear_entry = tk.Entry().pack()
        
        tk.Label(self.root, text="Podaj ile jest paliwa").pack()
        self.fuel_entry = tk.Entry().pack()

        tk.Label(self.root, text="Podaj pojemnosc").pack()
        self.capacity_entry = tk.Entry().pack()

        tk.Label(self.root, text="Podaj jakie auto ma spalanie na 100km").pack()
        self.wear_entry = tk.Entry().pack()
        
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Car")
    app = car("")
    app.run()
