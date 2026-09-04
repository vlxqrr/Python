class BMICalculator:
    def __init__(self, _height: float, _weight: float) -> None:
        self._height = float(_height)
        self._weight = float(_weight)
        self._BMI = None

        if not (0.5 <= _height <= 2.5):
            raise ValueError("Enter a proper value") 

        if not (2 <= _weight <= 300):
            raise ValueError("Enter a proper value") 

    # getting a height value
    @property
    def height(self):
        print("getter method called height")
        return self._height

    # setting a height value
    # checking the validation
    @height.setter
    def height(self, value):
        print("getter method called weight")

        if not (0.5 <= value <= 2.5):
            raise ValueError("Enter a proper value") 

        self._height = value

    # getting a weight value
    @property
    def weight(self):
        print("getter method called weight")
        return self._weight
    
    # setting a weight value
    # checking the validation
    @weight.setter
    def weight(self, value):
        print("getter method called weight")

        if not (0.5 <= value <= 2.5):
            raise ValueError("Enter a proper value") 
    
        self._weight = value

    def countBMI(self) -> float:
        self.BMI = self._weight/(self._height ** 2)
        return round(self.BMI, 2)

    def interpretationBMI(self):
        if self.BMI < 18.5:
            return "niedowaga"
        elif 18.5 <= self.BMI <= 24.9:
            return "waga prawidlowa"
        elif 25.0 <= self.BMI <= 29.9:
            return "nadwaga"
        else:
            return "otylosc"

    

