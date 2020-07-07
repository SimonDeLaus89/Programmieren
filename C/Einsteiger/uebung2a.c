/*
1.  Schreiben Sie ein Programm, das eine Variable für eine ganze Zahl definiert und ihr einen beliebigen Wert zuweist.
    Deklarieren Sie daraufhin zwei neue Variablen und weisen der ersten den doppelten Wert und der zweiten das Quadrat der ursprünglichen Variablen zu.
    Geben Sie daraufhin die entsprechenden Ergebnisse aus.

Neumann, Markus. C Programmieren: für Einsteiger: Der leichte Weg zum C-Experten (Einfach Programmieren lernen 8) (German Edition) (S.55). Kindle-Version.
*/

#include <stdio.h>

void main()
{
    int x = 2;
    int y = x + x;
    int z = x * x;

    printf("Doppelt: %d \n", y);
    printf("Quadrat: %d \n", z);
}