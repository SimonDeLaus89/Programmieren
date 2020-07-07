""""
1.  Schreiben Sie ein Programm, das es erlaubt, eine Gästeliste für Ihre nächste Geburtstagsparty zu gestalten.
    Dieses soll eine Schleife enthalten, in der Sie beliebig viele Namen eintragen können.
    Sollte vor dem Aufruf des Programms bereits eine Gästeliste bestehen, dann sollen die neuen Namen an die bisherige Datei angehängt werden.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.197). Kindle-Version.
"""

def delGast():
    f = open('Python\\Einsteiger\\uebung10\\gaeste.txt','r')
    x = f.readlines()
    f.close()

    print("Geladene Gäste:")
    for i in x:
        print("{}".format(i[:-1]))

    while True:
        eingabe = input("Welchen Gast möchten Sie entfernen?: ")
        if(eingabe == "quit"):
            break
        else:
            if(("{}\n".format(eingabe)) in x):
                print("{} von der Gästeliste entfernt.".format(eingabe))
                x.remove(("{}\n".format(eingabe)))
            else:
                print("Person war nicht auf der Gästeliste")

    f = open('Python\\Einsteiger\\uebung10\\gaeste.txt','w')
    for i in x:
        f.write("{}".format(i))
    f.close()

def addGast():
    f = open('Python\\Einsteiger\\uebung10\\gaeste.txt','a')

    while True:
        eingabe = input("Fügen Sie einen neuen Namen hinzu. (Zum Abbrechen 'quit' eingeben): ")

        if(eingabe == "quit"):
            break
        else:
            print("{} auf die Gästeliste gesetzt.".format(eingabe))
            f.write("{}\n".format(eingabe))

    f.close()

def main():
    x = 0;
    while(x != 1 and x != 2):
        x = eval(input("Was möchten Sie tun?\n 1 - Gäste hinzufügen\n 2 - Gäste entfernen\n Auswahl: "))
        if(x != 1 and x != 2):
            print("Auswahl nicht verfügbar. Bitte wiederholen.\n")

    if(x == 1):
        print("\n")
        addGast()
    else:
        print("\n")
        delGast()

if(__name__ == "__main__"):
    main()