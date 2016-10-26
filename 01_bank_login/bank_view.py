class Views:

    def __init__(self):
        pass

    def check_user(self):
        user_name = input("Please enter your user name: ")
        password = input("Please enter your password: ")
        return user_name, password

    def new_user(self):
        name = input("Enter a new username: ")
        password = input("Enter a user password: ")
        return(name, password)

    def account_request(self):

        # this should be name
        user_name = input("Please enter your user name: ")
        password = input("Please enter your password: ")
        return user_name, password

    def error(self):
        print("ERROR")




