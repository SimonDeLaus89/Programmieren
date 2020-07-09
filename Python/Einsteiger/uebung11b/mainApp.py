import tkinter as tk
from tkinter import messagebox as mb

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Uebung11b")
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
            mb.showinfo("Uebung11b", "Checkbox wurde ausgewählt!")