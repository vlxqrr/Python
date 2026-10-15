import math

def Triangle():
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))

    if a + b > c:
        print("Mozna utworzyc trojkat")

        obw = a + b + c
        print(f"Obwod wynosi {obw}")

        s = obw / 2
        pole = math.sqrt(s * (s-a) * (s-b) * (s-c))
        print(f"Pole wynosi {pole}")

        if a == b == c:
            print("Trojkat rownoboczny")
        elif a == b or b == c or c == a:
            print("Trojkat rownoraminny")
        else:
            print("Trojkat roznoboczny")
    else:
        print("Nie mozna utworzyc trojkata")
Triangle()