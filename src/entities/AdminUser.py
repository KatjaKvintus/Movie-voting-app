from entities import AppUser
from entities import Movie


class AdminUser():

    # Dictionary to store all admin users: username as the key and password as the value
    admin_users = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def create_new_admin_user():

            # Ask user for a username
            username = input("Choose admin username (min. 3 characters long:) ")
            
            username_is_unique = AppUser.check_if_username_is_unique(username)
            username_is_long_enough = AppUser.check_username_length(username_is_unique)
            username = username_is_long_enough
            
            password = input("Choose password (min. 3 characters long): ")
            password_is_long_enough = AppUser.check_password_lenght(password)
            password = password_is_long_enough 

            AdminUser.admin_users[username] = password

            # Read file and save users to all_users dictionary
            with open("movieapp_admin_users.txt", "a") as file:
                file.write(username + "," + password)
                file.write("\n")
                file.close()
            
            print("")
            print(f"New admin user created. Remember to send user account cresentials to the new admin. \n")


    # Tools menu for admin level users
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
                else:
                    print("Pelase choose from the list. ")

