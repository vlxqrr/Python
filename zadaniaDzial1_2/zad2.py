a = int(input("Podaj a: "))
b = int(input("Podaj b: "))


if a < 0 or b < 0:
    print("Podaj dodatnie liczby!")
else:
    pole = a * b
    obw = 2 * a + 2 * b
    print(f"Pole: {pole}, Obwod: {obw}")
