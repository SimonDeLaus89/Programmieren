"""
2.    Wählen Sie aus der vorherigen Aufgabe eine Datenstruktur aus, die Ihnen als besonders geeignet erscheint.
      Speichern Sie nun die Bücher in einer übergeordneten Datenstruktur ab.
      Auch hier sollen bei der Ausgabe alle Werte in einer eignen Zeile stehen.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.69-70). Kindle-Version.
"""

def main():
    buch1Dict = {"Titel": "Das Erbe der Macht", "Autor": "Andreas Suchanek", "Artikelnummer": 120512, "Preis": 17.99}
    buch2Dict = {"Titel": "Game of Thrones", "Autor": "George R. R. Martin", "Artikelnummer": 120708, "Preis": 25.99}
    buch3Dict = {"Titel": "Der Herr der Ringe", "Autor": "J. R. R. Tolkien", "Artikelnummer": 298765, "Preis": 24.99}

    buecher = [buch1Dict, buch2Dict, buch3Dict]

    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buecher[0]["Titel"], buecher[0]["Autor"], buecher[0]["Artikelnummer"],buecher[0]["Preis"]))
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buecher[1]["Titel"], buecher[1]["Autor"], buecher[1]["Artikelnummer"],buecher[1]["Preis"]))
    print("Titel: {}\nAutor: {}\nArtikelnummer: {}\nPreis: {}\n".format(buecher[2]["Titel"], buecher[2]["Autor"], buecher[2]["Artikelnummer"], buecher[2]["Preis"]))

if __name__ == "__main__":
    main()