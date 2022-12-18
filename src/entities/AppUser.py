from entities.Movie import Movie


class AppUser:

    # Dictionary to store all users: username as the key and password as the value
    all_users = {}
    admin_users = {}


    # The class constructor for creating new users
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_admin = False


    def create_new_user():

        username = input("Choose username (min. 3 characters long:) ")
        
        username_is_unique = AppUser.check_if_username_is_unique(username)
        username_is_long_enough = AppUser.check_username_length(username_is_unique)
        username = username_is_long_enough
        
        password = input("Choose password (min. 3 characters long): ")
        password_is_long_enough = AppUser.check_password_lenght(password)
        password = password_is_long_enough 

        AppUser.all_users[username] = password

        # Read file and save users to all_users dictionary
        with open("movieapp_users.txt", "a") as file:
            file.write(username + "," + password)
            file.write("\n")
            file.close()
        
        print("")
        print(f"Welcome to the movieapp, {username}!\n")
        Movie.welcome_to_movieapp()
    
    
    # Check returning users username and password
    def log_in_returning_user():

        username = input("What is your username? ")
        
        # Check is username exists
        username_exists = False
        while True:

            if username_exists:
                break

            if username not in AppUser.all_users.keys():
                print("I don't recognize this username. ")
                username = input("Please give correct username: ")
            
            if username in AppUser.all_users.keys():
                break
        
        # Ask for a password and check if those match. If not, keep asking password. 
        password = input("What is your password? ")

        if AppUser.all_users[username] != password:
            password_is_correct = False

            while True:
                if password_is_correct:
                    break

                print("Incorrect password. Please try again. \n")
                password = input("Password: ")

                if AppUser.all_users[username] == password:
                    password_is_correct = True  
        
        print(f"Welcome to Movie voting app, {username}!\n")
        Movie.welcome_to_movieapp()



    def create_new_admin_user():

        # Ask user for a username
        username = input("Choose admin username (min. 3 characters long:) ")
        
        username_is_unique = AppUser.check_if_username_is_unique(username)
        username_is_long_enough = AppUser.check_username_length(username_is_unique)
        username = username_is_long_enough
        
        password = input("Choose password (min. 3 characters long): ")
        password_is_long_enough = AppUser.check_password_lenght(password)
        password = password_is_long_enough 

        AppUser.admin_users[username] = password

        # Read file and save users to all_users dictionary
        with open("movieapp_admin_users.txt", "a") as file:
            file.write(username + "," + password)
            file.write("\n")
            file.close()
        
        print("")
        print(f"New admin user created. Remember to send user account cresentials to the new admin. \n")


    def check_if_username_is_unique(username):
        
        username_is_unique = False

        while True:

            if username_is_unique:
                break

            if username in AppUser.admin_users.keys() or AppUser.all_users.keys():
                print("This username is already taken.")
                username = input("Please choose unique username: ")
            
            if username not in AppUser.admin_users.keys() or AppUser.all_users.keys():
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


    def admin_tools():

        admin_username = input("Give admin username: ")
        admin_password = input("Give admin password: ")

        if AppUser.admin_users[admin_username] != admin_password:
            print("One or both incorrect. Are you trying to scam me? Better luck next time. Bye!")
            exit()
        
        print("Welcome, admin {admin_username}!")
        print("")
        
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
                Movie.print_voting_list()
            elif choice == "C" or choice == "c":
                Movie.admin_empty_voting_list()
            elif choice == "R" or choice == "":
                Movie.print_movie_suggestion_list()
            elif choice == "S" or choice == "s":
                Movie.admin_set_voting_list()
            elif choice == "M" or choice == "m":
                AppUser.create_new_admin_user()


        