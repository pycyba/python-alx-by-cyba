CREATE TABLE waluty (
    kod CHAR(3) NOT NULL,
    nazwa VARCHAR(80) NOT NULL,
    PRIMARY KEY(kod)
);

CREATE TABLE kursy (
    kod CHAR(3) NOT NULL,
    data DATE NOT NULL,
    kurs NUMERIC(12, 9) NOT NULL,
    PRIMARY KEY(kod, data),
    FOREIGN KEY(kod) REFERENCES waluty(kod)
);
