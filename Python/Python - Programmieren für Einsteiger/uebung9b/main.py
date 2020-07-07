"""
2.  Erstellen Sie ein Programm, das den Anwender dazu auffordert, ein Wort mit einer geraden Anzahl an Buchstaben einzugeben.
    Danach soll das Programm daraus zwei Strings gestalten, die jeweils eine Hälfte des Worts enthalten und diese dann ausgeben.
    Das Programm soll eine selbst definierte Ausnahme aufwerfen, wenn die Anzahl der Buchstaben ungerade ist.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.181). Kindle-Version. 
"""

from exception import OddError

def main():
    try:
        x = input("Geben Sie ein Wort mit gerader Anzahl an Buchstaben ein: ")
        if((len(x) % 2) != 0):
            raise OddError()
        else:
            a = x[:int(len(x) / 2)]
            b = x[int(len(x) / 2):]
            print("Teil 1: {}\nTeil 2: {}".format(a, b))
                
    except OddError:
        print("Das Wort {} hat eine ungerade Anzahl an Buchtaben!".format(x))

if(__name__ == "__main__"):
    main()