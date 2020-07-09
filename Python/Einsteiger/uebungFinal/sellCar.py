import tkinter as tk
from tkinter import messagebox as mb

class SellCar(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("UebungFinal")
        self.geometry("550x400")
        self.minsize(550, 400)
        self.maxsize(550, 400)
        self.focus_force()

        self.border = tk.Frame(self, relief = "ridge", borderwidth = 5)
        self.border.pack(fill = "both", expand = 1)

        self.label1 = tk.Label(self.border, text = "Geben Sie die Artikelnummer des Autos ein:")
        self.label1.config(font = ("Arial", 14, "bold"))
        self.label1.place(x = 50, y = 10)

        self.artNum = tk.StringVar()
        self.artNum.set("")
        self.lblArtNum = tk.Label(self.border, text = "Artikelnummer:")
        self.lblArtNum.place(x = 100, y = 100)
        self.tbxArtNum = tk.Entry(self.border, bd = 2, width = 22, textvariable = self.artNum)
        self.tbxArtNum.place(x = 200, y = 100)

        self.btnSave = tk.Button(self.border, bd = 2, width = 22, text = "Verkaufen", command = self.sell)
        self.btnSave.place(x = 200, y = 320)

        self.btnQuit = tk.Button(self.border, text = "Schließen", command = self.destroy)
        self.btnQuit.place(x = 100, y = 320)

        self.grab_set()

    def sell(self):
        if(self.tbxArtNum.get() != ""):
            try:
                f = open('Python\\Einsteiger\\uebungFinal\\sortiment.txt','r')
                content = f.readlines()
                f.close()
            except:
                content = ""

            hlp = False
            for i in range (0, len(content)):
                item = content[i].split(";")
                if(item[0] == self.artNum.get()):
                    hlp = True
                    content.remove(content[i])
                    self.artNum.set("")
                    break

            if(not hlp):
                mb.showinfo("UebungFinal", "Artikelnummer nicht im Sortiment!")
                self.focus_force()
            else:
                f = open('Python\\Einsteiger\\uebungFinal\\sortiment.txt','w')
                for i in content:
                    f.write("{}".format(i))
                f.close()

        else:
            if(self.tbxArtNum.get() == ""):
                mb.showerror("UebungFinal", "Keine Artikelnummer eingetragen!")
                self.focus_force()