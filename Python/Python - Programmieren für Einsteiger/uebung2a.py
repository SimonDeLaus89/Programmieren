"""
1.    Schreiben Sie ein Programm, das den Anwender dazu auffordert, zwei Zahlen einzugeben.
      Speichern Sie diese in zwei unterschiedlichen Variablen.
      Das Programm soll danach die beiden Werte addieren und ausgeben.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.54). Kindle-Version.
"""


def main():
    x = eval(input("Geben Sie eine erste Zahl ein: "))
    y = eval(input("Geben Sie eine zweite Zahl ein: "))

    z = x + y
    print("Summe: {}".format(z))

if(__name__ == "__main__"):
    main()