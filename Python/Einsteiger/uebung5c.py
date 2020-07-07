"""
3.  Betrachten sie nochmals das Programm aus Kapitel 8.1., das eine durch den Anwender eingegebene Zahl verdoppelt.
    Schreiben Sie ein Programm, das genau die gleiche Funktion erfüllt, das als Bedingung jedoch den Ausdruck “True” verwendet.
    Dieser trifft immer zu.
    Verwenden Sie einen break-Befehl, um die Ausführung abzubrechen, wenn der Anwender dies wünscht.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.104-105). Kindle-Version.
"""

def main():
    x = eval(input("Geben Sie eine Zahl ein: "))
    while True:
        print("Doppelter Wert von {} = {}".format(x, x * 2))
        x *= 2
        y = input("Weiter? (ja/nein) ")
        if(y != "ja"):
            break

if(__name__ == "__main__"):
    main()