"""
2.  Erstellen Sie eine Checkbox und einen Button.
    Wenn der Anwender den Button drückt, soll ein neues Fenster mit einer beliebigen Nachricht geöffnet werden – allerdings nur, wenn die Checkbox zuvor ausgewählt wurde.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.221-222). Kindle-Version.
"""

import tkinter as tk

class MsgBox(tk.Frame):
    def __init__(self, parent, text):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Message")
        self.parent.geometry("200x75")
        self.msg = text

        self.border = tk.Frame(self.parent, relief = "ridge", borderwidth = 5)
        self.border.pack(fill = "both", expand = 1)

        self.label1 = tk.Label(self.border, text = text)
        self.label1.pack()

        self.button = tk.Button(self.border, text = "Ok", command = self.parent.destroy)
        self.button.pack()

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Checkbox and Button!")
        self.parent.geometry("300x100")

        self.border = tk.Frame(self.parent, relief = "ridge", borderwidth = 5)
        self.border.pack(fill = "both", expand = 1)

        self.label1 = tk.Label(self.border, text = "Erst Checkbox, dann Button!")
        self.label1.pack()

        self.check = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(self.border, text = "Bestätigen", variable = self.check)
        self.checkbox1.pack()

        self.button = tk.Button(self.border, text = "Click", command = self.btnClick)
        self.button.pack()

    def btnClick(self):
        if(self.check.get()):
            popUp = tk.Tk()
            text = "Checkbox wurde ausgewählt!"
            MsgBox(popUp, text).pack()
            popUp.mainloop()

if(__name__ == "__main__"):
    root = tk.Tk()
    MainApplication(root).pack()
    root.mainloop()