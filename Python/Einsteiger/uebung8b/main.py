"""
2.  In Kapitel 11.7. wurde nur eine einzige Unterklasse von der Klasse Auto abgeleitet.
    Erstellen sie nun die Klasse Kombi, die sich ebenfalls von der Klasse Auto ableitet und die zusätzlich zu deren Werten den Kofferrauminhalt angibt. Gestalten Sie ein Hauptprogramm, das ein entsprechendes Objekt erzeugt und dessen Werte ausgibt.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.161-162). Kindle-Version.
"""

from suv import SUV
from kombi import Kombi

def main():
    x = SUV("Land Rover", "Range Rover", 2019, 89989, True)
    y = Kombi("Volkswagen", "Passat", 2016, 21990, 650)
    print("SUV: {}\nKombi: {}".format(x, y))

if(__name__ == "__main__"):
    main()