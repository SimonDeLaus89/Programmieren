"""
2.  Erstellen Sie eine Liste mit 10 Städten.
    Geben Sie den gesamten Inhalt der Liste einmal mit einer while- und einmal mit einer for-Schleife aus.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.104). Kindle-Version.
"""

def main():
    x = ["Berlin", "Hamburg", "Köln", "Stuttgart", "Düsseldorf", "Frankfurt", "München", "Bremen", "Hannover", "Dresden"]

    i = 0
    print("Do-While-Schleife:")
    while True:
        print("{}".format(x[i]))
        i += 1
        if(i >= len(x)):
            break

    i = 0
    print("\nWhile-Schleife:")
    while(i < len(x)):
        print("{}".format(x[i]))
        i += 1

    print("\nFor-Schleife:")
    for i in x:
        print("{}".format(i))

if(__name__ == "__main__"):
    main()