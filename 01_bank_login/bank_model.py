import sqlite3
# import datetime as dt
db = sqlite3.connect('bank.db')

cursor = db.cursor()


class Models:

    def __init__(self):
        pass

    def check_user(self, user_name, user_pass):

        user = cursor.execute("""
                       SELECT name FROM users WHERE name = user_name AND password = user_pass
                       """)
        return user.fetchall()

    def check_permission(self, user_name):

        status = int(cursor.execute("""
                                    SELECT permission FROM users WHERE name = user_name
                                    """))
        return status

    #  this is called after checking if user exists already
    def new_client(self, new_name, new_password, start_date, new_account):

        cursor.execute("""
                       INSERT INTO users ("name", "password", "creation_date", "permission") VALUES (?, ?, ?, ?)
                       """, (new_name, new_password, start_date, 1))
        db.commit()

        client_id = cursor.execute("""
                                 SELECT users.id FROM users WHERE name = new_name
                             """)
        # initialize balance at zero. change later if need
        cursor.execute("""
                       INSERT INTO accounts ("users_id", "account_no", "balance") VALUES (?, ?, ?)
                       """, (client_id, new_account, 0))

    def new_banker(self, new_name, new_password, start_date):

        cursor.execute("""
                       INSERT INTO users ("name", "password", "creation_date", "permission") VALUES (?, ?, ?, ?)
                       """, (new_name, new_password, start_date, 5))

    def view_accounts(self, acct_user):

        client_accounts = cursor.execute("""
                                  SELECT account_no FROM users, accounts WHERE accounts.users_id = users.id AND users.name = acct_user
                                  """)
        return client_accounts.fetchall()
        # db.commit()
