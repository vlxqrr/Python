class BMICalculator:
    def __init__(self, _height: float, _weight: float) -> None:
        self.set_height = float(_height)
        self.set_weight = float(_weight)

        if not (0.5 <= _height <= 2.5):
            raise ValueError("Enter a proper value") 

        if not (2 <= _weight <= 300):
            raise ValueError("Enter a proper value") 

    def get_height(self):
        print("getter method called height")
        return self._height

    def get_weight(self):
        print("getter method called weight")
        return self._weight

    def countBMI(self, _weight, _height) -> float:
        BMI = _weight/(_height ** 2)

    def set_BMI(self, ):
        return x


user_height = float(input("Enter your height in meters: "))
user_weight = float(input("Enter your weight in kilograms: "))

user_data = BMICalculator(_height = user_height, _weight = user_weight)

print(user_data)
