/*
3.  Gestalten Sie eine Struktur für einen Buchhändler.
    Diese soll den Titel, den Autor und den Preis enthalten.
    Füllen Sie die Struktur mit Werten und geben Sie diese aus.

Neumann, Markus. C Programmieren: für Einsteiger: Der leichte Weg zum C-Experten (Einfach Programmieren lernen 8) (German Edition) (S.72). Kindle-Version.
*/

#include <stdio.h>
#include <string.h>

struct Buch
{
   char title[100];
   char author[100];
   float price;
};

void main()
{
    struct Buch buch1;
    strncpy(buch1.title, "Gestern, heute, morgen", 100);
    strncpy(buch1.author, "Andi Latte", 100);
    buch1.price = 19.93;

    printf("Titel: %s\n", buch1.title);
    printf("Autor: %s\n", buch1.author);
    printf("Preis: %.2f €\n", buch1.price);
}
