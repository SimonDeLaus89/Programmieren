/*
2.  Schreiben Sie ein Programm, das vom Anwender zwei Werte abfragt.
    Berechnen Sie daraufhin das Ergebnis aus allen vier Grundrechenarten für die beiden Werte.
    Geben Sie bei der Ausabe den entsprechenden Term und das Ergebnis an.
    Das Programm soll es dem Anwender erlauben, Kommazahlen einzugeben.

Bonacina, Michael. C# Programmieren: für Einsteiger: Der leichte Weg zum C#-Experten! (Visual Studio 2019) (Einfach Programmieren lernen 5) (German Edition) (S.52-53). Kindle-Version.
*/


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace uebung2b
{
    class Program
    {
        static void Main(string[] args)
        {
            double x = 0.0;
            double y = 0.0;

            Console.Write("Geben Sie die erste Zahl ein: ");
            x = double.Parse(Console.ReadLine());

            Console.Write("Geben Sie die zweite Zahl ein: ");
            y = double.Parse(Console.ReadLine());

            Console.WriteLine("Summe: {0}", x + y);
            Console.WriteLine("Differenz: {0}", x - y);
            Console.WriteLine("Produkt: {0}", x * y);
            Console.WriteLine("Quotient: {0}", x / y);
        }
    }
}
