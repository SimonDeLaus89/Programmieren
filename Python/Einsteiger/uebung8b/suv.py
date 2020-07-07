from auto import Auto

class SUV(Auto):
    def __init__(self, ma, mo, bj, pr, allrad):
        Auto.__init__(self, ma, mo, bj, pr)
        if (allrad):
            self.__Allradantrieb = "Ja"
        else:
            self.__Allradantrieb = "Nein"

    def __str__(self):
        tmp = "Marke: {}\nModell:{}\nBaujahr: {}\nAllrad: {}\nPreis: {} €\n"
        return tmp.format(self.getMarke(), self.getModell(), self.getBaujahr(), self.getAllradantrieb(), self.getPreis())

    def getAllradantrieb(self):
            return self.__Allradantrieb