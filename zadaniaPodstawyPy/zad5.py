def isPalindrom():
    word = input("Podaj slowo: ")
    result = word.strip().lower().replace(" ", "")
    
    if result[::-1] == result:
        print(f"{word} jest palindromem")
    else: 
        print(f"{word} nie jest palindromem")

isPalindrom()