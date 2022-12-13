class Movie():

    list_of_movies_to_be_voted = []

    

    def __init__(self, movie_name: str, publish_year: int):
        self.movie_name = movie_name
        self.publish_year = publish_year
        self.votes = 0
    
    def movie_to_string(movie):
        print(f"{movie.movie_name} (published in {movie.publish_year})")
    

    # KESKEN
    def vote_for_movie():

        print("")
        print("This weeks candidates: ")
        Movie.print_voting_list() 
        print("")

        vote = int(input("My vote (write number): "))

        Movie.list_of_movies_to_be_voted[vote - 1].votes += 1

        print("Thank you for voting! \n")
        
    

    # NOT WORKING PROPERLY
    def print_voting_list():

        if len(Movie.list_of_movies_to_be_voted) == 0:
            print("Movie list is empty. \n")
        else:
            counter = 1

            for movie in Movie.list_of_movies_to_be_voted:
                cadidate_description = movie.movie_to_string() 
                print(f"[{counter}]: {cadidate_description}")
                counter += 1
            print("")
    

    # For admin: set up a list of 4 movies for next vote
    def admin_set_voting_list():

        setting_successfull = False

        if len(Movie.list_of_movies_to_be_voted) > 0:
            print("Empty list before creating new")
            choice = input("Do you want to empty old list? [Y]es or [N]o: ")

            if choice == "Y" or choice == "y":
                Movie.admin_empty_voting_list
            elif choice == "N" or choice == "n":
                print("Can't add any more movies right now.")
                return setting_successfull

        movies_added = 0

        while movies_added < 4:

            movie_name = input(f"Write movie no {movies_added + 1} name: ")
            publish_year = input("Publish year: \n")

            new_movie = Movie(movie_name, publish_year)
            Movie.list_of_movies_to_be_voted.append(new_movie)
            
            movies_added += 1
        
        setting_successfull = True

        # TO BE ADDED: saving movies into a txt file

        return setting_successfull
    
    # For admin: empty movie list
    def admin_empty_voting_list():
        Movie.list_of_movies_to_be_voted.clear()
        print("List is now empty.\n")
        
        
    

