n = int(input("Podaj n: "))

def Silnia(n):
    silnia = 1
    i = 1
    if n == 0:
        n = 1

    for i in range(1, n + 1):
        silnia *= i
    print(silnia)

Silnia(n)    