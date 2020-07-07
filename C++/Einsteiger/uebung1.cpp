/*
1.  Erweitern Sie das Programm aus diesem Kapitel so, dass es einen zweiten Ausgabebefehl enthält.
    Den Inhalt können Sie beliebig festlegen.
2.  Wenn Sie das Programm aus Aufgabe 1 ausführen, stellen Sie fest, dass dabei beide Textbausteine ohne Zeilenumbruch hintereinander ausgegeben werden.
    Fügen Sie daher nach der ersten Textausgabe den Begriff std::endl ein, um einen Zeilenumbruch zu erzeugen.
    Diesen müssen Sie einfach durch die doppelten Pfeile (<<) an den bisherigen Befehl anschließen.
3.  Im letzten Programm kamen mehrere Befehle aus dem Namensraum std zum Einsatz.
    Diesen Zusatz jedes Mal hinzuzufügen, ist jedoch recht umständlich.
    Wenn sie in einem Programm stets den gleichen Namensraum verwenden, ist es anstatt dessen möglich, dies durch den Befehl using namespace std; zu Beginn des Programms anzugeben.
    Fügen Sie diesen Befehl ein und entfernen Sie die übrigen Angaben zum Namensraum aus dem Programm.

Bonacina, Michael. C++ Programmieren: für Einsteiger: Der leichte Weg zum C++-Experten (Einfach Programmieren lernen 3) (German Edition) (S.32). Kindle-Version.
*/

#include <iostream>

using namespace std;

int main()
{
    cout << "Hallo Welt!" << endl;
    cout << "Und das ist Zeile 2" << endl;

    return 0;
}