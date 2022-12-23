import sys
from entities.AppUser import App_User
from entities.AdminUser import Admin_user
from repositories.AdminUserRepository import Admin_User_Repository
from repositories.AppUserRepository import App_User_Repository
from entities.Movie import Movie



def main():

    # Downloads user list, admin list and list of movies to be voted
    App_User_Repository.check_and_download_userlist()
    Admin_User_Repository.check_and_download_admin_userlist()
    Movie.download_movie_voting_list()
    Movie.download_movie_suggestions_list()

    start()


# Start menu for all users, both regular and admin
def start():

    print("Welcome to the movie voting app!\n")

    while True:

        print("Functionalities:")
        print("  [N] Create new user account ")
        print("  [L] Log in as returning user ")
        print("  [A] Log in as the admin user ")
        print("  [X] Close app\n")
        choice = input("My choice: ")

        if choice in ("N", "n"):
            App_User.create_new_user()
        elif choice in ("L", "l"):
            App_User.log_in_returning_user()
        elif choice in ("A", "a"):
            Admin_user.admin_log_in()
        elif choice in ("X", "x"):
            print("Bye!")
            sys.exit()
        else:
            print("Please choose from the list. \n")



if __name__ == "__main__":
    main()
