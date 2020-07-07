class Wohnung:
    def __init__(self, Name, ort, betten, preis):
        self.__Name = Name
        self.__Ort = ort
        self.__Betten =betten
        self.__Preis = preis

    def __str__(self):
        tmp = "Name: {}\nOrt: {}\n Bettenanzahl: {}\n Preis: {} €/Nacht!"
        return tmp.format(self.getName(), self.getOrt(), self.getBetten(), self.getPreis())

    def setName(self, Name):
        self.__Name = Name

    def getName(self):
        return self.__Name

    def setOrt(self, ort):
        self.__Ort = ort

    def getOrt(self):
        return self.__Ort

    def setBetten(self, betten):
        self.__Betten = betten

    def getBetten(self):
        return self.__Betten

    def setPreis(self, preis):
        self.__Preis = preis

    def getPreis(self):
        return self.__Preis