/*
3.  Erstellen�gen Sie eine weitere Spalte f�r die Versandkosten hinzu.

Fuchs, Paul. SQL: Handbuch f�r Einsteiger: Der leichte Weg zum SQL-Experten (Einfach Programmieren lernen 9) (German Edition) (S.72). BMU Media GmbH. Kindle-Version.
*/

USE OnlineshopXY;
GO

ALTER TABLE sortiment ADD sortiment_versandkosten DECIMAL(2,2);