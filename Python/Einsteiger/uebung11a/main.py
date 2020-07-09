"""
1.  Gestalten Sie ein Fenster, das zwei Eingabefelder enthält, in die der Anwender jeweils eine Zahl einfügen soll.
    Danach folgt ein Button und dann ein weiteres Eingabefeld.
    Wenn der Anwender den Button drückt, soll das Programm die Werte der beiden Felder addieren und mit dem insert-Befehl im letzten Eingabefeld ausgeben.
    Dieser muss als Parameter zunächst die Zahl 0 erhalten, damit das Ergebnis an der ersten Position des Feldes angezeigt wird.
    Danach folgt die Ausgabe – also das Ergebnis der Addition. Ordnen Sie die einzelnen Elemente mit dem place-Manager an.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.220-221). Kindle-Version.
"""

import tkinter as tk
import mainApp as app

if(__name__ == "__main__"):
    root = tk.Tk()
    app.MainApplication(root).pack()
    root.mainloop()