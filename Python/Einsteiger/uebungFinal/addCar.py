import tkinter as tk
from tkinter import messagebox as mb

class AddCar(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("UebungFinal")
        self.geometry("550x400")
        self.minsize(550, 400)
        self.maxsize(550, 400)
        self.focus_force()

        self.border = tk.Frame(self, relief = "ridge", borderwidth = 5)
        self.border.pack(fill = "both", expand = 1)

        self.label1 = tk.Label(self.border, text = "Geben Sie die Daten des Autos ein:")
        self.label1.config(font = ("Arial", 14, "bold"))
        self.label1.place(x = 50, y = 10)

        self.artNum = tk.StringVar()
        self.artNum.set("")
        self.lblArtNum = tk.Label(self.border, text = "Artikelnummer:")
        self.lblArtNum.place(x = 100, y = 100)
        self.tbxArtNum = tk.Entry(self.border, bd = 2, width = 22, textvariable = self.artNum)
        self.tbxArtNum.place(x = 200, y = 100)

        self.marke = tk.StringVar()
        self.marke.set("")
        self.lblMarke = tk.Label(self.border, text = "Marke:")
        self.lblMarke.place(x = 100, y = 140)
        self.tbxMarke = tk.Entry(self.border, bd = 2, width = 22, textvariable = self.marke)
        self.tbxMarke.place(x = 200, y = 140)

        self.modell = tk.StringVar()
        self.modell.set("")
        self.lblModell = tk.Label(self.border, text = "Modell:")
        self.lblModell.place(x = 100, y = 180)
        self.tbxModell = tk.Entry(self.border, bd = 2, width = 22, textvariable = self.modell)
        self.tbxModell.place(x = 200, y = 180)

        self.baujahr = tk.StringVar()
        self.baujahr.set("")
        self.lblBaujahr = tk.Label(self.border, text = "Baujahr:")
        self.lblBaujahr.place(x = 100, y = 220)
        self.tbxBaujahr = tk.Entry(self.border, bd = 2, width = 22, textvariable = self.baujahr)
        self.tbxBaujahr.place(x = 200, y = 220)

        self.preis = tk.StringVar()
        self.preis.set("")
        self.lblPreis = tk.Label(self.border, text = "Preis:")
        self.lblPreis.place(x = 100, y = 260)
        self.tbxPreis = tk.Entry(self.border, bd = 2, width = 22, textvariable = self.preis)
        self.tbxPreis.place(x = 200, y = 260)

        self.btnSave = tk.Button(self.border, bd = 2, width = 22, text = "Eingabe", command = self.add)
        self.btnSave.place(x = 200, y = 320)

        self.btnQuit = tk.Button(self.border, text = "Schließen", command = self.destroy)
        self.btnQuit.place(x = 100, y = 320)

        self.grab_set()

    def add(self):
        if((self.tbxArtNum.get() != "") and (self.tbxMarke.get() != "") and (self.tbxModell.get() != "") and (self.tbxBaujahr.get() != "") and (self.tbxPreis.get() != "")):
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
                    break

            if(not hlp):
                f = open('Python\\Einsteiger\\uebungFinal\\sortiment.txt','a')
                f.write("{};{};{};{};{}\n".format(self.tbxArtNum.get(), self.tbxMarke.get(), self.tbxModell.get(), self.tbxBaujahr.get(), self.tbxPreis.get()))
                f.close()

                self.artNum.set("")
                self.marke.set("")
                self.modell.set("")
                self.baujahr.set("")
                self.preis.set("")

            else:
                mb.showerror("UebungFinal", "Artikelnummer bereits vorhanden.")
                self.focus_force()

        else:
            if(self.tbxArtNum.get() == ""):
                mb.showerror("UebungFinal", "Artikelnummer angeben!")
                self.focus_force()
            elif(self.tbxMarke.get() == ""):
                mb.showerror("UebungFinal", "Marke angeben!")
                self.focus_force()
            elif(self.tbxModell.get() == ""):
                mb.showerror("UebungFinal", "Modell angeben!")
                self.focus_force()
            elif(self.tbxBaujahr.get() == ""):
                mb.showerror("UebungFinal", "Baujahr angeben!")
                self.focus_force()
            elif(self.tbxPreis.get() == ""):
                mb.showerror("UebungFinal", "Preis angeben!")
                self.focus_force()