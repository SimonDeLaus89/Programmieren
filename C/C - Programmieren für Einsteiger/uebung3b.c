/*
2.  Schreiben Sie ein Programm, das den Anwender zur Eingabe von drei Wörtern auffordert.
    Nehmen Sie diese einzeln auf.
    Fügen Sie sie anschließend zu einer einzigen Zeichenkette zusammen.
    Achten Sie darauf, zwischen den einzelnen Wörtern ein Leerzeichen anzubringen.

Neumann, Markus. C Programmieren: für Einsteiger: Der leichte Weg zum C-Experten (Einfach Programmieren lernen 8) (German Edition) (S.72). Kindle-Version.
*/

#include <stdio.h>
#include <string.h>

void main ()
{
    char x[65];
    char a[21];
    char b[21];
    char c[21];

    printf("Geben Sie Wort 1 (max 20 Zeichen) ein: ");
    scanf("%s", &a);
    printf("Geben Sie Wort 2 (max 20 Zeichen) ein: ");
    scanf("%s", &b);
    printf("Geben Sie Wort 2 (max 20 Zeichen) ein: ");
    scanf("%s", &c);

    strcpy(x, a);
    strncat(x, " ", 2);
    strncat(x, b , 21);
    strncat(x, " ", 2);
    strncat(x, c , 21);

    printf("Text: %s \n", x);
}