"""
1.  Stellen Sie sich vor, Sie möchten ein Spiel programmieren.
    Dieses soll einen Würfel enthalten, der zufällig eine Zahl zwischen 1 und 6 ausgibt.
    Suchen Sie in der Standardbibliothek nach einer passenden Funktion für Zufallszahlen und erstellen Sie ein Programm das in der Funktion würfeln den entsprechenden Wert ermittelt.
    Das Hauptprogramm soll lediglich das Ergebnis ausgeben.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.133-134). Kindle-Version.
"""

import random

def main():
    print("Du hast eine {} gewürfelt!".format(random.randint(1,6)))

if(__name__ == "__main__"):
    main()