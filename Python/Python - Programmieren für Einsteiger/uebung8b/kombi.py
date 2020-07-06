from auto import Auto

class Kombi(Auto):
    def __init__(self, ma, mo, bj, pr, volumen):
        Auto.__init__(self, ma, mo, bj, pr)
        self.__Ladevolumen = volumen

    def __str__(self):
        tmp = "Marke: {}\nModell:{}\nBaujahr: {}\nVolumen: {} l\nPreis: {} €\n"
        return tmp.format(self.getMarke(), self.getModell(), self.getBaujahr(), self.getVolumen(), self.getPreis())

    def getVolumen(self):
            return self.__Ladevolumen