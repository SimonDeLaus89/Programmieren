/*
3.  Eine Bildungseinrichtung bietet neben einem Java-Kurs noch einen Kurs für die Programmiersprache Python an.
    Speichern Sie die Teilnehmer jeweils in einer passenden Datenstruktur.
    Geben Sie daraufhin die Teilnehmer beider Kurse getrennt aus.
    Außerdem soll eine Liste mit allen Schülern der Bildungseinrichtung dargestellt werden.
    Die Namen der Teilnehmer, die beide Kurse besuchen, sollen darin nicht doppelt erscheinen.
    Listen Sie abschließend noch die Kursteilnehmer auf, die beide Bildungsangebote wahrnehmen.
    Wählen Sie eine Datenstruktur aus, die zu diesen Aufgaben passt.
    Anmerkung: Um diese Aufgabe sinnvoll zu erledigen, muss mindestens einer der Teilnehmer beide Kurse besuchen.

Neumann, Markus. Java: Kompendium: Professionell Java programmieren lernen (German Edition) (S.81-82). Kindle-Version.
*/

import java.util.*;

public class uebung3c {
    public static void main(String[] args)
    {
        HashSet<String> kursJava = new HashSet<>();
        HashSet<String> kursPython = new HashSet<>();
        HashSet<String> alleTeilnehmer = new HashSet<>();
        HashSet<String> teilnehmerBeideKurse = new HashSet<>();

        kursJava.add("Klaus");
        kursJava.add("Peter");
        kursJava.add("Sieglinde");
        kursJava.add("Simon");
        kursPython.add("Simon");
        kursPython.add("Paul");
        kursPython.add("Thomas");
        kursPython.add("Klaus");

        System.out.printf("Java: %s\n", kursJava);
        System.out.printf("Python: %s\n", kursPython);

        alleTeilnehmer.addAll(kursJava);
        alleTeilnehmer.addAll(kursPython);

        System.out.printf("Alle Teilnehmer %s\n", alleTeilnehmer);

        teilnehmerBeideKurse.addAll(kursJava);
        teilnehmerBeideKurse.retainAll(kursPython);

        System.out.printf("Beide Kurse: %s\n", teilnehmerBeideKurse);
    }
}