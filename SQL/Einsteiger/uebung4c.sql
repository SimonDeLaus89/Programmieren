/*
3.  Erstellenügen Sie eine weitere Spalte für die Versandkosten hinzu.

Fuchs, Paul. SQL: Handbuch für Einsteiger: Der leichte Weg zum SQL-Experten (Einfach Programmieren lernen 9) (German Edition) (S.72). BMU Media GmbH. Kindle-Version.
*/

USE OnlineshopXY;
GO

ALTER TABLE sortiment ADD sortiment_versandkosten DECIMAL(2,2);