num = int(input("Podaj liczbe: "))

if num % 2 == 0:
    print(f"Liczba {num} jest parzysta")
else:
    print(f"Liczba {num} jest nieparzysta")

if num == 0:
    print(f"Liczba {num} jest rowna 0")
elif num < 0:
    print(f"Liczba {num} jest ujemna")
else:
    print(f"Liczba {num} jest dodatnia")

