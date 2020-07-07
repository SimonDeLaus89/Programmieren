/*
2.  Gestalten Sie ein Programm, das vom Anwender zwei Fließkommazahlen abfragt.
    Geben Sie als Ergebnis die Summe der beiden Werte aus.

Neumann, Markus. C Programmieren: für Einsteiger: Der leichte Weg zum C-Experten (Einfach Programmieren lernen 8) (German Edition) (S.55). Kindle-Version.
*/

#include <stdio.h>

void main()
{
    float x;
    float y;

    printf ("Geben Sie den ersten Wert ein: ");
    scanf ("%f", &x);
    printf ("Geben Sie den ersten Wert ein: ");
    scanf ("%f", &y);
    printf ("Ergebnis: %f", x + y);
}