/*
3.  Wählen Sie abschließend eine Datenstruktur aus, die es ermöglicht, eine Zahl, ein Wort und eine boolesche Variable aufzunehmen.
    Löschen Sie daraus den Eintrag mit dem Wort und geben Sie die übrigen Inhalte aus.

Bonacina, Michael. C# Programmieren: für Einsteiger: Der leichte Weg zum C#-Experten! (Visual Studio 2019) (Einfach Programmieren lernen 5) (German Edition) (S.70-71). Kindle-Version.  
*/

using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace uebung3c
{
    class Program
    {
        static void Main(string[] args)
        {
            ArrayList x = new ArrayList();

            x.Add("Haus");
            x.Add(1);
            x.Add(true);

            x.Remove("Haus");

            Console.WriteLine("Werte {0}, {1}", x[0], x[1]);
        }
    }
}
