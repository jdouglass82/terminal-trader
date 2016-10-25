
import sqlite3

db = sqlite3.connect('living.db')

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE buildings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        city TEXT,
        build_year INTEGER,
        resident_id INTEGER,
        FOREIGN KEY(resident_id) REFERENCES residents(id)
    );
''')

# You can run the commit once after both executes. It is not necessary to run the commit after each of these table creations
# db.commit()

cursor.execute('''
    CREATE TABLE residents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        rent INTEGER,
    );
''')
# The first parameter in the foreign key will always be the column in the current table
#  The second parameter is the column in the concurrent table being reference

db.commit()
db.close()