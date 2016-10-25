from bank_view import Views
from bank_model import Models
import random

class Users:

	def __init__(self):

		self.models = Models()
		self.views = Views()




class Menu:

	def __init__(self):
		self.models = Models()
		self.views = Views()
	def view_accounts(self):
		self.request_info = self.views.account_number()
		number = request_info[0]
		password = request_info[1]
		table = self.models.gettable()
		if table!=none:
			pass
		else:
			self.views.error()

	def create_user(self):
		self.info = self.views.newuser()
		randnum = random.randrange(100000,999999)
		self.models.newuser(self.info[0],self.info[1],randnum)
		
	def transfer(self):
		pass

	def depo_with(self):
		pass



menu = Menu()
menu.create_user()

# something