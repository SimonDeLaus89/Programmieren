/*
3.  Erstellen Sie ein Programm, das über den getchar()-Befehl einen Buchstaben vom Anwender abfragt.
    Erhöhen Sie den erhaltenen int-Wert um 1 und geben Sie diesen Wert wieder als Buchstaben aus.
    Beobachten Sie, welches Ergebnis das Programm dabei anzeigt.

Neumann, Markus. C Programmieren: für Einsteiger: Der leichte Weg zum C-Experten (Einfach Programmieren lernen 8) (German Edition) (S.55-56). Kindle-Version.
*/

#include <stdio.h>

void main()
{
    int x;
    printf ("Geben Sie einen Buchstaben ein: ");
    x = getchar();
    x++;
    printf ("Ergebnis nach der Erhöhung des Werts: %c\n", x);
}