"""
1.  Erstellen Sie ein Programm für einen Gebrauchtwagenhändler, das eine Liste mit drei verschiedenen Fahrzeugen und deren Eigenschaften enthält (Vgl. Kapitel 6.1).
    Das Programm soll daraufhin den Anwender nach einem Maximalpreis fragen, den er höchstens für den Autokauf aufwenden will.
    Das Programm soll nun alle Fahrzeuge mit ihren Eigenschaften ausgeben, deren Preis kleiner oder gleich wie der Maximalpreis ist.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.86-87). Kindle-Version.
"""

def main():
    fahrzeug1 = ["VW", "Golf", 2011, 5000]
    fahrzeug2 = ["Renault", "Clio", 2013, 6000]
    fahrzeug3 = ["Porsche", "Panamera", 2014, 25000]
    listeFahrzeuge = [fahrzeug1, fahrzeug2, fahrzeug3]

    maxpreis = eval(input("Geben Sie bitte den Maximalpreis ein: "))

    if listeFahrzeuge[0][3] <= maxpreis:
        print ("Marke: ",listeFahrzeuge[0][0])
        print ("Modell: ",listeFahrzeuge[0][1])
        print ("Baujahr: ",listeFahrzeuge[0][2])
        print ("Preis: ",listeFahrzeuge[0][3], "\n")

    if listeFahrzeuge[1][3] <= maxpreis:
        print ("Marke: ",listeFahrzeuge[1][0])
        print ("Modell: ",listeFahrzeuge[1][1])
        print ("Baujahr: ",listeFahrzeuge[1][2])
        print ("Preis: ",listeFahrzeuge[1][3], "\n")

    if listeFahrzeuge[2][3] <= maxpreis:
        print ("Marke: ",listeFahrzeuge[2][0])
        print ("Modell: ",listeFahrzeuge[2][1])
        print ("Baujahr: ",listeFahrzeuge[2][2])
        print ("Preis: ",listeFahrzeuge[2][3], "\n")

if __name__ == "__main__":
    main()