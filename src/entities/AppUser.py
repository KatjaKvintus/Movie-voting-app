from entities.Movie import Movie


class AppUser:

    # Dictionary to store all users: username as the key and password as the value
    all_users = {}


    # The class constructor for creating new users
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_admin = False


    def create_new_user():

        # Ask user for a username
        username = input("Choose username (min. 3 characters long:) ")
        
        # Checking if username is allready in use
        username_is_unique = False

        while True:

            if username_is_unique:
                break

            if username in AppUser.all_users.keys():
                print("This username is already taken.")
                username = input("Please choose unique username: ")
            
            if username not in AppUser.all_users.keys():
                username_is_unique = True
        
        # Checking if username is too short
        while True:

            if len(username) >= 3:
                break
            else:
                print("You chose too short username. It should be at least 3 characters long.")
                username = input("Please choose longer username: ")
        
        # Ask user for a password
        password = input("Choose password (min. 3 characters long): ")

        # Check if password is long enough
        while True:

            if len(password) >= 3:
                break
            else:
                print("You chose too short password. It should be at least 3 characters long.")
                password = input("Please choose longer username: ")

        #new_user = AppUser(username, password)

        # Read file and save users to all_users dictionary
        with open("movieapp_users.txt", "a") as file:
            file.write(username + "," + password)
            file.write("\n")
            file.close()
        
        print("")
        print(f"Welcome to the movieapp, {username}!\n")
        
    
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


    def set_up_admin_user():
        admin_name = "Admin"
        admin_password = "Password"

        admin_user = AppUser(admin_name, admin_password)
        admin_user.is_admin = True
    

    def admin_tools():

        username = input("Give admin username: ")
        password = input("Give admin password: ")

        if username != "admin" or password != "password":
            print("One or both incorrect. Are you trying to scam me? Good luck next time. Bye!")
            exit()

        print("")
        
        while True:

            print("Choose function:")
            print("  [P]rint current voting list ")
            print("  [C]lear voting list ")
            print("  [S]et up a new votings list ")
            print("  [E]xit admin tools \n")
            choice = input("My choice: ")
        
            if choice == "E" or choice == "e":
                break
            elif choice == "P" or choice == "p":
                Movie.print_voting_list()
            elif choice == "C" or choice == "c":
                Movie.admin_empty_voting_list()
            elif choice == "S" or choice == "s":
                Movie.admin_set_voting_list()


        