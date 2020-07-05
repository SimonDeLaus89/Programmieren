/*
2.  Erstellen Sie ein Programm mit den Integer-Variablen a und b und weisen Sie diesen beliebige Werte zu.
    Addieren Sie a und b und weisen Sie diesen Wert der Variablen a zu.
    Multiplizieren Sie den neuen Wert für a mit b und weisen Sie diesen erneut a zu und geben Sie den Wert von a auf dem Bildschirm aus.
    Erstellen Sie zwei verschiedene Lösungswege für die mathematischen Operationen.

Bonacina, Michael. C++ Programmieren: für Einsteiger: Der leichte Weg zum C++-Experten (Einfach Programmieren lernen 3) (German Edition) (S.52). Kindle-Version.
*/

#include <iostream>

using namespace std;

int main()
{
    int x = 2;
    int y = 3;
    int tmp = 0;

    tmp = x + y;
    tmp = tmp * y;

    cout << "Ergebnis (v1): " << tmp << endl;

    x += y;
    x *= y;

    cout << "Ergebnis (v2): " << x << endl;

    return 0;
}