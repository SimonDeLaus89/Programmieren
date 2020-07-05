/*
2.  Erstellen Sie ein Programm, das eine Datenstruktur aus drei beliebigen Worten enthält.
    Es soll möglich sein, diese später noch zu erweitern.'
    Geben Sie anschließend die Zahl der Einträge über die Konsole aus.
    Wählen Sie dafür eine passende Datenstruktur.

Bonacina, Michael. C# Programmieren: für Einsteiger: Der leichte Weg zum C#-Experten! (Visual Studio 2019) (Einfach Programmieren lernen 5) (German Edition) (S.70). Kindle-Version.
*/


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace uebung3b
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> x = new List<string>();

            x.Add("Haus");
            x.Add("Auto");
            x.Add("Straße");

            Console.WriteLine("Anzahl der Elemente: {0}", x.Count);
        }
    }
}
