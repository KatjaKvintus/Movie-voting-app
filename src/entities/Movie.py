


class Movie():

    list_of_movies_to_be_voted = []
    list_of_movie_suggestions = []
    


    def __init__(self, movie_name: str, publish_year: str):
        self.movie_name = movie_name
        self.publish_year = publish_year
        self.votes = 0


    # Movie basic functionalities for user
    def welcome_to_movieapp():

        voting_status = Movie.check_voting_status()

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

            if answer == "E" or answer == "e":
                print("Bye!")
                exit()
            elif answer == "S" or answer == "s":
                Movie.print_voting_list()
            elif answer == "V" or answer == "v":
                Movie.vote_for_movie()
            elif answer == "P" or "p":
                Movie.suggest_a_movie()
            else:
                print("Pelase choose from the list. ")



    def check_voting_status():

        current_voting_list_file_exists = False
        
        while not current_voting_list_file_exists:     

            #movieapp_voting_status = "entities/voting_status.txt"       PALAUTA ENNEN KUIN JULKAISET!!!!
            movieapp_voting_status = "/home/kvintus/ot-harjoitustyo/src/entities/voting_status.txt"

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



    ######################## This is for testing only
    def testing_add_movies():
        test_movie_1 = Movie("The Shawshank Redemption", "1994")
        Movie.list_of_movies_to_be_voted.append(test_movie_1)
        test_movie_2 = Movie("The Godfather", "1972")
        Movie.list_of_movies_to_be_voted.append(test_movie_2)
        test_movie_3 = Movie("The Dark Knight", "2008")
        Movie.list_of_movies_to_be_voted.append(test_movie_3 )
        test_movie_4 = Movie("The Godfather: Part II", "1974")
        Movie.list_of_movies_to_be_voted.append(test_movie_4 )


    def movie_to_string(movie):
        return(f"{movie.movie_name} (published in {movie.publish_year})")
    
    # KESKEN
    def vote_for_movie():

        print("")
        print("This weeks candidates: ")
        Movie.print_voting_list() 
        print("")

        vote = int(input("My vote (write number): "))
        Movie.list_of_movies_to_be_voted[vote - 1].votes += 1
        print("Thank you for voting! \n")


    def suggest_a_movie():

        print("You can suggest one movie for next weeks voting.")    
        print("App admin(s) will decide, if this movie is worthy. ")

        while True:
            movie_name = input("Please give movie name: ")

            if len(movie_name) < 1:
                print("Movie name is too short. Please give correct movie name. \n")
                continue
            else:
                break
        
        while True:
            publish_year = input("Please give movie publish year: ")

            if int(publish_year) < 1878:
                print("Please check the year.")
                print("As a true movie fan, you do must now that the first movie was published 1878.\n")
                continue
            else:
                break
        
        new_movie = Movie(movie_name, publish_year)
        Movie.list_of_movie_suggestions.append(new_movie)

        with open("voting_suggestions.txt", "a") as file:
            file.write(movie_name + "," + publish_year + "\n")
        file.close()   


    def print_voting_list():

        if len(Movie.list_of_movies_to_be_voted) == 0:
            print("Movie list is empty. \n")
        else:
            counter = 1
            print("The movie list for this weeks vote is: ")

            for movie in Movie.list_of_movies_to_be_voted:
                candidate_description = movie.movie_to_string() 
                print(f"[{counter}]: {candidate_description}")
                counter += 1
            print("")

    
    def print_movie_suggestion_list():

        if len(Movie.list_of_movie_suggestions) == 0:
            print("Suggestion list is empty. \n")
        else:
            counter = 1
            print("The suggestions are: ")

            for movie in Movie.list_of_movie_suggestions:
                candidate_description = movie.movie_to_string() 
                print(f"[{counter}]: {candidate_description}")
                counter += 1
            print("")


    # For admin: set up a list of 4 movies for next vote. Admin can add movies of their choice 
    # or pick max 4 suggestions from movie suggestion list.
    def admin_set_voting_list():

        max_amount_of_movies_to_be_added = 4
        setting_successfull = False

        if len(Movie.list_of_movies_to_be_voted) > 0:
            print("Empty the current list before creating new")
            choice = input("Do you want to empty old list? [Y]es or [N]o: ")

            if choice == "Y" or choice == "y":
                Movie.admin_empty_voting_list
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
                Movie.print_movie_suggestion_list()
                print()
                choice2 = print("If you want to add any of these, type the movie number. If not, press [X].\n")

                if len(Movie.print_movie_suggestion_list) <= choice2 > 0:
                    add_this_movie_to_be_voted = Movie.list_of_movie_suggestions[int(choice2) - 1]
                    Movie.list_of_movies_to_be_voted.append(add_this_movie_to_be_voted)
                    movies_added += 1
                elif choice2 == "X" or choice2 =="x":
                    break

        while movies_added < max_amount_of_movies_to_be_added:
            movie_name = input(f"Write movie no {movies_added + 1} name: ")
            publish_year = input("Publish year: ")
            print()
            new_movie = Movie(movie_name, publish_year)
            Movie.list_of_movies_to_be_voted.append(new_movie)
            movies_added += 1
        
        # Save movies to voting_list.txt
        with open("movieapp_users.txt", "a") as file:
            for movie in Movie.list_of_movies_to_be_voted:
                file.write(movie.movie_name + "," + movie.publish_year)
                file.write("\n")
            file.close()        
        
        setting_successfull = True
        print("\ņSetting movie list succesfull.\n")
        return setting_successfull
    

    # For admin: empty movie voting list
    def admin_empty_voting_list():
        Movie.list_of_movies_to_be_voted.clear()
        empty_the_text_file = open("entities/voting_list.txt", 'w')
        empty_the_text_file.close()
        print("Voting list is now empty.\n")
    
    # For admin: empty movie suggestion list
    def admin_empty_suggestion_list():
        Movie.list_of_movie_suggestions.clear()
        empty_the_text_file = open("entities/voting_suggestions.txt", 'w')
        empty_the_text_file.close()
        print("Suggestions list is now empty.\n")
        


