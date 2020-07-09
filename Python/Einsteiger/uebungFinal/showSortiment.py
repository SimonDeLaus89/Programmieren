import tkinter as tk
from tkinter import messagebox as mb

class ShowSortiment(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("UebungFinal")
        self.geometry("500x400")
        self.minsize(500, 400)
        self.maxsize(500, 400)
        self.focus_force()

        self.border1 = tk.Frame(self, relief = "ridge", borderwidth = 5)
        self.border1.pack(fill = "both", expand = 1)

        self.label1 = tk.Label(self.border1, text = "Das aktuelle Sortiment:")
        self.label1.config(font = ("Arial", 14, "bold"))
        self.label1.pack(pady = 20)

        self.border2 = tk.Frame(self.border1, relief = "ridge", borderwidth = 5)
        self.border2.pack(pady = 20, padx = 30)

        try:
            f = open('Python\\Einsteiger\\uebungFinal\\sortiment.txt','r')
            content = f.readlines()
            f.close()
        except:
            content = ""

        self.scrollbar = tk.Scrollbar(self.border2)
        self.list = tk.Listbox(self.border2, yscrollcommand = self.scrollbar.set, width = 50)

        i = 0
        for line in content:
            lineSingle = line.split(";")
            for item in lineSingle:
                if(i == 0):
                    output = "Artikelnummer: {}".format(item)
                    i += 1

                elif(i == 1):
                    output = "Marke: {}".format(item)
                    i += 1

                elif(i == 2):
                    output = "Modell: {}".format(item)
                    i += 1

                elif(i == 3):
                    output = "Baujahr: {}".format(item)
                    i += 1

                elif(i == 4):
                    output = "Preis: {}".format(item)
                    i = 0

                self.list.insert(tk.END, output)
            self.list.insert(tk.END, "")
        if(self.list.size() == 0):
            mb.showinfo("UebungFinal", "Derzeit kein Auto verfügbar")
            self.focus_force()

        self.scrollbar.config(command = self.list.yview)
        self.list.pack(side="left", fill = "both")
        self.scrollbar.pack(side = "left", fill = "y")

        self.button = tk.Button(self.border1,text = "OK", command = self.destroy, width = 10, height = 2)
        self.button.config(font=("Arial", 10))
        self.button.pack(pady = 10)

        self.grab_set()