import sqlite3


conn = sqlite3.connect('Izdatelstvo.db')
cursor = conn.cursor()
cursor.executescript('''
PRAGMA foreign_keys=ON;

CREATE TABLE Издатель (
  id INTEGER PRIMARY KEY,
  Название TEXT,
  Город TEXT,
  Сайт TEXT
);

CREATE TABLE Издание (
  id INTEGER PRIMARY KEY,
  Название_книги TEXT,
  Дата INTEGER,
  Издатель_id INTEGER,
  Произведение_id INTEGER,
  FOREIGN KEY (Издатель_id) REFERENCES Издатель(id)
  ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (Произведение_id) REFERENCES Произведение(id)
  ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Произведение (
  id INTEGER PRIMARY KEY,
  Название TEXT,
  Дата INTEGER,
  Жанр TEXT
);

CREATE TABLE Автор (
  id INTEGER PRIMARY KEY,
  Фамилия TEXT,
  Имя TEXT,
  Email TEXT
);

CREATE TABLE Автор_Произведение (
  Автор_id INTEGER,
  Произведение_id INTEGER,
  FOREIGN KEY (Автор_id) REFERENCES Автор(id)
  ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (Произведение_id) REFERENCES Произведение(id)
  ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Заказчик (
  id INTEGER PRIMARY KEY,
  Имя_заказчика TEXT,
  Телефон INTEGER,
  Адресс TEXT
);

CREATE TABLE Заказ (
  id INTEGER PRIMARY KEY,
  Дата INTEGER,
  Тираж TEXT,
  Статус_заказа TEXT,
  Издание_id INTEGER,
  Заказчик_id INTEGER,
  FOREIGN KEY (Издание_id) REFERENCES Издание(id)
  ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (Заказчик_id) REFERENCES Заказчик(id)
  ON UPDATE CASCADE ON DELETE CASCADE
);
 ''')
conn.commit()

cursor.executescript('''
INSERT INTO Издатель (Название, Город, Сайт)
VALUES ('Ранок', 'Харьков', 'www.ranok.com.ua'), ('Основы', 'Киев', 'osnova.com.ua'), ('ЭКСМО', 'Москва', 'eksmo.ru');

INSERT INTO Автор (Фамилия, Имя, Email)
VALUES ('Гарисон', 'Гарри', 'garry@gmail.com'), ('Скаландис', 'Ант', 'antscal12@gmail.com'),
('Перумов', 'Ник', 'perumov@mail.ru'), ('Головачев', 'Василий', 'golovachov@gmail.com'),
('Азимов', 'Айзек', 'isaacaz@gmail.com'), ('Асприн', 'Роберт', 'pasprin@gmail.com');

INSERT INTO Произведение (Название, Дата)
VALUES ('Черный человек', '1993'), ('Реликт', '1995'), ('Пираньи', '1989'), ('Реликт 2', '1999'), 
('Чувство долга', '1962'), ('Чума из космоса', '1965'), ('Мир Смерти', '1990'), ('Возвращение в Мир Смерти', '1998'),
('Плененная планета', '1969'), ('Эльфийский клинок', '1993'), ('Рождение мага', '1999'),
('Алмазный меч, деревянный меч', '1998'), ('Конец вечности', '1955'),
('Я, робот', '1950'), ('Сами боги', '1972'), ('Мир воров', '1979'), ('Тени Санктуария', '1981');

INSERT INTO Заказчик (Имя_заказчика, Телефон, Адресс)
VALUES ('ООО"Мечта"', 380532345753 , 'Кривой Рог'), ('ООО"Пионер"', 385689421556, 'Киев'),
('ЧП Калина', 0563457538 , 'Днепр');

INSERT INTO Автор_Произведение (Автор_id, Произведение_id)
VALUES (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 8), (3, 10), (3, 11), (3, 12), (4, 1), (4, 2), (4, 3), (4, 4),
(5, 13), (5, 14), (5, 15), (6, 16), (6, 17);
 
INSERT INTO Издание (Название_книги, Дата, Издатель_id, Произведение_id)
VALUES ('Чувство долга', 1991, 2, 5), ('Реликт', 1997, 3, 2), ('Конец вечности', 1989, 2, 13),
('Мир воров', 2001, 1, 16), ('Рождение мага', 2000, 2, 10);

INSERT INTO Заказ (Дата, Тираж, Статус_заказа, Издание_id, Заказчик_id)
VALUES (1990, 20000, 'Готов', 1, 2), (1996, 10000, 'В печати', 2, 1), (1989, 10000, 'Готов', 3, 2),
 (2001, 5000, 'На согласовании', 4, 3), (2000, 15000, 'Готов', 5, 3); 
''')
conn.commit()

data = cursor.execute('SELECT * From Автор_Произведение WHERE Автор_id = 1;')
print(data.fetchall())

data1 = cursor.execute('SELECT * FROM Издание WHERE Издание.Издатель_id=2;')
print(data1.fetchall())
conn.close()