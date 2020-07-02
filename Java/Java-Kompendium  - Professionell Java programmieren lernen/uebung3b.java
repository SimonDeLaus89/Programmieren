/*
2.  Erzeugen Sie eine Liste für die Namen der Mitarbeiter eines Unternehmens.
    Geben Sie daraufhin dem Anwender die Möglichkeit, fünf Namen in die Liste einzutragen und geben Sie abschließend die gesamte Liste aus.

Neumann, Markus. Java: Kompendium: Professionell Java programmieren lernen (German Edition) (S.80-81). Kindle-Version.
*/

import java.io.*;
import java.util.*;

public class uebung3b {
    public static void main(String[] args) throws Exception
    {
        ArrayList<String> namen = new ArrayList<>();

        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        System.out.print("Geben Sie den ersten Namen ein: ");
        namen.add(br.readLine());

        System.out.print("Geben Sie den zweiten Namen ein: ");
        namen.add(br.readLine());

        System.out.print("Geben Sie den dritten Namen ein: ");
        namen.add(br.readLine());

        System.out.print("Geben Sie den vierten Namen ein: ");
        namen.add(br.readLine());

        System.out.print("Geben Sie den fünften Namen ein: ");
        namen.add(br.readLine());

        System.out.println("Namen: " + namen);
    }
}