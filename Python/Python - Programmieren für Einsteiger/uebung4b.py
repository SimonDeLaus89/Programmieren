"""
2.  Schreiben Sie ein Programm, das dem Anwender fünf einfache Rechenaufgaben stellt.
    Überprüfen Sie die Eingabe. Wenn das Ergebnis richtig ist, erhält der Anwender einen Punkt.
    Erstellen Sie nach dem Ende der Aufgaben eine Bewertung:
        Bei 0 Punkten: Dringend Nachhilfe benötigt!
        Bei 1 bis 2 Punkten: Viele Fehler: weitere Übung erforderlich!
        Bei 3 bis 4 Punkten: Gute Leistung!
        Bei 5 Punkten: Super! Alle Aufgaben richtig gelöst!

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.87). Kindle-Version.
"""

def main():
    punkte = 0

    if(eval(input("Was ist 1+1? ")) == 2):
        punkte += 1

    if(eval(input("Was ist 1*1? ")) == 1):
        punkte += 1

    if(eval(input("Was ist 1-1? ")) == 0):
        punkte += 1

    if(eval(input("Was ist 1/1? ")) == 1):
        punkte += 1

    if(eval(input("Was ist 17+4? ")) == 21):
        punkte += 1

    if(punkte == 0):
        print("{} Punkte. Dringend Nachhilfe benötigt!".format(punkte))
    elif(punkte == 1):
        print("{} Punkt. Viele Fehler: weitere Übung erforderlich!".format(punkte))
    elif(punkte == 2):
        print("{} Punkt. Viele Fehler: weitere Übung erforderlich!".format(punkte))
    elif(punkte > 2 and punkte < 5):
        print("{} Punkte. Gute Leistung!".format(punkte))
    else:
        print("{} Punkte. Super! Alle Aufgaben richtig gelöst!".format(punkte))

if __name__ == "__main__":
    main()