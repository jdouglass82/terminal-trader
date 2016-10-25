
import sqlite3

db = sqlite3.connect('bank.db')

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        accounts_id INTEGER,
        name TEXT,
        password TEXT,
        creation_date INTEGER,
        permission BOOLEAN,
        FOREIGN KEY(accounts_id) REFERENCES accounts(id)
    );
''')

# You can run the commit once after both executes. It is not necessary to run the commit after each of these table creations
# db.commit()

cursor.execute('''
    CREATE TABLE accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_no INTEGER,
        balance INTEGER
    );
''')
# The first parameter in the foreign key will always be the column in the current table
#  The second parameter is the column in the concurrent table being reference

db.commit()
print("Your tables have been made!")
# db.close()

# SEED

USERS = [
    [1, "Empire State", "New York", 1930, True],
    [1, "Bradbury", "Los Angeles", 1893, True],
    [1, "White House", "Washington D.C.", 1800, True]
]

ACCOUNTS = [
    [100000, 1],
    [90000, 2]
]

print("Destroying old data")
cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM accounts")

for users in USERS:
    cursor.execute("""
        INSERT INTO users ("accounts_id", "name", "password", "creation_date", "permission") VALUES (?, ?, ?, ?, ?)""", (users[0], users[1], users[2], users[3], users[4],))

db.commit()

for accounts in ACCOUNTS:
    cursor.execute("""
        INSERT INTO accounts ("account_no", "balance") VALUES (?, ?)""", (accounts[0], accounts[1]))

db.commit()

db.close()
