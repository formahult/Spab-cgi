CREATE TABLE Locations(
	ID INTEGER PRIMARY KEY NOT NULL,
	Timestamp TEXT NOT NULL,
	Latitude REAL NOT NULL,
	Longitude REAL NOT NULL
);


CREATE TABLE Locations(
	ID INTEGER PRIMARY KEY NOT NULL,
	Timestamp TEXT NOT NULL,
	Latitude REAL NOT NULL,
	Longitude REAL NOT NULL
);


CREATE TABLE Waypoints(
        ID INTEGER PRIMARY KEY NOT NULL,
        Latitude REAL NOT NULL,
        Longitude REAL NOT NULL
);


CREATE TABLE Commands(
        ID INTEGER PRIMARY KEY NOT NULL,
        Active BOOLEAN NOT NULL,
        Command TEXT NOT NULL,
        Latitude REAL,
        Longitude REAL,
        Arguments TEXT
);
