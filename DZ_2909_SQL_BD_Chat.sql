CREATE TABLE Users (
	ID INTEGER,
	Login TEXT,
	Password TEXT,
	Email TEXT,
	Gender TEXT,
	Age INTEGER
);

CREATE TABLE Chat (
	ID INTEGER,
	Chat_Name TEXT,
	Number_users TEXT,
	Data TEXT,
	Ttime TEXT
);

CREATE TABLE Messages (
	ID INTEGER,
	ID_User INTEGER,
	ID_Chat INTEGER,
	Messages_text TEXT,
	Data TEXT,
	Ttime TEXT,
	Size INTEGER
);