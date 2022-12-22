from entities.Movie import Movie
from repositories.AdminUserRepository import Admin_User_Repository
from repositories.MovieRepository import Movie_Repository
from services.MovieService import Movie_Service


class Admin_user():


    def __init__(self, username, password):
        self.username = username
        self.password = password


    def create_new_admin_user():

        # Ask user for a username
        username = input("Choose admin username (min. 3 characters long:) ")

        username_is_unique = Admin_user.check_if_username_is_available(username)
        username_is_long_enough = Admin_user.check_username_length(username_is_unique)
        username = username_is_long_enough

        password = input("Choose password (min. 3 characters long): ")
        password_is_long_enough = Admin_user.check_password_lenght(password)
        password = password_is_long_enough

        Admin_user.admin_users[username] = password
        Admin_User_Repository.save_new_admin_user_to_file(username, password)

        print(f"\nNew admin user created.")
        print("Remember to send user account cresentials to the new admin. \n")


    # Log in for admin users. Check if username and password match.
    def admin_log_in():

        admin_username = input("What is your admin username? ")

        # Check is username exists
        username_exists = False
        while True:

            if username_exists:
                username_exists = True
                break

            if admin_username not in Admin_User_Repository.admin_users:
                print("I don't recognize this username. ")
                admin_username = input("Please give correct admin username: ")

            if admin_username in Admin_User_Repository.admin_users:
                break

        # Ask for a password and check if those match. If not, keep asking password.
        admin_password = input("What is your password? ")

        if Admin_User_Repository.admin_users[admin_username] != admin_password:
            password_is_correct = False

            while True:
                if password_is_correct:
                    break

                print("Incorrect password. Please try again. \n")
                admin_password = input("Password: ")

                if Admin_User_Repository.admin_users[admin_username] == admin_password:
                    password_is_correct = True

        print(f"Welcome, admin {admin_username}!")
        print("")
        Admin_user.admin_tools()

    # Tools menu for admin level users
    def admin_tools():

        while True:

            print("Choose function:")
            print("  [P]rint current voting list ")
            print("  [C]lear voting list ")
            print("  [R]ead suggestions for next weeks movie voting ")
            print("  [S]et up a new votings list ")
            print("  [M]ake new admin user account ")
            print("  [E]xit admin tools \n")
            choice = input("My choice: ")

            if choice in ("E", "e"):
                break
            if choice in("P", "p"):
                Movie.print_voting_list_for_admin()
            elif choice in ("C", "c"):
                Movie_Repository.empty_voting_list()
            elif choice in ("R", "r"):
                Movie.print_movie_suggestion_list()
            elif choice in ("S", "s"):
                Movie.set_voting_list()
            elif choice in ("M", "m"):
                Admin_user.create_new_admin_user()
            else:
                print("Please choose from the list. \n")


    # Check if suggester username is already in use among Admin Users
    def check_if_username_is_available(self, username):

        username_is_unique = False

        while True:

            if username_is_unique:
                break

            if username in Admin_user.admin_users:
                print("This username is already taken.")
                username = input("Please choose unique username: ")
                continue
            else:
                username_is_unique = True

        return username


    def check_username_length(self, username):
        while True:
            if len(username) >= 3:
                return username
            print("You chose too short username. It should be at least 3 characters long.")
            username = input("Please choose longer username: ")


    def check_password_lenght(self, password):
        while True:
            if len(password) >= 3:
                return password
            print("You chose too short password. It should be at least 3 characters long.")
            password = input("Please choose longer username: ")
