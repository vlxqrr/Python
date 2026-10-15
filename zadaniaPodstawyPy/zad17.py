def wczytaj_liczbe(minimum, maksimum):
    if minimum > maksimum:
        raise ValueError("Blad parametrow")
    
    while True:
        try:
            liczba = int(input("Podaj liczbe od 1 do 10: "))

            if not minimum <= liczba <= maksimum:
                raise ValueError(f"Liczba musi być w zakresie od {minimum} do {maksimum}")
            
            return liczba
        
        except ValueError as e:
            print(f"Blad: {e}")

result = wczytaj_liczbe(1, 10)
print(result)