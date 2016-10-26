from bank_view import Views
from bank_model import Models
import random
from datetime import datetime


class Users:

    def __init__(self, user_name):
        self.views = Views()
        self.user_name = user_name
        self.model = Models()


class Client(Users):

    def __init__(self, user_name):
        super.__init__()

    def view_account(self):
        self.accounts = self.model.view_accounts(self.user_name)
        print(self.accounts)

    def withdrawl(self):
        pass

    def deposit(self):
        pass

    def transfer_money(self):
        pass


class Banker(Users):

    def __init__(self, user_name):
        super.__init__()

    # to do: add a check to see if user exits already
    def new_client(self):
        self.info = self.views.new_user()
        randnum = random.randrange(100000, 999999)
        dt = datetime.date()
        self.models.new_client(self.info[0], self.info[1], dt, randnum)

    def new_banker(self):
        self.info = self.views.new_user()

    # adding additional client accounts
    def add_acct(self, client_username):
        pass

    def check_account(self, user_name):
        pass

    def withdrawl(self, user_name):
        pass

    def deposit(self, user_name):
        pass


class Menu:

    def __init__(self):
        self.models = Models()
        self.views = Views()

    def login(self):
        self.request_info = self.views.check_user()
        user_name = self.request_info[0]
        password = self.request_info[1]
        acct_user = self.models.locate_user(user_name, password)
        if acct_user is not None:
            permission_level = self.models.check_permission(user_name)
            if permission_level > 1:
                self.bank_user = Banker(user_name)  # might not need to pass in name
            self.client_user = Client(user_name)
        else:
            self.views.error()

    def is_unique(self):
        pass

menu = Menu()
# check first if user already exists
menu.create_user()


