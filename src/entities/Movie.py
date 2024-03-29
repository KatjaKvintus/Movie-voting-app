import sys
from repositories.Movie_Repository import Movie_Repository
from services.Movie_Service import Movie_Service
import datetime

class Movie():


    def __init__(self, movie_name: str, publish_year: str):
        self.movie_name = movie_name
        self.publish_year = publish_year
        self.votes = 0


    def download_movie_voting_list():
        """ Downloads from a file the voting list (that keeps track of given votes).
        """

        current_voting_list_file_exists = False

        while not current_voting_list_file_exists:

            movieapp_voting_list = "src/repositories/voting_list.txt"

            try:
                # Test if file exists
                with open(movieapp_voting_list, encoding="utf-8") as testfile:
                    current_voting_list_file_exists = True
                    testfile.close()

            except OSError:
                print("Error: movie list not found.")
                sys.exit()

        # Read file and save movies list_of_movies_to_be_voted list
        with open(movieapp_voting_list, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                if len(row) > 0:
                    movie_details = row.split(",")
                    new_movie = Movie(movie_details[0], movie_details[1])
                    Movie_Repository.list_of_movies_to_be_voted.append(new_movie)
        file.close()


    def download_movie_suggestions_list():
        """Downloads from a file the voting list (that keeps track of given votes)
        """

        current_voting_list_file_exists = False

        while not current_voting_list_file_exists:

            movieapp_suggestions_list = "src/repositories/voting_suggestions.txt"

            try:
                # Test if file exists
                with open(movieapp_suggestions_list, encoding="utf-8") as testfile:
                    current_voting_list_file_exists = True
                    testfile.close()

            except OSError:
                print("Error: movie list not found.")
                sys.exit()

        # Read file and save movies list_of_movies_to_be_voted list
        with open(movieapp_suggestions_list, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                movie_details = row.split(",")
                new_movie = Movie(movie_details[0], movie_details[1])
                Movie_Repository.list_of_movie_suggestions.append(new_movie)
            file.close()


    def welcome_to_movieapp():
        """Basic functionalities menu for user.
        """

        voting_status = Movie_Repository.check_voting_status()
        voting_status = voting_status.strip()

        if voting_status == "open":
            print("This weeks movie vote is open!\n")
        elif voting_status == "closed":
            print("Unfortunately there is no ongoing movie voting right now.")
        else:
            print(voting_status)


        while True:

            print("What would you like to do?")

            if voting_status == "open":
                print("  [S]ee movie voting list")
                print("  [V]ote for a movie ")
            print("  [P]ropose a movie for nex weeks vote")
            print("  [E]xit app \n")

            answer = input("Answer by giving a letter: ")
            print()

            if answer in ("E", "e"):
                print("Bye!")
                sys.exit()
            elif answer in ("S", "s"):
                Movie_Service.print_voting_list()
            elif answer in ("V", "v"):
                Movie.vote_for_movie()
            elif answer in ("P","p"):
                Movie.suggest_a_movie()
            else:
                print("Please choose from the list. ")


    def get_movie_name(movie):
        return movie.movie_name


    def get_publish_year(movie):
        return movie.publish_year


    def movie_to_string(movie):
        publ_year = str(Movie.get_publish_year(movie))
        description = Movie.get_movie_name(movie) + " (published in " + publ_year + ")"
        return description



    def vote_for_movie():
        """User can vote for a movie by giving a number between 1 and 4.
        """

        print("")
        print("This weeks candidates: ")
        Movie_Service.print_voting_list()
        print("")

        while True:
            vote = input("My vote (write number): ")

            if vote.isnumeric and int(vote) >= 1 and int(vote) <= 4:
                name = Movie_Repository.list_of_movies_to_be_voted[int(vote) - 1].get_movie_name()

                Movie_Repository.save_movie_vote(name)
                print("Thank you for voting! \n")
                break

            print("Please answer by giving number 1, 2, 3 or 4. ")
            continue


    def suggest_a_movie():
        """ Functionality for user: suggesta as movie for next vote. Admin user can add
        the suggestions to voting list.
        """

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
                print("As a true fan, you do must now that the first movie was published 1878.\n")
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



    def set_voting_list():
        """For admin: set up a list of 4 movies for next vote. Admin can add movies
        of their choice or see suggestions from movie suggestion list to add.
        """

        max_amount_of_movies_to_be_added = 4
        setting_successfull = False

        movie_voting_list_length = len(Movie_Repository.list_of_movies_to_be_voted)

        if movie_voting_list_length > 0:
            print("You need to empty the current list before creating a new list. ")
            choice = input("Do you want to empty the old list now? Press [Y]es or [N]o: ")

            if choice in ("Y", "y"):
                Movie_Repository.empty_voting_list
            elif choice in ("N", "n"):
                print("Can't add any more movies right now.")


        movies_added = 0
        suggestions_amount = len(Movie_Repository.list_of_movie_suggestions)

        # If there is/are movie suggestion(s) available, suggest admin to look at the list
        # before adding movies
        if len(Movie_Repository.list_of_movie_suggestions) > 0:
            Movie.offer_movie_suggestions(suggestions_amount)

        movie_spots_left = 4 - len(Movie_Repository.list_of_movies_to_be_voted)

        if movie_spots_left > 0:

            print(f"You can add {movie_spots_left} movies. Choose wisely! \n")

            movies_listed = ""

            while movies_added < max_amount_of_movies_to_be_added:
                movie_name = input(f"Write movie no {movies_added + 1} name: ")
                publish_year = input("Publish year: ")
                new_movie = Movie(movie_name, publish_year)
                Movie_Repository.list_of_movies_to_be_voted.append(new_movie)
                movies_listed += movie_name + "," + publish_year + ";"
                movies_added += 1
                print()

            Movie_Repository.save_voting_list_to_file(movies_listed)
            print()
            setting_successfull = True
            print("Setting movie list succesfull.\n")
            Movie_Repository.open_voting()
            Movie_Repository.clear_all_votes()        # deletes previously given votes
            return setting_successfull
        
        else:
            print("Movie voting list is now full. ")


    def offer_movie_suggestions(suggestions_amount):
        ''' While setting new voting list, if there are suggestions in the list,
        the admin will be asked if they want to check it first and maybe add some
        of those to the final voting list.
        '''

        print(f"Movie suggestions list has {suggestions_amount} suggestion(s) available.")
        print("Would you like to see the list before adding any movies for vote? \n")

        choice1 = input("If you do, press [Y] - if not, press [Ń]:")
        print()

        while True:

            if choice1 in ("Y", "y"):
                Movie.print_movie_suggestion_list()
                print()

                print("If you want to add one of these for voting, press [A].")
                
                #if len(Movie_Repository.list_of_movie_suggestions) <= 4:
                #    print("If you want to add all to the voting list, press [Z].")
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

                #elif choice2 in ("Z", "z"):
                 #   for suggestion in Movie_Repository.list_of_movie_suggestions:
                  #      Movie_Repository.list_of_movies_to_be_voted.append(suggestion)
                   #     Movie_Repository.save_voting_list_to_file(suggestion.movie_to_string())
                    #    Movie_Repository.list_of_movie_suggestions.clear()
                    #break
                
                elif choice2 in ("X", "x"):
                    break
                else:
                    print("I didn't recognise that. Please give the number of the movie you want to add.")
            elif choice1 in ("N", "n"):
                break
            else:
                    print("I didn't recognise that. Please give the number of the movie you want to add.")


    def print_voting_list_for_admin():
        """Prints a list of movies if it is available.
        """

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


    def print_movie_suggestion_list():
        """Prints the current movie suggestions list
        """

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
