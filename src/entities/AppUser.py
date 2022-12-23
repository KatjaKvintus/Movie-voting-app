from entities.Movie import Movie
from repositories.AppUserRepository import App_User_Repository


class App_User:
    """ Class responsible for creating nre user accounts and providing tools for users.
    """


    # The class constructor for creating new users
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.has_voted = False


    
    def create_new_user():
        """Create new user. Ask asks the user for a username and password as input.
        Username has to be unique (not in use among other users) and at least 3 characters long. 
        """

        username = input("Choose username (min. 3 characters long:) ")

        username_is_unique = App_User.check_if_username_is_available(username)
        username_is_long_enough = App_User.check_username_length(username_is_unique)
        username = username_is_long_enough

        password = input("Choose password (min. 3 characters long): ")
        password_is_long_enough = App_User.check_password_lenght(password)
        password = password_is_long_enough

        App_User_Repository.all_users[username] = password

        App_User_Repository.save_new_user_to_file(username, password)

        print("")
        print(f"Welcome to the movieapp, {username}!\n")
        Movie.welcome_to_movieapp()


    
    def log_in_returning_user():
        """ Check returning users username and password. Username has to be created
        previously and password has to match username.
        """

        username = input("What is your username? ")

        # Check is username exists
        username_exists = False
        while True:

            if username_exists:
                break

            if username not in App_User_Repository.all_users:
                print("I don't recognize this username. ")
                username = input("Please give correct username: ")

            if username in App_User_Repository.all_users:
                break

        # Ask for a password and check if those match. If not, keep asking password.
        password = input("What is your password? ")

        if App_User_Repository.all_users[username] != password:
            password_is_correct = False

            while True:
                if password_is_correct:
                    break

                print("Incorrect password. Please try again. \n")
                password = input("Password: ")

                if App_User_Repository.all_users[username] == password:
                    password_is_correct = True

        print(f"Welcome to Movie voting app, {username}!\n")
        Movie.welcome_to_movieapp()


    
    def check_if_username_is_available(username):
        """Verification function: check if suggester username is already in use among AppUsers.
        """
        username_is_unique = False

        while True:

            if username_is_unique:
                break

            if username in App_User_Repository.all_users:
                print("This username is already taken.")
                username = input("Please choose unique username: ")
                continue
            username_is_unique = True

        return username


    
    def check_username_length(username):
        """ If username length is >= 3, returns username. If not, asks again.
        """
        while True:
            if len(username) >= 3:
                return username
            print("You chose too short username. It should be at least 3 characters long.")
            username = input("Please choose longer username: ")


    
    def check_password_lenght(password):
        """If password length is >= 3, returns password. If not, asks again.
        """
        while True:
            if len(password) >= 3:
                return password
            print("You chose too short password. It should be at least 3 characters long.")
            password = input("Please choose longer username: ")
