from entities.AppUser import AppUser
from entities.AdminUser import AdminUser
#from entities.Movie import Movie
from repositories.AdminUserRepository import AdminUserRepository
from repositories.AppUserRepository import AppUserRepository
from repositories.MovieRepository import MovieRepository



def main():

    AppUserRepository.check_and_download_userlist()
    AdminUserRepository.check_and_download_userlist()
    MovieRepository.download_movie_lists()
    

    start()


# Start menu for all users, both regular and admind
def start():

    print("Welcome to the movie voting app!\n")

    while True:

        print("Functionalities:")
        print("  [N] Create new user account ")
        print("  [L] Log in as returning user ")
        print("  [A] Log in as the admin user ") 
        print("  [X] Close app\n")
        choice = input("My choice: ")

        if choice == "N" or choice == "n":
            AppUser.create_new_user()
        elif choice == "L" or choice == "l":
            AppUser.log_in_returning_user()
        elif choice == "A" or choice == "a":
            AdminUser.admin_log_in()
        elif choice == "X" or choice == "x":
            print("Bye!")
            exit()
        else:
            print("Pelase choose from the list. \n")

   

if __name__ == "__main__":
    main()
