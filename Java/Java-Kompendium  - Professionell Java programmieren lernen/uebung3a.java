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

        System.out.println("Gesamter Kurs: " + Arrays.toString(kurs));
        System.out.println("Erster Eintrag: " + kurs[0]);
        System.out.println("Letzter Eintrag: " + kurs[5]);

        kurs[2] = "Simon";
        System.out.println("Neue Kursliste: " + Arrays.toString(kurs));
    }
}