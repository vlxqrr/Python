row = int(input("Podaj szerokosc: "))
col = int(input("Podaj wysokosc: "))

for i in range(row):
    for j in range(col):
        print("*", end="")
    print()