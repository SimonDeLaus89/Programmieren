/*
3.  Erstellen Sie eine Liste mit fünf Gästen, die Sie zu Ihrem nächsten Geburtstag einladen.
    Speichern Sie diese in einem mehrdimensionalen Array ab.
    Verwenden Sie für jeden Gast jeweils ein eigenes Feld für den Vornamen, den Nachnamen und für die Telefonnummer.
    Geben Sie anschließend alle Felder aus, wobei jeder Gast in einer eigenen Zeile stehen soll, die alle Daten, die ihn betreffen, enthält.

Bonacina, Michael. C++ Programmieren: für Einsteiger: Der leichte Weg zum C++-Experten (Einfach Programmieren lernen 3) (German Edition) (S.52-54). Kindle-Version.
*/

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string x[5][3] = {{"Thomas", "Mayer", "1234234"}, {"Sebastian", "Maurer", "753254"}, {"Franziska", "Schmidt", "126543"}, {"Michaela", "Mayer", "234534"}, {"Oliver", "Brandt", "865245"}};

    cout << "Gast1 1: " << x[0][0] << " " << x[0][1] << ", " << x[0][2] << endl;
    cout << "Gast1 2: " << x[1][0] << " " << x[1][1] << ", " << x[1][2] << endl;
    cout << "Gast1 3: " << x[2][0] << " " << x[2][1] << ", " << x[2][2] << endl;
    cout << "Gast1 4: " << x[3][0] << " " << x[3][1] << ", " << x[3][2] << endl;
    cout << "Gast1 5: " << x[4][0] << " " << x[4][1] << ", " << x[4][2] << endl;

    return 0;
}