# This file contains classes User and Ui 
# (maybe later will be divided to two separate files)

from datetime import datetime

class User:

    # The class constructor for creating new users
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #self.can_vote = True

    all_users = {}

    # Read usernamelist from a file
    with open("userlist.txt") as userlistfile:

            for row in userlistfile:
                row = row.replace("\n", "")
                user_info = row.split(" ")
                new_user = User(user_info[0], user_info[1])
                all_users.append(new_user)

    def username(self, username: str):
        return username

    # Creating a new user account. The username should be unique and both username and password
    # should be minimum 5 characters long.
    def create_new_user():
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

        if len(password_new) < 5:
            while True:
                if len(password_new) >= 5:
                    break
                print("The password needs to be at least 5 characters long.\n")
                password_new = input("Please choose a new password: ")

        new_user = (username_new, password_new)
        User.all_users.append(new_user)
        User.usernames.append(username_new)
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

##################################################################################
# Text UI - will be updated to a graphic one later
class Ui(User):

    movie_suggestions = []
    this_weeks_votes = []

    def __init__(self):
        self.ui = []

    # Starting page: user can crate a new user account, existing users can log in
    def startpage():

        print("Welcome to the movie night voting app!\n")
        print("Please choose from below: ")
        print("Click [N] to create new user account")
        print("Click [S] to sign in (if you already have an user account)")

        choice = input("My choice: ")
        print("")

        # Creating new account
        # Both username and password need to be at least 5 characters long
        # Username needs to be unique
        # TO BE ADDED: TRY-EXCEPT if user inputs something else
        if choice == "N" or choice == "n":
            User.create_new_user()

        # Sign-in for old user
        elif choice == "S" or choice == "s":            
            User.returning_user(User.usernames)
    
        # Voting function
        Ui.vote_for_a_movie()

        # Would user like to suggest a movie?
        choice = input("Would you like to suggest a movie for next weeks vote? [Y/N] ")
        if choice == "N" or choice == "n":
            print("Ok! Maybe next time. See you on the movie night!")
        elif choice == "Y" or choice == "y":
            Ui.suggest_new_movie()

    # The main view: 
    def app_main_view():

        date_today = datetime.now()
        weekday_now = date_today.weekday()
        print(f"Today is {weekday_now}, {date_today}")
        print("Movie voting is open!")              # This needs to be changed

    # Voting function
    def vote_for_a_movie():
        print("Voting is open!") 
        print("Please choose your favorite and vote foa a movie for the movie night!")
        print("[1] Harry Potter 1")
        print("[2] Harry Potter 2")
        print("[3] Harry Potter 3")
        print("[4] Harry Potter 4")
        print("")
        
        users_vote = input("Vote by choosing a number 1-4: ")
        Ui.this_weeks_votes.append(users_vote)
        
        print("Thank you for voting!")
        print("")
        

     # User can suggest a movie to be added for next movie vote
    def suggest_new_movie(movie_suggestions):
        movie = input("Please write down the name of the movie: ")
        movie_suggestions.append(movie)
        print("Thank you for your input!")
            
    def print_movie_suggestions(movie_suggestions):
        for unit in movie_suggestions:
            print(unit)




