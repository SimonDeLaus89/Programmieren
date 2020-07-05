/*
1.  Gestalten Sie ein Programm, das die Zahlen 3 und 3,5 jeweils in einer Variablen speichert und die Werte anschließend addiert.
    Das Ergebnis soll in einer weiteren Variablen als Fließkommazahl gespeichert und anschließend auf dem Bildschirm ausgegeben werden.
    Wiederholen Sie diesen Vorgang, speichern Sie dabei dieses Mal jedoch nur den ganzzahligen Teil in der Variablen ab.

Bonacina, Michael. Java Programmieren: für Einsteiger: Der leichte Weg zum Java-Experten (2. Auflage: komplett neu verfasst) (Einfach Programmieren lernen 1) (German Edition) (S.58). Kindle-Version.

*/

public class uebung2a
{
    public static void main(final String[] args)
    {
        int x = 3;
        double y = 3.5;

        double z1 = x + y;
        System.out.printf("Ergebnis: %.1f\n", z1);

        int z2 = (int) (x + y);
        System.out.printf("Ergebnis: %d", z2);
    }
}