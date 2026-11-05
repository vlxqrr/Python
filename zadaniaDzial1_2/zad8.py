result = int(input("Podaj wynik: "))

if 0 < result < 39:
    print("Ocena: 1")
elif 40 < result < 54:
    print("Ocena: 2")
elif 55 < result < 69:
    print("Ocena: 3")
elif 70 < result < 84:
    print("Ocena: 4")
elif 85 < result < 94:
    print("Ocena: 5")
elif 95 < result < 100:
    print("Ocena: 6")
else: 
    print("Podaj poprawne dane")