BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "region" (
	"idreg"	INTEGER NOT NULL,
	"nomreg"	TEXT,
	"idpais"	INTEGER NOT NULL,
	PRIMARY KEY("idreg")
);
CREATE TABLE IF NOT EXISTS "subcategoria" (
	"idsubc"	INTEGER NOT NULL,
	"nomsubc"	TEXT,
	"idcat"	INTEGER NOT NULL,
	PRIMARY KEY("idsubc")
);
CREATE TABLE IF NOT EXISTS "pais" (
	"idpais"	INTEGER NOT NULL,
	"nompais"	TEXT,
	PRIMARY KEY("idpais")
);
CREATE TABLE IF NOT EXISTS "categoria" (
	"idcat"	INTEGER NOT NULL,
	"nomcat"	TEXT,
	PRIMARY KEY("idcat")
);
CREATE TABLE IF NOT EXISTS "bspub" (
	"idp"	INTEGER NOT NULL,
	"nomp"	TEXT,
	"preciop"	REAL,
	"imgp"	TEXT,
	"fuentep"	TEXT,
	"fecsp"	TIMESTAMP,
	"fecswp"	TIMESTAMP,
	"idcat"	INTEGER NOT NULL,
	"idpais"	INTEGER NOT NULL,
	PRIMARY KEY("idp")
);
CREATE TABLE IF NOT EXISTS "bscon" (
	"idc"	INTEGER NOT NULL,
	"nomc"	TEXT,
	"precioc"	REAL,
	"imgc"	TEXT,
	"fuentec"	TEXT,
	"fecsc"	TIMESTAMP,
	"fecswc"	TIMESTAMP,
	"idcat"	INTEGER NOT NULL,
	"idpais"	INTEGER NOT NULL,
	PRIMARY KEY("idc")
);
INSERT INTO "region" VALUES (1,'VALPARAISO',1);
INSERT INTO "subcategoria" VALUES (1,'ARANCELES',1);
INSERT INTO "pais" VALUES (1,'CHILE');
INSERT INTO "categoria" VALUES (1,'EDUCACION');
INSERT INTO "bscon" VALUES (1,'test',200.0,'www.google.cl','www.gropoz.com','2019-12-12','2019-12-11',1,1);
COMMIT;
