/*
1.  Ein Händler nimmt Bestellungen für ein bestimmtes Produkt entgegen.
    Dabei speichert er die gewünschte Anzahl in der Variablen bestellmenge.
    Die Zahl der verfügbaren Produkte wird in der Variablen bestand vermerkt.
    Außerdem nutzt das Programm die boolesche Variable zahlung, in der vermerkt ist, ob der Artikel bereits bezahlt wurde.
    Das Programm soll nun überprüfen, ob die gewünschte Anzahl verfügbar ist und ob die Zahlung eingegangen ist.
    In diesem Fall gibt es zurück, dass die Ware versendet wird. Ist die benötigte Anzahl vorhanden, die Zahlung jedoch noch nicht eingegangen, soll es den Kunden darauf hinweisen, dass der Artikel nach Zahlungseingang verschickt wird.
    Wenn nicht genügend Artikel vorhanden sind, wird der Käufer darüber informiert, wie viele Einheiten noch verfügbar sind.

Bonacina, Michael. Java Programmieren: für Einsteiger: Der leichte Weg zum Java-Experten (2. Auflage: komplett neu verfasst) (Einfach Programmieren lernen 1) (German Edition) (S.72). Kindle-Version.
*/

public class uebung3a
{
    public static void main(String[] args) throws Exception
    {
        int bestellmenge = 19;
        int bestand = 20;
        boolean zahlung = false;

        if (bestellmenge > bestand)
        {
            System.out.printf("Nicht genügend Einheiten auf Lager. Es sind nur noch %d Einheiten verfügbar\n", bestand);
        }
        else if(zahlung)
        {
            System.out.println("Geldeingang bestätigt. Ware wird versendet.");
        }
        else
        {
            System.out.println("Auf Zahlung wird gewartet.");
        }


    }
}