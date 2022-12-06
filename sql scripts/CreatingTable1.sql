

CREATE TABLE temperature 
(
[RecordID] BIGINT PRIMARY KEY IDENTITY(1,1),
[TimeStamp] DATETIME NOT NULL,
[Temperature] NUMERIC(10,5) NOT NULL, -- PRECISION=10 AND SCALE=5  Which means that it has total 10 digits and 5 dig, after the decimal point
[Hummidity] REAL NOT NULL,   -- floating poinf number
[LocationID] SMALLINT NOT NULL
)



DROP TABLE dbo.temperature 

