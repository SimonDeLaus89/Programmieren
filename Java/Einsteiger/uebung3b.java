/*
2.  Bisher wurden die verschiedenen Werte stets direkt in das Programm eingegeben.
    In der Praxis ist es jedoch üblich, dass der Anwender diese eingibt.
    Dieser Vorgang ist in Java relativ kompliziert.
    Da diese Funktion jedoch auch bei den weiteren Beispielen nützlich ist, soll sie hier kurz vorgestellt werden.
    Die Einzelheiten werden dabei nicht erklärt – das folgt in den weiteren Kapiteln (vorwiegend in den Kapiteln VII und VIII). (Code vorgegeben)
    Sie können mit dem eigentlichen Programm beginnen.
    Dazu sollen Sie dem Nutzer eine kleine Rechenaufgabe stellen und ihn dazu auffordern, diese zu lösen.
    Überprüfen Sie nun mit einer if-Abfrage, ob der Anwender das richtige Ergebnis ermittelt hat und geben Sie eine entsprechende Meldung aus.

Bonacina, Michael. Java Programmieren: für Einsteiger: Der leichte Weg zum Java-Experten (2. Auflage: komplett neu verfasst) (Einfach Programmieren lernen 1) (German Edition) (S.73-74). Kindle-Version. 
*/

import java.io.*;

public class uebung3b
{
    public static void main(String[] args) throws Exception
    {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        System.out.print("Wieviel ist 999 + 1? ");
        int x = Integer.parseInt(br.readLine());

        if (x == 1000)
        {
            System.out.println("Richtig!");
        }
        else
        {
            System.out.println("Falsch!");
        }
    }
}