import sys



class Movie_Repository:

    list_of_movies_to_be_voted = []
    list_of_movie_suggestions = []


    # Returns "open" or "closed" depending on if the voting is open or not, or ""
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

        with open(movieapp_voting_status) as file:
            for row in file:
                status_now = row
            file.close()

        return status_now


    # The vote, given by user, is saved to a file.
    def save_movie_vote(movie_name):

        with open("repositories/votes.txt", "a") as file:
            file.write(movie_name + "\n")
        file.close()


    # Saves movie suggestion to the file
    def save_movie_suggestion(movie_name, publish_year):

        with open("repositories/voting_suggestions.txt", "a") as file:
            file.write(movie_name + "," + publish_year + "\n")
        file.close()



    def save_voting_list_to_file(movie_list_as_text):
        # Save movies to voting_list.txt

        individual_movies = movie_list_as_text.split(";")

        with open("repositories/voting_list.txt", "a") as file:
            for item in individual_movies:
                file.write(item)
                file.write("\n")
        
        file.close()


    # For admin: empty movie voting list
    def empty_voting_list():
        Movie_Repository.list_of_movies_to_be_voted.clear()
        open("repositories/voting_list.txt", 'w').close()
        print ("Voting list is now empty.\n")

    # For admin: empty movie suggestion list
    def empty_suggestion_list():
        Movie_Repository.list_of_movie_suggestions.clear()
        open("repositories/voting_suggestions.txt", 'w').close()
        print ("Suggestions list is now empty.\n")

    # For admin: empties the file that keep track of given votes
    def clear_all_votes():
        open("repositories/voting_suggestions.txt", 'w').close()
        print("All votes wiped out.\n")

    # For admin: close voting
    def close_voting():
        with open("voting_status.txt", "w") as file:
            file.write("closed")
            file.write("\n")
        file.close()
    
    # For admin: set voting status message when winning movie is known
    def set_voting_status_message_as_winner_movie(movie_name):
        with open("voting_status.txt", "w") as file:
            file.write(f"The voting has ended! Next movie nigh movie is {movie_name")
            file.write("\n")
        file.close()
