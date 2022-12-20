from entities.Movie import Movie
from repositories.AdminUserRepository import AdminUserRepository
from repositories.MovieRepository import MovieRepository
from services.MovieService import MovieService


class AdminUser():

    
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def create_new_admin_user():

            # Ask user for a username
            username = input("Choose admin username (min. 3 characters long:) ")
            
            username_is_unique = AdminUser.check_if_username_is_unique(username)
            username_is_long_enough = AdminUser.check_username_length(username_is_unique)
            username = username_is_long_enough
            
            password = input("Choose password (min. 3 characters long): ")
            password_is_long_enough = AdminUser.check_password_lenght(password)
            password = password_is_long_enough 

            AdminUser.admin_users[username] = password
            AdminUserRepository.save_new_admin_user_to_file(username, password)     
            
            print(f"\nNew admin user created. Remember to send user account cresentials to the new admin. \n")


    def admin_log_in():

        admin_username = input("What is your admin username? ")
        
        # Check is username exists
        username_exists = False
        while True:

            if username_exists:
                break

            if admin_username not in AdminUserRepository.admin_users:
                print("I don't recognize this username. ")
                admin_username = input("Please give correct admin username: ")
            
            if admin_username in AdminUserRepository.admin_users.keys():
                break
        
        # Ask for a password and check if those match. If not, keep asking password. 
        password = input("What is your password? ")

        if AdminUserRepository.admin_users[admin_username] != password:
            password_is_correct = False

            while True:
                if password_is_correct:
                    break

                print("Incorrect password. Please try again. \n")
                password = input("Password: ")

                if AdminUserRepository.admin_users[admin_username] == password:
                    password_is_correct = True  

            print(f"Welcome, admin {admin_username}!")
            print("")
            AdminUser.admin_tools()

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
        
            if choice == "E" or choice == "e":
                break
            elif choice == "P" or choice == "p":
                MovieService.print_voting_list()
            elif choice == "C" or choice == "c":
                MovieRepository.empty_voting_list()
            elif choice == "R" or choice == "":
                Movie.print_movie_suggestion_list()
            elif choice == "S" or choice == "s":
                Movie.admin_set_voting_list()
            elif choice == "M" or choice == "m":
                AdminUser.create_new_admin_user()
            else:
                print("Pelase choose from the list. ")


    # Check if suggester username is already in use among Admin Users
    def check_if_username_is_unique(username):
        
        username_is_unique = False

        while True:

            if username_is_unique:
                break

            if username in AdminUser.admin_users:
                print("This username is already taken.")
                username = input("Please choose unique username: ")
                continue
            else:
                username_is_unique = True

        return username


    def check_username_length(username):
        while True:
            if len(username) >= 3:
                return username
            else:
                print("You chose too short username. It should be at least 3 characters long.")
                username = input("Please choose longer username: ")


    def check_password_lenght(password):
        while True:
            if len(password) >= 3:
                return password
            else:
                print("You chose too short password. It should be at least 3 characters long.")
                password = input("Please choose longer username: ")