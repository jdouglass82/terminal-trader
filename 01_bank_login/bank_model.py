import sqlite3
import datetime as dt
conn = sqlite3.connect('bank.db')
c = conn.cursor()

	def __init__(self):
		c.execute('CREATE TABLE IF NOT EXISTS users ('id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, creation_date ');'


		c.execute('CREATE TABLE IF NOT EXISTS accounts ('id INTEGER PRIMARY KEY AUTOINCREMENT);''
