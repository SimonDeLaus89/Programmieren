/*
1.  Erstellen Sie ein Programm, das eine Datenstruktur mit drei integer-Werten beinhaltet.
    Geben Sie dafür beliebige Zahlen ein und erhöhen Sie diese dann jeweils um 1.
    Geben Sie anschließend die Ergebnisse aus. Wählen Sie dafür eine passende Datenstruktur.

Bonacina, Michael.C# Programmieren: für Einsteiger: Der leichte Weg zum C#-Experten! (Visual Studio 2019) (Einfach Programmieren lernen 5) (German Edition) (S.69-70). Kindle-Version. 
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace uebung3a
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] x = new int[3] { 1, 2, 3 };

            Console.WriteLine("Werte: {0} {1} {2}", x[0], x[1], x[2]);

            x[0] += 1;
            x[1] += 1;
            x[2] += 1;

            Console.WriteLine("Werte: {0} {1} {2}", x[0], x[1], x[2]);
        }
    }
}
