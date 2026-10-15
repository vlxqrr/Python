def add():
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    result = a + b 
    print(result)

def subtract():
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    result = a - b 
    print(result)

def multiply():
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    result = a * b 
    print(result)

def divide():
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    result = a / b 
    print(result)

def Calculator():
    information = "Menu\n" \
    "1. Dodawanie\n" \
    "2. Odejmowanie\n" \
    "3. Mnozenie\n" \
    "4. Dzielenie\n" \
    "5. Zakoncz"
    print(information)
    
    while True:
        action = input("Wybierz akcje ktora chcesz wykonac 1-5: ")

        if action == "1":
            add()
        elif action == "2":
            subtract()
        elif action == "3":
            multiply()
        elif action == "4":
            divide()
        elif action == "5":
            print("Dziekujemy za skorzystanie!")
            break
        else:
            print("Podaj poprawne dane!")

Calculator()