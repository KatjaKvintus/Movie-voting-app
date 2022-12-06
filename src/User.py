#from Ui import Ui

class User:

    # Keeps track of all usernames in use
    usernames = []

    # Keeps track of users
    all_users = []

    # The class constructor for creating new users
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #self.can_vote = True      

    def load_users(all_users):
        # Read usernamelist from a file
        with open("userlist.txt") as userlistfile:

            for row in userlistfile:
                row = row.replace("\n", "")
                user_info = row.split(" ")
                new_user = User(user_info[0], user_info[1])
                User.usernames.append(user_info[0])
                all_users.append(new_user)
        
        return all_users

    def username(self, username: str):
        return username

    # Creating a new user account. The username should be unique and both username and password
    # should be minimum 5 characters long.
    def create_new_user(all_users):
        username_new = input("Write the username you like to use: ")

        while True:
            if username_new not in User.usernames and len(username_new) >= 5:
                break
            if username_new in User.usernames:
                print("This username is already taken.")
            if len(username_new) < 5:
                print("The username has to be at least 5 characters long")
            username_new = input("Please choose new username: ")

        password_new = input("Choose a password: ")

        if len(password_new) < 5:
            while True:
                if len(password_new) >= 5:
                    break
                print("The password needs to be at least 5 characters long.\n")
                password_new = input("Please choose a new password: ")

        new_user = User(username_new, password_new)
        all_users.append(new_user)
        print(f"Nice to meet you, {username_new }!")
        print("")
    

    # For returning users: check username and password
    def returning_user(usernames):

        username_old = input("Please fill in your username: ")
        check_username_result = User.check_returning_users_username(username_old)

        if check_username_result == False:
            while True:
                if check_username_result == True:
                    break
                print("Can't find this username - please check for typos and try again")
                username_old = input("Please fill in your username: ")

            password_old = input("Please fill in your password: ")            

            while True:
                check_password_result = User.check_password(password_old)
                if check_password_result == True:
                    break

                print("Wrong password - please check for typos and try again")
                password_old = input("Please fill in your password: ")

            print(f"Welcome back, {username_old }!")
            print("")

    # Checking if username exists
    def check_returning_users_username(users_username):
        username_found = False
        for account in Ui.all_users:
            if account.username == users_username:
                username_found = True
        return username_found
    
    # Checking if password matches the username
    def check_password(users_username, users_password):
        password_correct = False
        for account in Ui.all_users:
            if account.password == users_password:
                password_correct = True
        return password_correct
