"""
1.  Erstellen Sie ein Programm, das die Quadratzahlen von 1 bis 10 ausgibt.
    Verwenden Sie hierfür einmal eine while-Schleife und einmal eine for-Schleife.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.104). Kindle-Version.
"""

def main():
    i = 0
    print("Do-While-Schleife:")
    while True:
        i += 1
        print("Quadrat von {} = {}".format(i, i*i))
        if(i > 9):
            break

    i = 0
    print("\nWhile-Schleife:")
    while(i < 0):
        i += 1
        print("Quadrat von {} = {}".format(i, i*i))

    print("\nFor-Schleife:")
    for i in range (1, 11):
        print("Quadrat von {} = {}".format(i, i*i))

if(__name__ == "__main__"):
    main()