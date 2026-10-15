def Ranking():
    uczniowie = ["Ala", "Jan", "Ola", "Ewa"]
    punkty = [18, 12, 18, 15]

    dane = zip(uczniowie, punkty)
    desc = sorted(punkty, reverse=True)
    print(f"Ranking\n {dane} {desc}")
Ranking()