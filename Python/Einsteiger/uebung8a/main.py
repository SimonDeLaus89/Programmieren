"""
1.  Stellen Sie sich vor, Sie schreiben ein Programm für einen Anbieter für Ferienwohnungen, das auf der Klasse Wohnung beruhen soll.
    Diese soll den Namen der Wohnung, den Standort, die Anzahl der Betten, und den Preis pro Übernachtung enthalten.
    Schreiben Sie danach passende Methoden, um die Werte abzurufen und falls notwendig zu verändern.
    Erstellen Sie anschließend ein Hauptprogramm, das einige Objekte erzeugt und anschließend ihre Werte ausgibt.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.160-161). Kindle-Version.
"""

from wohnung import Wohnung

def main():
    x = Wohnung("Meerblick", "Sylt", 4, 69)
    y = Wohnung("Alpen-Panorama", "Füssen", 5, 74)
    z = Wohnung("Am Seeufer", "Konstanz", 3, 58)

    print("{}\n{}\n{}\n".format(x, y, z))

if(__name__ == "__main__"):
    main()