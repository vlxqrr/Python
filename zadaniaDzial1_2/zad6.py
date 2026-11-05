a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

if a > b > c:
    print("A jest najwieksze")
elif b > c > a:
    print("B jest najwieksze")
else: 
    print("C jest najwieksze")