
import sqlite3

db = sqlite3.connect('bank.db')

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        password TEXT,
        creation_date INTEGER,
        permission INTEGER
    );
''')

# You can run the commit once after both executes. It is not necessary to run the commit after each of these table creations
# db.commit()

cursor.execute('''
    CREATE TABLE accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        users_id INTEGER,
        account_no INTEGER,
        balance INTEGER,
        FOREIGN KEY(users_id) REFERENCES users(id)
    );
''')
# The first parameter in the foreign key will always be the column in the current table
#  The second parameter is the column in the concurrent table being reference

db.commit()
print("Your tables have been made!")
# db.close()

# SEED

USERS = [
    ["Empire State", "New York", 1930, 1],
    ["Bradbury", "Los Angeles", 1893, 2],
    ["White House", "Washington D.C.", 1800, 2]
]

ACCOUNTS = [
    [1, 100000, 1],
    [2, 90000, 2],
    [2, 98900, 2]
]

print("Destroying old data")
cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM accounts")

for users in USERS:
    cursor.execute("""
        INSERT INTO users ("name", "password", "creation_date", "permission") VALUES (?, ?, ?, ?)""", (users[0], users[1], users[2], users[3]))

db.commit()

for accounts in ACCOUNTS:
    cursor.execute("""
        INSERT INTO accounts ("users_id", "account_no", "balance") VALUES (?, ?, ?)""", (accounts[0], accounts[1], accounts[2]))

db.commit()

db.close()
