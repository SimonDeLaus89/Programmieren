/*
2.  Schreiben Sie ein Programm, das den Anwender zur Eingabe einer Zahl auffordert.
    Das Programm soll daraufhin den doppelten Wert als Ergebnis ausgeben.

Neumann, Markus. Java: Kompendium: Professionell Java programmieren lernen (German Edition) (S.60-61). Kindle-Version.
*/

import java.io.*;

public class uebung2b
{
    public static void main(String[] args) throws IOException
    {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        System.out.print("Geben Sie eine Zahl ein: ");
        String x = br.readLine();

        int zahl = Integer.parseInt(x);
        System.out.println("Zahl * 2: " + zahl * 2);
    }
}