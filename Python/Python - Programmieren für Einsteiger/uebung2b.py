"""
2.    Schreiben Sie ein Programm, das den Anwender dazu auffordert, einen beliebigen Inhalt einzugeben.
      Speichern Sie den Wert in einer Variablen und geben Sie anschließend ihren Datentyp aus.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.54-55). Kindle-Version.
"""


def main():
    x = eval(input("Geben Sie etwas ein: "))

    print("Type: {}".format(type(x)))

if(__name__ == "__main__"):
    main()