from BMICalculator import BMICalculator


class Program:
    def __init__(self):
        print("Witaj w kalkulatorze BMI")
        self.saveNumber()
        self.user_data = BMICalculator(self.user_height, self.user_weight)

    # Checking if user entered proper data
    # Checking validation
    def saveNumber(self):
        while True:
            try:
                height = (
                    input("Podaj swoj wzrost w metrach: ").strip().replace(",", ".")
                )

                self.user_height = float(height)

                if not (0.5 <= self.user_height <= 2.5):
                    print("Podaj poprawny wzrost w metrach")
                    continue

                break
            except ValueError:
                print("Podano bledne dane")

        while True:
            try:
                weight = (
                    input("Podaj swoja wage w kilogramach: ").strip().replace(",", ".")
                )

                self.user_weight = float(weight)

                if not (2 <= self.user_weight <= 300):
                    print("Waga musi byc w zakresie od 2 do 300kg")
                    continue

                break
            except ValueError:
                print("Podano bledne dane")

    # Saving data to file
    def saveToFile(self):
        with open("BMI/aplikacja_konsolowa/wynik_bmi.txt", "w") as file:
            bmi_value = self.user_data.countBMI()
            interpretation_bmi = self.user_data.interpretationBMI()
            file.write("Wzrost " + str(self.user_height) + "m \n")
            file.write("Waga " + str(self.user_weight) + "kg \n")
            file.write("BMI " + str(bmi_value) + "\n")
            file.write("Interpretacja " + str(interpretation_bmi) + "\n")

    # Getting and showing users data
    def run(self):
        bmi_value = self.user_data.countBMI()
        interpretation_bmi = self.user_data.interpretationBMI()
        print(f"Wzrost {self.user_height} m")
        print(f"Waga {self.user_weight} kg")
        print(f"BMI {bmi_value}")
        print(f"Interpretacja {interpretation_bmi}")
        self.saveToFile()
        print("Wynik zapisany")


if __name__ == "__main__":
    program = Program()
    program.run()
