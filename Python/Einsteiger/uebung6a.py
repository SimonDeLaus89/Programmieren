"""
1.  Schreiben Sie ein Programm, das zwei Zahlen vom Anwender abfragt.
    Dieses soll nun eine Funktion aufrufen, die die Werte zwischen der ersten und der zweiten Zahl in Zweierschritten ausgibt.
    Für diese Ausgabe müssen zwei verschiedene Optionen bestehen – je nachdem, ob die erste oder die zweite Zahl größer ist.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.123). Kindle-Version.
"""

def anzeigeMinus(x, y):
    for i in range (x, y - 1, -2):
        print("{}".format(i))

def anzeigePlus(x, y):
    while (x <= y):
        print("{}".format(x))
        x += 2

def main():
    x = eval(input("Geben Sie eine Zahl ein: "))
    y = eval(input("Geben Sie eine weitere Zahl ein: "))

    if(x < y):
        anzeigePlus(x, y)
    else:
        anzeigeMinus(x, y)

if(__name__ == "__main__"):
    main()