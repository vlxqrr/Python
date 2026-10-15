import random
n = int(input("Podaj ilosc rzutow: "))

def ThrowDice():
    counterOne = 0
    counterTwo = 0
    counterThree = 0
    counterFour = 0
    counterFive = 0
    counterSix = 0

    if n <= 0:
        print("Podaj dodatnia ilosc rzutow")
        return
    
    for i in range(n):
        result = random.randint(1, 6)
        print(result)

        if result == 1:
            counterOne += 1
        elif result == 2:
            counterTwo += 1
        elif result == 3:
            counterThree += 1
        elif result == 4:
            counterFour += 1
        elif result == 5:
            counterFive += 1
        elif result == 6:
            counterSix += 1

    information = f"Wystapienie 1: {counterOne}\n " \
    f"Wystapienie 2: {counterTwo}\n " \
    f"Wystapienie 3: {counterThree}\n " \
    f"Wystapienie 4: {counterFour}\n " \
    f"Wystapienie 5: {counterFive}\n " \
    f"Wystapienie 6: {counterSix}"

    print(information)

ThrowDice()
