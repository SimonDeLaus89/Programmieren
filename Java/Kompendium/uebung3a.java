/*
1.  Erstellen Sie ein Programm, das ein Array aus sechs String-Variablen erzeugt.
    Dieses soll die Vornamen der Teilnehmer an einem Sprachkurs enthalten.
    Geben Sie das gesamte Array sowie den ersten und den letzten Namen der Liste aus.
    Ändern Sie danach einen beliebigen Eintrag und geben Sie das Array erneut aus.

Neumann, Markus. Java: Kompendium: Professionell Java programmieren lernen (German Edition) (S.80). Kindle-Version.
*/

import java.util.*;

public class uebung3a {
    public static void main(String[] args)
    {
        String[] kurs = {"Paul","Melanie","Nadine","Thorsten","Kevin","Daniel"};

        System.out.printf("Gesamter Kurs: %s\n", Arrays.toString(kurs));
        System.out.printf("Erster Eintrag: %s\n", kurs[0]);
        System.out.printf("Letzter Eintrag: %s\n", kurs[5]);

        kurs[2] = "Simon";
        System.out.printf("Neue Kursliste: %s\n", Arrays.toString(kurs));
    }
}