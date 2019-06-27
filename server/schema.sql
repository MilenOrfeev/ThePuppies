DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS coordinates;
DROP TABLE IF EXISTS details;

CREATE TABLE user
(
    SID    TEXT PRIMARY KEY,
    name   TEXT NOT NULL,
    seat   INTEGER,
    role   TEXT,
    team   TEXT,
    xCoord INTEGER,
    yCoord INTEGER
);