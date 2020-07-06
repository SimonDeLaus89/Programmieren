"""
2.  Schreiben Sie ein Programm, das den Anwender dazu auffordert, einen Nutzernamen und ein Passwort einzugeben.
    Nehmen Sie diese Werte auf und leiten Sie sie an eine Funktion weiter.
    Erfinden Sie einige Kombinationen aus Nutzernamen und Passwörtern.
    Schreiben Sie diese zu Beginn der Funktion in eine Liste, die wiederum aus Tupeln mit den entsprechenden Kombinationen besteht.
    Die Funktion soll nun die Liste durchgehen und überprüfen, ob das entsprechende Paar aus Nutzername und Passwort darin enthalten ist.
    Trifft dies zu, soll es eine Erfolgsmeldung ausgeben.
    Trifft das nicht zu, soll es dem Anwender mitteilen, dass die Registrierung fehlgeschlagen ist.

Bonacina, Michael. Python 3: Programmieren für Einsteiger: Der leichte Weg zum Python-Experten (Einfach Programmieren lernen 2) (German Edition) (S.123). Kindle-Version.
"""

def login(name, pw):
    daten = [("karl01", "abcde"), ("*susi*", "qedX01"),("00xyz00", "a7r9f3"), ("martin.mueller", "martin")]
    for i in daten:
        if(i[0] == name):
            if(i[1] == pw):
                return True
            else:
                return False
    return False

def main():
    name = input("Geben Sie ihren Nutzernamen an: ")
    pw = input("Geben Sie ihr Passwort ein: ")

    if(login(name, pw)):
        print("Login erfolgreich")
    else:
        print("Login gescheitert")

if(__name__ == "__main__"):
    main()