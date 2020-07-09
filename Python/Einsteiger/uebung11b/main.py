"""
2.  Erstellen Sie eine Checkbox und einen Button.
    Wenn der Anwender den Button drückt, soll ein neues Fenster mit einer beliebigen Nachricht geöffnet werden – allerdings nur, wenn die Checkbox zuvor ausgewählt wurde.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.221-222). Kindle-Version.
"""

import tkinter as tk
import mainApp as app

if(__name__ == "__main__"):
    root = tk.Tk()
    app.MainApplication(root).pack()
    root.mainloop()