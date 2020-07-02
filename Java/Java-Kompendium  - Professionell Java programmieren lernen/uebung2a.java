/*
1.  Erstellen Sie ein Programm, das drei Variablen für ganze Zahlen enthält.
    Diese sollen jedoch jeweils einen unterschiedlichen Typ verwenden.
    Geben sie einer von ihnen einen beliebigen Wert.
    Weisen Sie daraufhin den beiden anderen Variablen den Wert der ersten Variablen zu.
    Wählen Sie dafür Typen, die keine explizite Umformung des Variablentyps notwendig machen.

Neumann, Markus. Java: Kompendium: Professionell Java programmieren lernen (German Edition) (S.60-61). Kindle-Version.
*/

public class uebung2a
{
    public static void main(String[] args)
    {
        byte x = 1;
        int y = 2;
        long z = 3;

        System.out.println("Werte: x: " + x + " y: " + y + " z: " + z);
        
        y = x;
        z = x;

        System.out.println("Werte: x: " + x + " y: " + y + " z: " + z);
    }
}