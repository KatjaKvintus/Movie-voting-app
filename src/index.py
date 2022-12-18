
from entities.AppUser import AppUser
from entities.Movie import Movie


def main():

    check_and_download_userlists()
    download_movie_lists()

    ######################## This is for testing only
    test_movie_1 = Movie("The Shawshank Redemption", "1994")
    Movie.list_of_movies_to_be_voted.append(test_movie_1)
    test_movie_2 = Movie("The Godfather", "1972")
    Movie.list_of_movies_to_be_voted.append(test_movie_2)
    test_movie_3 = Movie("The Dark Knight", "2008")
    Movie.list_of_movies_to_be_voted.append(test_movie_3 )
    test_movie_4 = Movie("The Godfather: Part II", "1974")
    Movie.list_of_movies_to_be_voted.append(test_movie_4 )

    start()


def start():

    print("Welcome to the movie voting app!\n")

    while True:
        print("Functionalities:")
        print("  [N] Create new user account ")
        print("  [L] Log in as returning user ")
        print("  [A] Log in as the admin user ")
        print("  [S] Suggest a movie for the next weeks vote ")    
        print("  [X] Close app\n")
        choice = input("My choice: ")

        if choice == "N" or choice == "n":
            AppUser.create_new_user()
        elif choice == "L" or choice == "l":
            AppUser.log_in_returning_user()
        elif choice == "A" or choice == "a":
            AppUser.admin_tools()
        elif choice == "S" or choice == "s":
            Movie.
        elif choice == "X" or choice == "x":
            print("Bye!")
            exit()


# Check if userlist and admin userlist are available and if it is, download both and save users to a dictionaries
def check_and_download_userlists():

    userlist_file_exists = False
    
    while not userlist_file_exists:     

        #movieapp_userlist = "movieapp_users.txt"       PALAUTA ENNEN KUIN JULKAISET!!!!
        movieapp_userlist = "/home/kvintus/ot-harjoitustyo/src/movieapp_users.txt"

        try:
            # Test if file exists
            with open(movieapp_userlist) as testfile:
                userlist_file_exists = True
        
        except OSError:
            print("Error: userlist not found.")
            exit()

    # Read file and save users to all_users dictionary
    with open(movieapp_userlist) as file:
        for line in file:
            userdata = line.split(",")
            username = str.strip(userdata[0])
            password = str.strip(userdata[1])
            AppUser.all_users[username] = password
    
        file.close()

    admin_userlist_file_exists = False
   
    while not admin_userlist_file_exists:     

        #movieapp_admin_userlist = "movieapp_admin_users.txt"       # PALAUTA ENNEN KUIN JULKAISET!!!!
        movieapp_admin_userlist = "/home/kvintus/ot-harjoitustyo/src/movieapp_admin_users.txt"

        try:
            # Test if file exists
            with open(movieapp_admin_userlist) as testfile:
                admin_userlist_file_exists = True
        
        except OSError:
            print("Error: admin userlist not found.")
            exit()
    
        # Read file and save admin users to all_users dictionary
        with open(movieapp_admin_userlist) as file:
            for line in file:
                userdata = line.split(",")
                username = str.strip(userdata[0])
                password = str.strip(userdata[1])
                AppUser.admin_users[username] = password
        
            file.close()


    # Read file and save users to all_users dictionary
    with open(movieapp_userlist) as file:
        for line in file:
            userdata = line.split(",")
            username = str.strip(userdata[0])
            password = str.strip(userdata[1])
            AppUser.all_users[username] = password
    
        file.close()
        

def download_movie_lists():

    current_voting_list_file_exists = False
    
    while not current_voting_list_file_exists:     

        #movieapp_voting_list = "entities/voting_list.txt"       PALAUTA ENNEN KUIN JULKAISET!!!!
        movieapp_voting_list = "/home/kvintus/ot-harjoitustyo/src/entities/voting_list.txt"

        try:
            # Test if file exists
            with open(movieapp_voting_list) as testfile:
                current_voting_list_file_exists = True
        
        except OSError:
            print("Error: movie list not found.")
            exit()

    # Read file and save movies list_of_movies_to_be_voted list
    with open(movieapp_voting_list) as file:
        for movie in file:
            Movie.list_of_movies_to_be_voted.append(movie)
    
        file.close()

        
    

if __name__ == "__main__":
    main()
