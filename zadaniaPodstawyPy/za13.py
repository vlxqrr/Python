def Convert():
    data = "12 -3 7 0 18 -5 4"
    convertedData = list(map(int, data.split()))

    evens = filter(lambda x: x > 0, convertedData)
    print(list(evens))

    squares = [x**2 for x in convertedData if x > 0]
    print(squares)

    squaresSum = sum(squares)
    print(squaresSum)
Convert()