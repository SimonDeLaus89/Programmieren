"""
1.  Schreiben Sie ein Programm, das zwei Zahlen vom Benutzer abfragt und anschließend die erste Zahl durch die zweite teilt.
    Das Programm soll zwei Ausnahmen enthalten: eine für den Fall, dass der Anwender als zweite Zahl 0 eingibt und die andere, wenn er anstatt einer Zahl eine Zeichenkette eingibt.
    Abschließend sollen alle weiteren Ausnahmen abgefangen und dabei die Art des Fehlers ausgegeben werden.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.180-181). Kindle-Version.
"""

import sys

def main():
    try:
        x = eval(input("Geben Sie den Dividenden ein: "))
        y = eval(input("Geben Sie den Divisor Zahl ein: "))
        print("Quotient: {}".format(x / y))
    except ZeroDivisionError:
        print("Der Divisor darf nicht 0 sein.")
    except TypeError:
        print("Sie müssen Zahlen eingeben.")
    except:
        print ("Folgender Fehler ist aufgetreten: {}", sys.exc_info()[0])        

if(__name__ == "__main__"):
    main()