/*
2.  Erstellen Sie eine Tabelle f�r das Sortiment des Unternehmens.
    Gestalten Sie hierbei eine Spalte f�r die Artikelnummer, den Produkttyp, den Preis und die Anzahl der verf�gbaren Artikel.
    Entscheiden Sie selbst, welche Datentypen, Attribute und Bedingungen f�r diese Tabelle sinnvoll sind.

Fuchs, Paul. SQL: Handbuch f�r Einsteiger: Der leichte Weg zum SQL-Experten (Einfach Programmieren lernen 9) (German Edition) (S.72). BMU Media GmbH. Kindle-Version.
*/

USE OnlineshopXY;
GO

CREATE TABLE sortiment (
	sortiment_id INT IDENTITY(1,1) PRIMARY KEY,
      sortiment_produkttyp VARCHAR(30) NOT NULL,
      sortiment_preis DECIMAL(5,2) NOT NULL,
      sortiment_anzahl INT
);