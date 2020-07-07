/*
1.  Erstellen Sie ein Programm, das jeweils eine int-, eine double und eine string-Variable enthält.
    Multiplizieren Sie die Werte der int- und der double-Variablen und speichern Sie den Wert in einer neuen Variablen.
    Wählen Sie hierfür einen passenden Typ.
    Geben Sie anschließend das Ergebnis zusammen mit der string-Variablen aus.

Bonacina, Michael. C# Programmieren: für Einsteiger: Der leichte Weg zum C#-Experten! (Visual Studio 2019) (Einfach Programmieren lernen 5) (German Edition) (S.52). Kindle-Version. 
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace uebung2a
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 3;
            double y = 7.2;
            double z = 0;
            string a = "Moin";

            z = x * y;

            Console.WriteLine("String: {0}, Produkt: {1}", a, z);
        }
    }
}
