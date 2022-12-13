
from entities.AppUser import AppUser
from entities.Movie import Movie


def main():
    check_and_download_userlist()
    AppUser.set_up_admin_user()

    # This is for testing only
    test_movie_1 = Movie("The Shawshank Redemption", "1994")
    Movie.list_of_movies_to_be_voted.append(test_movie_1)
    test_movie_2 = Movie("The Godfather", "1972")
    Movie.list_of_movies_to_be_voted.append(test_movie_2)
    test_movie_3 = Movie("The Dark Knight", "2008")
    Movie.list_of_movies_to_be_voted.append(test_movie_3 )
    test_movie_4 = Movie("The Godfather: Part II", "1974")
    Movie.list_of_movies_to_be_voted.append(test_movie_4 )

    start()

# Check, is userlist is available and if it is, download it and save users to a dictionary
def check_and_download_userlist():

    ''' # EI TOIMI VIELÄ - KORJATTAVA
    userlist_file_exists = False
    
    while not userlist_file_exists:     

        movieapp_userlist = "movieapp_users.txt"

        try:
            # Test if file exists
            with open(movieapp_userlist, "r") as testfile:
                userlist_file_exists = True
        
        except OSError:
            print("Error: userlist not found.")
            exit()
    '''
    
    movieapp_userlist = "/home/kvintus/ot-harjoitustyo/src/movieapp_users.txt"
    
    # Read file and save users to all_users dictionary
    with open(movieapp_userlist) as file:
        for line in file:
            userdata = line.split(",")
            username = str.strip(userdata[0])
            password = str.strip(userdata[1])
            AppUser.all_users[username] = password
    
        file.close()

        
def start():

    print("Welcome to the movie voting app!\n")

    while True:
        print("Functionalities:")
        print("  [N] Create new user account ")
        print("  [L] Log in as returning user ")
        print("  [A] Log in as the admin user ")
        #print("  [S] Suggest a movie for the next weeks vote")     TO BE ADDED LATER
        print("  [X] Close app\n")
        choice = input("My choice: ")

        if choice == "N" or choice == "n":
            AppUser.create_new_user()
        elif choice == "L" or choice == "l":
            AppUser.log_in_returning_user()
        elif choice == "A" or choice == "a":
            AppUser.admin_tools()
        elif choice == "X" or choice == "x":
            print("Bye!")
            exit()
        
        print("This weeks movie vote is open!")
        answer = input("Would you like to vote? Press [Y]es or [N]o: ")

        if answer == "Y" or answer == "y":
            Movie.vote_for_movie()
    


if __name__ == "__main__":
    main()
