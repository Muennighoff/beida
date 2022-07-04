-- Clear tables
drop table if exists stocks;

-- Create tables
CREATE TABLE stocks
(
	stock TEXT,
    year INT,
    month INT,
    season INT,
    datum TEXT,
    opening REAL,
    highest REAL,
    lowest REAL,
    closing REAL,
    incr REAL,
    incrpct REAL,
    volume INT,
    amount INT,
    amplitude REAL,
    changed REAL
);

