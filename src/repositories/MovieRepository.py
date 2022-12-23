import sys



class Movie_Repository:

    list_of_movies_to_be_voted = []
    list_of_movie_suggestions = []


    def check_voting_status():
        """ Returns "open" or "closed" depending on if the voting is open or not, or 
        a status message is a winner movie has been set.
        """

        current_voting_list_file_exists = False

        while not current_voting_list_file_exists:

            movieapp_voting_status = "repositories/voting_status.txt" 

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


    def save_movie_vote(movie_name):
        """The vote, given by user, is saved to a file.
        """
        with open("repositories/votes.txt", "a") as file:
            file.write(movie_name + "\n")
        file.close()


    def save_movie_suggestion(movie_name, publish_year):
        """Saves movie suggestion to the file
        """
        with open("repositories/voting_suggestions.txt", "a") as file:
            file.write(movie_name + "," + publish_year + "\n")
        file.close()


    def save_voting_list_to_file(movie_list_as_text):
        """Save movies (list set by admin user) to voting_list.txt
        """

        individual_movies = movie_list_as_text.split(";")

        with open("repositories/voting_list.txt", "a") as file:
            for item in individual_movies:
                file.write(item)
                file.write("\n")
        
        file.close()


    def empty_voting_list():
        """For admin: empty movie voting list
        """
        Movie_Repository.list_of_movies_to_be_voted.clear()
        open("repositories/voting_list.txt", 'w').close()
        print ("Voting list is now empty.\n")


    def empty_suggestion_list():
        """For admin: empty movie suggestion list
        """
        Movie_Repository.list_of_movie_suggestions.clear()
        open("repositories/voting_suggestions.txt", 'w').close()
        print ("Suggestions list is now empty.\n")


    def clear_all_votes():
        """For admin: empties the file that keep track of given votes
        """
        open("repositories/voting_suggestions.txt", 'w').close()
        print("All votes wiped out.\n")


    def close_voting():
        """For admin: close voting
        """
        with open("voting_status.txt", "w") as file:
            file.write("closed")
            file.write("\n")
        file.close()
        print("Voting is now closed.")


    def set_voting_status_message_as_winner_movie(movie_name):
        """For admin: set voting status message when winning movie is known
        """
        with open("repositories/voting_status.txt", "w") as file:
            file.write(f"The voting has ended. Next movie night movie is '{movie_name}'! ")
            file.write("\n")
        file.close()
