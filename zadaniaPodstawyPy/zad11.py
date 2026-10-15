def Zbiory():
    python = ["U01", "U02", "U03", "U03", "U05"]
    robotyka = ["U02", "U04", "U05"]

    obaKola = set(python) & set(robotyka)
    wynikObaKola = sorted(obaKola)
    print(f"Oba kola: {wynikObaKola}")

    conajmniejJedno = set(python) | set(robotyka)
    wynikConajmniejJedno = sorted(conajmniejJedno)
    print(f"Conajmniej jedno: {wynikConajmniejJedno}")

    tylkoPython = set(python) - set(robotyka)
    wynikTylkoPython = sorted(tylkoPython)
    print(f"Tylko w Python: {wynikTylkoPython}")

    tylkoJedno = set(python) ^ set(robotyka)
    wynikTylkoJedno = sorted(tylkoJedno)
    print(f"Dokladnie jedno: {wynikTylkoJedno}")
Zbiory()

