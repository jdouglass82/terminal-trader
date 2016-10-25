class Views:

 	def __init__(self):
 		pass

 	def account_request(self):

 		account_number = input("Please enter your account number: ")

 		password = input("Please enter your password: ")

 		return account_number, password

 	def error(self):
 		print("ERROR")

 	def newuser(self):
 		name = input("Type your username: ")
 		password = input("Type your password: ")
 		return(name,password)