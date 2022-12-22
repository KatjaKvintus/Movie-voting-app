import sys
from repositories.MovieRepository import Movie_Repository
from services.MovieService import Movie_Service
import datetime

class Movie():


    def __init__(self, movie_name: str, publish_year: str):
        self.movie_name = movie_name
        self.publish_year = publish_year
        self.votes = 0


    # Downloads from a file the voting list (that keeps track of given votes during )
    def download_movie_voting_list():

        current_voting_list_file_exists = False

        while not current_voting_list_file_exists:

            #movieapp_voting_list = "repositories/voting_list.txt" #PALAUTA ENNEN KUIN JULKAISET!!!!
            movieapp_voting_list = "/home/kvintus/ot-harjoitustyo/src/repositories/voting_list.txt"

            try:
                # Test if file exists
                with open(movieapp_voting_list) as testfile:
                    current_voting_list_file_exists = True
                    testfile.close()

            except OSError:
                print("Error: movie list not found.")
                sys.exit()

        # Read file and save movies list_of_movies_to_be_voted list
        with open(movieapp_voting_list) as file:
            for row in file:
                row = row.replace("\n", "")
                movie_details = row.split(",")
                new_movie = Movie(movie_details[0], movie_details[1])
                Movie_Repository.list_of_movies_to_be_voted.append(new_movie)
            file.close()
    

    # Downloads from a file the voting list (that keeps track of given votes during )
    def download_movie_suggestions_list():

        current_voting_list_file_exists = False

        while not current_voting_list_file_exists:

            #movieapp_voting_list = "repositories/voting_suggestions.txt" #PALAUTA ENNEN KUIN JULKAISET!!!!
            movieapp_suggestions_list = "/home/kvintus/ot-harjoitustyo/src/repositories/voting_suggestions.txt"

            try:
                # Test if file exists
                with open(movieapp_suggestions_list) as testfile:
                    current_voting_list_file_exists = True
                    testfile.close()

            except OSError:
                print("Error: movie list not found.")
                sys.exit()

        # Read file and save movies list_of_movies_to_be_voted list
        with open(movieapp_suggestions_list) as file:
            for row in file:
                row = row.replace("\n", "")
                movie_details = row.split(",")
                new_movie = Movie(movie_details[0], movie_details[1])
                Movie_Repository.list_of_movie_suggestions.append(new_movie)
            file.close()


    # Movie basic functionalities for user
    def welcome_to_movieapp():

        voting_status = Movie_Repository.check_voting_status()


        if voting_status == "open":
            print("This weeks movie vote is open!\n")
        else:
            print("Unfortunately there is no ongoing movie voting right now.")


        while True:

            print("What would you like to do?")

            if voting_status == "open":
                print("  [S]ee movie voting list")
                print("  [V]ote for a movie ")
                print("  [P]ropose a movie for nex weeks vote")
                print("  [E]xit app \n")

            answer = input("Answer by giving a letter: ")

            if answer in ("E", "e"):
                print("Bye!")
                sys.exit()
            elif answer in ("S", "s"):
                Movie_Service.print_voting_list()
            elif answer in ("V", "v"):
                Movie.suggest_a_movie()
            elif answer in ("P","p"):
                Movie.suggest_a_movie()
            else:
                print("Please choose from the list. ")


    def get_movie_name(movie):
        return movie.movie_name


    def get_publish_year(movie):
        return movie.publish_year


    def movie_to_string(movie):
        description = Movie.get_movie_name(movie) + " (published in " + Movie.get_publish_year(movie) + ")"
        return description


    # User can vote for a movie by giving number 1-4.
    def vote_for_movie():

        print("")
        print("This weeks candidates: ")
        Movie_Service.print_voting_list()
        print("")

        while True:
            vote = input("My vote (write number): ")

            if vote.isnumeric and int(vote) >= 1 and int(vote) <= 4:
                the_movie = Movie_Repository.list_of_movies_to_be_voted[vote - 1].get_movie_name()

                Movie_Repository.save_movie_vote(the_movie)
                print("Thank you for voting! \n")
                break

            print("Please answer by giving number 1, 2, 3 or 4. ")
            continue


    def suggest_a_movie():

        print("You can suggest one movie for next weeks voting.")    
        print("App admin(s) will decide, if this movie is worthy.\n")

        while True:
            movie_name = input("Please give movie name: ")

            if len(movie_name) < 1:
                print("Movie name is too short. Please give correct movie name. \n")
                continue
            break

        while True:
            publish_year = input("Please give movie publish year: ")
            current_date = datetime.date.today()
            current_year = current_date.year


            if int(publish_year) < 1878:
                print("Please check the year.")
                print("As a true movie fan, you do must now that the first movie was published 1878.\n")
                continue
            if int(publish_year) > current_year + 1:
                print("Please check the year.")
                print("It can't be bigger than current year. (We are no going back to the future.)")
                continue
            break

        new_movie = Movie(movie_name, publish_year)
        Movie_Repository.list_of_movie_suggestions.append(new_movie)

        Movie_Repository.save_movie_suggestion(movie_name, publish_year)

        print("Thank you for your suggestion!\n")


    # For admin: set up a list of 4 movies for next vote. Admin can add movies of their choice
    # or pick max 4 suggestions from movie suggestion list.
    def set_voting_list():

        max_amount_of_movies_to_be_added = 4
        setting_successfull = False

        movie_voting_list_length = len(Movie_Repository.list_of_movies_to_be_voted)

        if len(Movie_Repository.list_of_movies_to_be_voted) > 0:
            print("You need to empty the current list before creating a new list. ")
            choice = input("Do you want to empty old list? Press [Y]es or [N]o: ")

            if choice in ("Y", "y"):
                Movie_Repository.empty_voting_list
            elif choice in ("N", "n"):
                print("Can't add any more movies right now.")
                return setting_successfull

        movies_added = 0

        # If there is movie suggestions available, suggest admin to look at them before adding movies
        if len(Movie_Repository.list_of_movie_suggestions) > 0:

            print(f"Movie suggestions list has {len(Movie_Repository.list_of_movie_suggestions)} suggestion(s) available.")
            print("Would you like to see the list before adding any movies for vote? \n")
        
            choice1 = input("If you do, press [Y] - if not, press [Ń]:")
            print()

            while True:
                if choice1 in ("Y", "y"):
                    Movie.print_movie_suggestion_list()
                    print()
                    
                    print("If you want to add one of these for voting, press [A].")
                    if len(Movie_Repository.list_of_movie_suggestions) <= 4:
                        print("If you want to add all to the voting list, press [Z].")
                    print("If not, press [X].\n")

                    choice2 = input("I choose: ")
                    print()

                    if choice2 in ("A", "a"):
                        number = input("Which movie do you want to add? Give the number of the movie.")

                        while True:
                            if int(number) < len(Movie_Repository.list_of_movie_suggestions) and int(number) > 0:
                                add_this_movie = Movie_Repository.list_of_movie_suggestions[int(number) - 1]
                                Movie_Repository.list_of_movies_to_be_voted.append(add_this_movie)
                                Movie_Repository.save_voting_list_to_file(add_this_movie.movie_to_string())
                                Movie_Repository.list_of_movie_suggestions.pop(int(number))
                                movies_added += 1
                                break
                            else:
                                print("I didn't recognise that. Please give the number of the movie you want to add.")
                            

                    elif choice2 in ("Z", "z"):
                        for suggestion in Movie_Repository.list_of_movie_suggestions:
                            Movie_Repository.list_of_movies_to_be_voted.append(suggestion)
                            Movie_Repository.save_voting_list_to_file(suggestion.toString())
                            Movie_Repository.list_of_movie_suggestions.clear()
                        break
                    
                    elif choice2 in ("X", "x"):
                        break
                    else:
                        print("I didn't recognise that. Please give the number of the movie you want to add.")

        movie_spots_left = 4 - len(Movie_Repository.list_of_movies_to_be_voted)

        if movie_spots_left > 0:

            print(f"You can add {movie_spots_left} movies. Choose wisely! \n")

            movies_listed = ""

            while movies_added < max_amount_of_movies_to_be_added:
                movie_name = input(f"Write movie no {movies_added + 1} name: ")
                publish_year = input("Publish year: ")
                new_movie = Movie(movie_name, publish_year)
                Movie_Repository.list_of_movies_to_be_voted.append(new_movie)
                movies_listed = movie_name + "," + publish_year + ";"
                movies_added += 1
                print()

            Movie_Repository.save_voting_list_to_file(movies_listed)
            print()
            setting_successfull = True
            print("Setting movie list succesfull.\n")
            return setting_successfull
        
        else:
            print("Movie voting list is now full. ")


    # Prints a list of movies if it is available. 
    def print_voting_list_for_admin():

        if len(Movie_Repository.list_of_movies_to_be_voted) == 0:
            print("The movie list is empty.\n")
        else:
            counter = 1
            print("The movie list for this weeks vote is: ")

            for movie in Movie_Repository.list_of_movies_to_be_voted:
                candidate_description = Movie.movie_to_string(movie) 
                print(f"[{counter}]: {candidate_description}")
                counter += 1
            print("")

    # Prints the current movie suggestions list
    def print_movie_suggestion_list():

        if len(Movie_Repository.list_of_movie_suggestions) == 0:
            print("Suggestion list is empty. \n")
        else:
            counter = 1
            print("The suggestions are: ")

            for movie in Movie_Repository.list_of_movie_suggestions:
                candidate_description = Movie.movie_to_string(movie)
                print(f"[{counter}]: {candidate_description}")
                counter += 1
            print("")


    