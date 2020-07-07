"""
1.  Gestalten Sie ein Fenster, das zwei Eingabefelder enthält, in die der Anwender jeweils eine Zahl einfügen soll.
    Danach folgt ein Button und dann ein weiteres Eingabefeld.
    Wenn der Anwender den Button drückt, soll das Programm die Werte der beiden Felder addieren und mit dem insert-Befehl im letzten Eingabefeld ausgeben.
    Dieser muss als Parameter zunächst die Zahl 0 erhalten, damit das Ergebnis an der ersten Position des Feldes angezeigt wird.
    Danach folgt die Ausgabe – also das Ergebnis der Addition. Ordnen Sie die einzelnen Elemente mit dem place-Manager an.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.220-221). Kindle-Version.
"""

import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Addieren")
        self.parent.geometry("300x300")

        self.border = tk.Frame(self.parent, relief = "ridge", borderwidth = 5)
        self.border.pack(fill = "both", expand = 1)

        self.label1 = tk.Label(self.border, text = "Zahl 1:")
        self.label1.place(x = 20, y = 30)

        self.label2 = tk.Label(self.border, text = "Zahl 2:")
        self.label2.place(x = 170, y = 30)

        self.label3 = tk.Label(self.border, text = "Ergebnis:")
        self.label3.place(x = 50, y = 180)

        self.input1 = tk.Entry(self.border, bd = 2, width = 10)
        self.input1.place(x = 20, y = 70)

        self.input2 = tk.Entry(self.border, bd = 2, width = 10)
        self.input2.place(x = 170, y = 70)

        self.output = tk.Entry(self.border, bd = 2, width = 10)
        self.output.place(x = 120, y = 180)

        self.button = tk.Button(self.border, text = "Addieren", command = self.addieren)
        self.button.place (x = 100, y = 120)

    def addieren(self):
        try:
            num1 = int(self.input1.get())
            num2 = int(self.input2.get())

            self.input1.delete(0,'end')
            self.input2.delete(0,'end')
            self.output.delete(0,'end')
            self.output.insert(0, num1 + num2)

        except:
            self.input1.delete(0,'end')
            self.input2.delete(0,'end')
            self.output.delete(0,'end')
            self.output.insert(0, "Error!")

if(__name__ == "__main__"):
    root = tk.Tk()
    MainApplication(root).pack()
    root.mainloop()