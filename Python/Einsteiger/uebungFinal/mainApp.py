import tkinter as tk
from showSortiment import ShowSortiment as show
from addCar import AddCar as add
from sellCar import SellCar as sell
from changePrice import ChangePrice as change

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("UebungFinal")
        self.parent.geometry("700x350")
        self.parent.minsize(700, 350)
        self.parent.maxsize(700, 350)

        self.border = tk.Frame(self.parent, relief = "ridge", borderwidth = 5)
        self.border.pack(fill = "both", expand = 1)

        self.buttonShow = tk.Button(self.border,text="Sortiment anzeigen", width = 20, height = 5, command = show)
        self.buttonShow.config(font=("Arial", 12, "bold"))
        self.buttonShow.place(relx = 0.1, rely = 0.1, anchor = tk.NW)

        self.buttonAdd = tk.Button(self.border,text="Fahrzeug hinzufügen", width = 20, height = 5, command = add)
        self.buttonAdd.config(font=("Arial", 12, "bold"))
        self.buttonAdd.place(relx = 0.9, rely = 0.1, anchor = tk.NE)

        self.buttonSell = tk.Button(self.border,text="Fahrzeug verkaufen", width = 20, height = 5, command = sell)
        self.buttonSell.config(font=("Arial", 12, "bold"))
        self.buttonSell.place(relx = 0.1, rely = 0.9, anchor = tk.SW)

        self.buttonChange = tk.Button(self.border,text="Preis ändern", width = 20, height = 5, command = change)
        self.buttonChange.config(font=("Arial", 12, "bold"))
        self.buttonChange.place(relx = 0.9, rely = 0.9, anchor = tk.SE)

        self.buttonQuit = tk.Button(self.border,text="Beenden", command = self.parent.destroy)
        self.buttonQuit.config(font=("Arial", 12, "bold"))
        self.buttonQuit.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)