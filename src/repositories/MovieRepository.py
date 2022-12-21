import sys


class Movie_Repository:

    list_of_movies_to_be_voted = []
    list_of_movie_suggestions = []


    # Downloads from a file the voting list (that keeps track of given votes during )
    def download_movie_lists():

        current_voting_list_file_exists = False

        while not current_voting_list_file_exists:

            #movieapp_voting_list = "repositories/voting_list.txt" #PALAUTA ENNEN KUIN JULKAISET!!!!
            movieapp_voting_list = "/home/kvintus/ot-harjoitustyo/src/repositories/voting_list.txt"

            try:
                # Test if file exists
                with open(movieapp_voting_list) as testfile:
                    current_voting_list_file_exists = True

            except OSError:
                print("Error: movie list not found.")
                sys.exit()

        # Read file and save movies list_of_movies_to_be_voted list
        with open(movieapp_voting_list) as file:
            for movie in file:
                Movie_Repository.list_of_movies_to_be_voted.append(movie)

            file.close()


    # Return "open" or "closed" depending on if the voting is open or not
    def check_voting_status():

        current_voting_list_file_exists = False

        while not current_voting_list_file_exists:

            #movieapp_voting_status = "repositories/voting_status.txt" PALAUTA ENNEN KUIN JULKAISET!!!!
            movieapp_voting_status = "/home/kvintus/ot-harjoitustyo/src/repositories/voting_status.txt"

            try:
                # Test if file exists
                with open(movieapp_voting_status) as testfile:
                    current_voting_list_file_exists = True

            except OSError:
                print("Error: voting status not found.")
                sys.exit()

        # Read file and save movies list_of_movies_to_be_voted list
        with open(movieapp_voting_status) as file:
            for row in file:
                status_now = row

            file.close()

        return status_now


    # The vote, given by user, is saved to a file.
    def save_movie_vote(self, movie_name):

        with open("repositories/votes.txt", "a") as file:
            file.write(movie_name + "\n")
        file.close()


    # Saves movie suggestion to the file
    def save_movie_suggestion(movie_name, publish_year):

        with open("repositories/voting_suggestions.txt", "a") as file:
            file.write(movie_name + "," + publish_year + "\n")
        file.close()


    # Prints the current movie suggestions list
    def print_movie_suggestion_list():

        if len(Movie_Repository.list_of_movie_suggestions) == 0:
            print("Suggestion list is empty. \n")
        else:
            counter = 1
            print("The suggestions are: ")

            for movie in Movie_Repository.list_of_movie_suggestions:
                candidate_description = movie.movie_to_string()
                print(f"[{counter}]: {candidate_description}")
                counter += 1
            print("")


    def save_voting_list_to_file():
        # Save movies to voting_list.txt
        with open("voting_list.txt", "a") as file:
            for movie in Movie_Repository.list_of_movies_to_be_voted:
                file.write(movie.movie_name + "," + movie.publish_year)
                file.write("\n")
            file.close()

    # For admin: empty movie voting list
    def empty_voting_list():
        Movie_Repository.list_of_movies_to_be_voted.clear()
        empty_the_text_file = open("repositories/voting_list.txt", 'w')
        empty_the_text_file.close()
        return "Voting list is now empty.\n"

    # For admin: empty movie suggestion list
    def empty_suggestion_list():
        Movie_Repository.list_of_movie_suggestions.clear()
        empty_the_text_file = open("repositories/voting_suggestions.txt", 'w')
        empty_the_text_file.close()
        return "Suggestions list is now empty.\n"

    # For admin: empties the file that keep track of given votes
    def clear_all_votes():
        Movie_Repository.list_of_movie_suggestions.clear()
        empty_the_text_file = open("repositories/voting_suggestions.txt", 'w')
        empty_the_text_file.close()
        return "All votes wiped out.\n"

    # For admin: close voting
    def close_voting():
        with open("voting_status.txt", "w") as file:
            file.write("closed")
            file.write("\n")
        file.close()
