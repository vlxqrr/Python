import random

number = random.randint(1, 100)
counter = 0
while True:
    userNumber = int(input("Podaj liczbe od 1 do 100: "))
    if userNumber > 0:
        if userNumber > number:
            counter += 1
            print("Za duzy")
        elif userNumber < number:
            counter += 1
            print("Za maly")
        elif userNumber == number:
            print("Brawo!")
            break
    else:
        print("Podaj poprawne dane!")
       
        