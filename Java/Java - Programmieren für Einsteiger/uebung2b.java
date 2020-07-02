/*
2.  Betrachten Sie nochmals das erste Programm dieses Lehrbuchs (Kapitel III.1.), das den Text "Herzlich Willkommen zum Java-Kurs!" ausgibt.
    Schreiben Sie ein Programm, das genau die gleiche Funktion erfüllt.
    Dabei soll jedoch ein Array gestaltet und dabei jedes einzelne Wort in einem Feld gespeichert werden.
    Geben Sie daraufhin die einzelnen Felder nacheinander aus.

Bonacina, Michael. Java Programmieren: für Einsteiger: Der leichte Weg zum Java-Experten (2. Auflage: komplett neu verfasst) (Einfach Programmieren lernen 1) (German Edition) (S.58-60). Kindle-Version.
*/

public class uebung2b
{
    public static void main(final String[] args)
    {
        String[] x = {"Herzlich", "Willkommen", "zum", "Java-Kurs!"};

        System.out.print(x[0] + " " + x[1] + " " + x[2] + " " + x[3]);
    }
}