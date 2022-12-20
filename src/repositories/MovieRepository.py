#from entities.Movie import Movie


class MovieRepository:

    list_of_movies_to_be_voted = []
    list_of_movie_suggestions = []


    # Downloads from a file the voting list (that keeps track of given votes during )
    def download_movie_lists():

        current_voting_list_file_exists = False
        
        while not current_voting_list_file_exists:     

            #movieapp_voting_list = "repositories/voting_list.txt"       PALAUTA ENNEN KUIN JULKAISET!!!!
            movieapp_voting_list = "/home/kvintus/ot-harjoitustyo/src/repositories/voting_list.txt"

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
                MovieRepository.list_of_movies_to_be_voted.append(movie)
        
            file.close()
    

    # Return "open" or "closed" depending on if the voting is open or not
    def check_voting_status():

        current_voting_list_file_exists = False
        
        while not current_voting_list_file_exists:     

            #movieapp_voting_status = "repositories/voting_status.txt"       PALAUTA ENNEN KUIN JULKAISET!!!!
            movieapp_voting_status = "/home/kvintus/ot-harjoitustyo/src/repositories/voting_status.txt"

            try:
                # Test if file exists
                with open(movieapp_voting_status) as testfile:
                    current_voting_list_file_exists = True
            
            except OSError:
                print("Error: voting status not found.")
                exit()

        # Read file and save movies list_of_movies_to_be_voted list
        with open(movieapp_voting_status) as file:
            for row in file:
                status_now = row
        
            file.close()

        return status_now
    


    # User can vote for a movie by giving number 1-4. The vote is saved to a file.
    def vote_for_movie():

        print("")
        print("This weeks candidates: ")
        MovieRepository.print_voting_list() 
        print("")

        while True:
            vote = input("My vote (write number): ")

            if int(vote).isnumeric and int(vote) >= 1 and int(vote) <= 4:
                the_movie = MovieRepository.list_of_movies_to_be_voted[vote - 1].get_movie_name()
            
                with open("repositories/votes.txt", "a") as file:
                    file.write(the_movie + "\n")
                file.close() 

                print("Thank you for voting! \n")
                break
        
            else:
                print("Please answer by giving number 1, 2, 3 or 4. ")
                continue



    # Saves movie suggestion to the file
    def save_movies_suggestion(movie_name, publish_year):

        with open("repositories/voting_suggestions.txt", "a") as file:
            file.write(movie_name + "," + publish_year + "\n")
        file.close()   
      

    # Prints the current movie suggestions list
    def print_movie_suggestion_list():

        if len(MovieRepository.list_of_movie_suggestions) == 0:
            print("Suggestion list is empty. \n")
        else:
            counter = 1
            print("The suggestions are: ")

            for movie in MovieRepository.list_of_movie_suggestions:
                candidate_description = movie.movie_to_string() 
                print(f"[{counter}]: {candidate_description}")
                counter += 1
            print("")


    # For admin: set up a list of 4 movies for next vote. Admin can add movies of their choice 
    # or pick max 4 suggestions from movie suggestion list.
    def admin_set_voting_list():

        max_amount_of_movies_to_be_added = 4
        setting_successfull = False

        if len(MovieRepository.list_of_movies_to_be_voted) > 0:
            print("Empty the current list before creating new")
            choice = input("Do you want to empty old list? [Y]es or [N]o: ")

            if choice == "Y" or choice == "y":
                MovieRepository.empty_voting_list
            elif choice == "N" or choice == "n":
                print("Can't add any more movies right now.")
                return setting_successfull

        movies_added = 0

        print("Would you like to add something from the suggestions list?\n")
        choice1 = input("Choose below: ")
        print("  [Y]es, show me the list")
        print("  [N]o \n")

        while True:
            if choice1 == "Y" or choice1 == "y":
                MovieRepository.print_movie_suggestion_list()
                print()
                choice2 = print("If you want to add any of these, type the movie number. If not, press [X].\n")

                if len(MovieRepository.print_movie_suggestion_list) <= choice2 > 0:
                    add_this_movie_to_be_voted = MovieRepository.list_of_movie_suggestions[int(choice2) - 1]
                    MovieRepository.list_of_movies_to_be_voted.append(add_this_movie_to_be_voted)
                    movies_added += 1
                elif choice2 == "X" or choice2 =="x":
                    break

        while movies_added < max_amount_of_movies_to_be_added:
            movie_name = input(f"Write movie no {movies_added + 1} name: ")
            publish_year = input("Publish year: ")
            print()
            new_movie = Movie(movie_name, publish_year)
            MovieRepository.list_of_movies_to_be_voted.append(new_movie)
            movies_added += 1
        
        # Save movies to voting_list.txt
        with open("voting_list.txt", "a") as file:
            for movie in MovieRepository.list_of_movies_to_be_voted:
                file.write(movie.movie_name + "," + movie.publish_year)
                file.write("\n")
            file.close()        
        
        setting_successfull = True
        print("\ņSetting movie list succesfull.\n")
        return setting_successfull
    

    # For admin: empty movie voting list
    def empty_voting_list():
        MovieRepository.list_of_movies_to_be_voted.clear()
        empty_the_text_file = open("repositories/voting_list.txt", 'w')
        empty_the_text_file.close()
        print("Voting list is now empty.\n")
    

    # For admin: empty movie suggestion list
    def empty_suggestion_list():
        MovieRepository.list_of_movie_suggestions.clear()
        empty_the_text_file = open("repositories/voting_suggestions.txt", 'w')
        empty_the_text_file.close()
        print("Suggestions list is now empty.\n")
    
    # For admin: empties the file that keep track of given votes
    def clear_all_votes():
        MovieRepository.list_of_movie_suggestions.clear()
        empty_the_text_file = open("repositories/voting_suggestions.txt", 'w')
        empty_the_text_file.close()
        print("All votes wiped out.\n")


    


    # For admin: close voting
    def close_voting():

        with open("voting_status.txt", "w") as file:
            for movie in Movie.list_of_movies_to_be_voted:
                file.write("closed")
                file.write("\n")
            file.close() 
        

