import sqlite3
import datetime as dt
db = sqlite3.connect('bank.db')

cursor = db.cursor()
class Models:


	def __init__(self):
		pass
# 		cursor.execute('''
#     CREATE TABLE users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         accounts_id INTEGER,
#         name TEXT,
#         password TEXT,
#         creation_date INTEGER,
#         permission BOOLEAN,
#         FOREIGN KEY(accounts_id) REFERENCES accounts(id)
#     );
# ''')


	def islegit():
		pass

	def gettable():
		table = cursor.execute('''SELECT accounts_id FROM users WHERE accounts_id=number);''')
		return table

	def newuser(self, newname, newpassword, account):
		
		
		cursor.execute("""
			INSERT INTO  accounts ("account_no") VALUES (?)

			""", (account,)) 

		db.commit()
		acc = cursor.execute("""SELECT accounts.id FROM accounts WHERE account_no = account""")
		cursor.execute("""
			INSERT INTO users ("name", "password", "accounts_id") VALUES (newname,newpassword,acc)

		""")
		# something