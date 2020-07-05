/*
1.  Erstellen Sie ein Programm mit einem Array, das fünf Fließkommazahlen enthält.
    Geben Sie die Werte einzeln aus.

Neumann, Markus. C Programmieren: für Einsteiger: Der leichte Weg zum C-Experten (Einfach Programmieren lernen 8) (German Edition) (S.72). Kindle-Version.
*/

#include <stdio.h>

void main()
{
    float x[] = {1.0, 2.1, 3.2, 4.3, 5.4};

    printf("Zahl 1: %f\n", x[0]);
    printf("Zahl 2: %f\n", x[1]);
    printf("Zahl 3: %f\n", x[2]);
    printf("Zahl 4: %f\n", x[3]);
    printf("Zahl 5: %f\n", x[4]);
}