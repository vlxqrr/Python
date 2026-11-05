word = input("Podaj slowo: ")
lowerWord = word.lower().replace(" ", "")
if lowerWord[::-1] == lowerWord or lowerWord == "":
    print(f"Slowo {word} jest palindromem")
