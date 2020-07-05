/*
1.  Erstellen Sie ein Programm, mit den Integer-Variablen a und b, weisen Sie diesen jeweils einen bestimmten Wert zu und geben Sie diesen aus.
    Tauschen Sie daraufhin die Werte der beiden Variablen aus, sodass die Variable a den vorherigen Wert von b und b den vorherigen Wert von a annimmt.
    Hierfür ist eine zusätzliche Integer-Variable als Zwischenspeicher notwendig. Geben Sie nach dem Tausch die neuen Werte aus.

Bonacina, Michael. C++ Programmieren: für Einsteiger: Der leichte Weg zum C++-Experten (Einfach Programmieren lernen 3) (German Edition) (S.52). Kindle-Version.
*/

#include <iostream>

using namespace std;

int main()
{
    int x = 2;
    int y = 3;
    int tmp = 0;

    cout << "x: " << x << endl;
    cout << "y: " << y << endl;

    tmp = x;
    x = y;
    y = tmp;

    cout << "x: " << x << endl;
    cout << "y: " << y << endl;

    return 0;
}