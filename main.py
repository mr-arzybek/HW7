import sqlite3

db = sqlite3.connect('hw.db')

c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user (
hobby text,
name text,
surname text,
year integer,
points integer
)''')

# c.execute("INSERT INTO user VALUES ('football', 'Данияр', 'Жыргалбек', 2002, 10)")
# c.execute("INSERT INTO user VALUES ('valebol', 'Максим', 'Евтушенко', 1990, 10)")
# c.execute("INSERT INTO user VALUES ('basketball', 'Абдула', 'Манаров', 2001, 9)")
# c.execute("INSERT INTO user VALUES ('football', 'Адилет', 'Женишбеков', 2000, 10)")
# c.execute("INSERT INTO user VALUES ('basketball', 'Сергей', 'Беляев', 1993, 5)")
# c.execute("INSERT INTO user VALUES ('valebol', 'Алимбек', 'Акеров', 2004, 5)")
# c.execute("INSERT INTO user VALUES ('basketball', 'Арзыбек', 'Абдырахманов', 1999, 10)")
# c.execute("INSERT INTO user VALUES ('valebol', 'Элдияр', 'Нурали', 2002, 10)")
# c.execute("INSERT INTO user VALUES ('football', 'Бектур', 'Рысбаев', 2001, 10)")
# c.execute("INSERT INTO user VALUES ('football', 'Назира', 'Абдиллаева', 2001, 10)")
# c.execute("SELECT rowid FROM user")

c.execute("UPDATE user SET name = 'genius' WHERE points = 10")
c.execute("SELECT rowid, surname, name FROM user ")

items = c.fetchall()

print(items)

for i in items:
    surname = i[1]
    if len(surname) > 10:
        print(surname)
    else:
        ...

c.execute("SELECT rowid, name FROM user WHERE name = 'genius'")
c.execute("DELETE FROM user WHERE rowid % 2 = 0")
print(c.fetchall())



db.commit()
db.close()
