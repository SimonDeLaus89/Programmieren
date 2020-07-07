"""
2.  Suchen Sie eine Funktion, die das aktuelle Datum und die Uhrzeit wiedergibt.
    Lesen Sie in der Standardbibliothek nach, wie der Wert, den die Funktion zurückgibt, aufgebaut ist und geben Sie Datum und Uhrzeit nach deutscher Schreibweise aus.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.134-135). Kindle-Version.
"""


import time

def main():
    x = time.localtime()
    print("Heute ist der {:02d}.{:02d}.{:02d}! Es ist {:02d}:{:02d} Uhr!".format(x[2], x[1], x[0], x[3], x[4]))

if(__name__ == "__main__"):
    main()