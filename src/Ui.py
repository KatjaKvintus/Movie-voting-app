from User import User
from datetime import datetime


# Text UI - will be updated to a graphic one later
class Ui():

    movie_suggestions = []
    this_weeks_votes = []
    #all_users = []

    def __init__(self):
        self.ui = []

    # Starting page: user can crate a new user account, existing users can log in
    def startpage():

        print("Welcome to the movie night voting app!\n")
        print("Please choose from below: ")
        print("Click [N] to create new user account")
        print("Click [S] to sign in (if you already have an user account)")

        choice = input("My choice: ")
        print("")

        # Creating new account
        # Both username and password need to be at least 5 characters long
        # Username needs to be unique
        # TO BE ADDED: TRY-EXCEPT if user inputs something else
        if choice == "N" or choice == "n":
            User.create_new_user(User.all_users)

        # Sign-in for old user
        elif choice == "S" or choice == "s":            
            User.returning_user(User.usernames)
    
        # Voting function
        Ui.vote_for_a_movie()

        # Would user like to suggest a movie?
        choice = input("Would you like to suggest a movie for next weeks vote? [Y/N] ")
        if choice == "N" or choice == "n":
            print("Ok! Maybe next time. See you on the movie night!")
        elif choice == "Y" or choice == "y":
            Ui.suggest_new_movie()

    # The main view: 
    def app_main_view():

        date_today = datetime.now()
        weekday_now = date_today.weekday()
        print(f"Today is {weekday_now}, {date_today}")
        print("Movie voting is open!")              # This needs to be changed

    # Voting function
    def vote_for_a_movie():
        print("Voting is open!") 
        print("Please choose your favorite and vote for a movie for the movie night!")
        print("[1] Harry Potter 1")
        print("[2] Harry Potter 2")
        print("[3] Harry Potter 3")
        print("[4] Harry Potter 4")
        print("")
        
        users_vote = input("Vote by choosing a number 1-4: ")
        Ui.this_weeks_votes.append(users_vote)
        
        print("Thank you for voting!")
        print("")
        

     # User can suggest a movie to be added for next movie vote
    def suggest_new_movie(movie_suggestions):
        movie = input("Please write down the name of the movie: ")
        movie_suggestions.append(movie)
        print("Thank you for your input!")
            
    def print_movie_suggestions(movie_suggestions):
        for unit in movie_suggestions:
            print(unit)




