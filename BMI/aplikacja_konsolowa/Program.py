from BMICalculator import BMICalculator

class Program():
    def __init__(self):
        print(f"Witaj w kalkulatorze BMI")

        self.user_height = float(input("Podaj swoj wzrost w metrach: "))
        self.user_weight = float(input("Podaj swoja wage w kilogramach: "))

        self.user_data = BMICalculator(self.user_height, self.user_weight)

        
    def saveToFile(self):
        with open("BMI/aplikacja_konsolowa/wynik_bmi.txt", "w") as file:
            bmi_value = self.user_data.countBMI()
            interpretation_bmi = self.user_data.interpretationBMI()
            file.write("Wzrost " + str(self.user_height) + "m \n")
            file.write("Waga " + str(self.user_weight) + "kg \n")
            file.write("BMI " + str(bmi_value) + "\n")
            file.write("Interpretacja " + str(interpretation_bmi) + "\n")
           
            
    def run(self):
        bmi_value = self.user_data.countBMI()
        interpretation_bmi = self.user_data.interpretationBMI()
        print(f"Wzrost {self.user_height} m")
        print(f"Waga {self.user_weight} kg")
        print(f"BMI {bmi_value}")
        print(f"Interpretacja {interpretation_bmi}")
        self.saveToFile()
        print(f"Wynik zapisany")
        
if __name__ == "__main__":
    program = Program()
    program.run()