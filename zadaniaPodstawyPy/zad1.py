distanceValue = float(input("Podaj przejechany dystans: "))
wearValue = float(input("Podaj srednie spalanie w litrach na 100 km: "))
priceValue = float(input("Podaj cene za 1 L paliwa: "))

def Wear():
    if distanceValue < 0:
        print("Dystans nie moze byc mniejszy od 0")

    wear = (wearValue * distanceValue) / 100
    print(f"Zuzycie paliwa: {wear:.3f} L")

def Price():
    price = (wearValue * distanceValue * priceValue) / 100
    print(f"Koszt przejazdu {price:.3f} zl")

Wear()
Price()

