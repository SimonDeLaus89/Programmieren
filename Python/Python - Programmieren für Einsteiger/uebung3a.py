"""
1.    Stellen Sie sich vor, Sie schreiben ein Programm für die Verwaltung der Bestände eines Buchhändlers.
      Zu jedem Buch sollen der Titel, der Autor, eine Artikelnummer und der Preis gespeichert werden.
      Schreiben Sie drei Programme, die jeweils eine Liste, ein Dictionary beziehungsweise ein Tupel verwenden.
      Jedes Programm soll die Werte für drei Bücher abspeichern und die Daten anschließend auf dem Bildschirm ausgeben.
      Die Ausgabe soll dabei nicht als komplette Liste erfolgen, sondern jeder Wert soll in einer eigenen Zeile stehen.
      Nach jedem Buch soll eine Leerzeile folgen. Dazu dient das Zeichen \n.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.69). Kindle-Version.
"""

def main():
    buch1List = ["Das Erbe der Macht", "Andreas Suchanek", 120512, 17.99]
    buch2List = ["Game of Thrones", "George R. R. Martin", 120708, 25.99]
    buch3List = ["Der Herr der Ringe", "J. R. R. Tolkien", 298765, 24.99]

    buch1Dict = {"Titel": "Das Erbe der Macht", "Autor": "Andreas Suchanek", "Artikelnummer": 120512, "Preis": 17.99}
    buch2Dict = {"Titel": "Game of Thrones", "Autor": "George R. R. Martin", "Artikelnummer": 120708, "Preis": 25.99}
    buch3Dict = {"Titel": "Der Herr der Ringe", "Autor": "J. R. R. Tolkien", "Artikelnummer": 298765, "Preis": 24.99}

    buch1Tuple = ("Das Erbe der Macht", "Andreas Suchanek", 120512, 17.99)
    buch2Tuple = ("Game of Thrones", "George R. R. Martin", 120708, 25.99)
    buch3Tuple = ("Der Herr der Ringe", "J. R. R. Tolkien", 298765, 24.99)

    print("List:")
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buch1List[0], buch1List[1], buch1List[2], buch1List[3]))
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buch2List[0], buch2List[1], buch2List[2], buch2List[3]))
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buch3List[0], buch3List[1], buch3List[2], buch3List[3]))

    print("Dict:")
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buch1Dict["Titel"], buch1Dict["Autor"], buch1Dict["Artikelnummer"], buch1Dict["Preis"]))
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buch2Dict["Titel"], buch2Dict["Autor"], buch2Dict["Artikelnummer"], buch2Dict["Preis"]))
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buch3Dict["Titel"], buch3Dict["Autor"], buch3Dict["Artikelnummer"], buch3Dict["Preis"]))


    print("Tuple:")
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buch1Tuple[0], buch1Tuple[1], buch1Tuple[2], buch1Tuple[3]))
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buch2Tuple[0], buch2Tuple[1], buch2Tuple[2], buch2Tuple[3]))
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buch3Tuple[0], buch3Tuple[1], buch3Tuple[2], buch3Tuple[3]))

if(__name__ == "__main__"):
    main()