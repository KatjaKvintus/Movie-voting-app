class User:

    # The class constructor for creating new users
    def __init__(self, username : str, password: str):
        self.username = username
        self.password = password
    
    all_users = []
    usernames = []

    def username(self, username: str):
        return username

    def createNewUser():
        username_new = input("Write the username you like to use: ")

        while True:

            if username_new not in User.all_users and len(username_new) >= 5:
                break

            if username_new in User.usernames:
                print("This username is already taken.")
            
            if len(username_new) < 5:
                print("The username has to be at least 5 characters long")
                
            username_new = input("Please choose new username: ")
            
            
        password_new = input("Choose a password: ")

        if len(password_new ) < 5:

            while True: 

                if len(password_new) >= 5:
                    break

                print("The password needs to be at least 5 characters long.\n")
                password_new  = input("Please choose a new password: ")

        new_user = (username_new, password_new )
        User.all_users.append(new_user)
        User.usernames.append(username_new)

        print(f"Nice to meet you, {username_new }!")
        
    

# Text UI - will be updated to a graphic one later
class Ui(User):

    def __init__(self):
        self.ui = []

    print("Welcome to the movie night voting app!\n")
    print("Please choose from below: ")
    print("Click [N] to create new user account")
    print("Click [S] to sign in (if you already have an user account")

    choice = input("My choice: ")

    # Creating new account
    # Both username and password need to be at least 5 characters long
    # Username needs to be unique
    if choice == "N":
        
        User.createNewUser()
    
    # Sign-in for old user
    if choice == "S":

        username_old = input("Please fill in your username: ")

        if username_old not in usernames:

            while True:

                if username_old in usernames:
                    break

                print("Can't find this username - please check for typos and try again")
                username_old = input("Please fill in your username: ")
        
        password_old = input("Please fill in your password: ")

        if password_old != username_old.password:

            while True:

                if password_old == username_old.password:
                    break

                print("Wrong password - please check for typos and try again")
                password_old = input("Please fill in your password: ")

        print(f"Welcome back, {username_new }!")





