n = int(input("Podaj n: "))
list = []

if n < 1:
    print(list)
else:
    for i in range(1, n):
        if i % 3 == 0 and i % 5 != 0:
            list.append(i)
    print(list)     