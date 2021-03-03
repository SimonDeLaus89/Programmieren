/*
1.  Erstellen Sie eine Datenbank für das Unternehmen OnlineshopXY, in der Sie alle relevanten Informationen für das Unternehmen aufnehmen.
    Wechseln Sie dann in diese Datenbank, um die weitere Bearbeitung vorzunehmen.
2.  Erstellen Sie eine Tabelle für das Sortiment des Unternehmens.
    Gestalten Sie hierbei eine Spalte für die Artikelnummer, den Produkttyp, den Preis und die Anzahl der verfügbaren Artikel.
    Entscheiden Sie selbst, welche Datentypen, Attribute und Bedingungen für diese Tabelle sinnvoll sind.
3.  Fügen Sie eine weitere Spalte für die Versandkosten hinzu.
4.  Löschen Sie die eben hinzugefügte Spalte wieder.

Fuchs, Paul. SQL: Handbuch für Einsteiger: Der leichte Weg zum SQL-Experten (Einfach Programmieren lernen 9) (German Edition) (S.72). BMU Media GmbH. Kindle-Version.
*/

CREATE DATABASE OnlineshopXY;
GO

USE OnlineshopXY;
GO

CREATE TABLE sortiment (
	sortiment_id INT IDENTITY(1,1) PRIMARY KEY,
      sortiment_produkttyp VARCHAR(30) NOT NULL,
      sortiment_preis DECIMAL(5,2) NOT NULL,
      sortiment_anzahl INT
);

ALTER TABLE sortiment ADD sortiment_versandkosten DECIMAL(2,2);

ALTER TABLE sortiment DROP COLUMN sortiment_versandkosten;