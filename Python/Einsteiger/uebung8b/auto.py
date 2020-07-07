class Auto:
    anzahl = 0
    def __init__(self, ma, mo, bj, pr):
        self.__Marke = ma
        self.__Modell = mo
        self.__Baujahr = bj
        self.__Preis = pr

        Auto.anzahl += 1

    def __del__(self):
        Auto.anzahl -= 1

    def __str__(self):
        tmp = "Marke: {}\nModell:{}\nBaujahr: {}\nPreis: {} €\n"
        return tmp.format(self.getMarke(), self.getModell(), self.getBaujahr(), self.getPreis())

    def getMarke(self):
        return self.__Marke

    def getModell(self):
        return self.__Modell

    def getBaujahr(self):
        return self.__Baujahr

    def getPreis(self):
        return self.__Preis

    def setPreis(self, preis_neu):
        if(preis_neu <= (self.__Preis * 1.05)):
            self.__Preis = preis_neu
        else:
            print("Der Preis würde um mehr als 5% erhöht werden.")
            bestaetigung = input("{} als neuen Preis festlegen? (ja/nein) ".format(preis_neu))
            if bestaetigung == "ja":
                self.__Preis = preis_neu