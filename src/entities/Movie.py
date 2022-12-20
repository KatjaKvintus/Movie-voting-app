from repositories.MovieRepository import MovieRepository
from services.MovieService import MovieService
import datetime

class Movie():

    
    def __init__(self, movie_name: str, publish_year: str):
        self.movie_name = movie_name
        self.publish_year = publish_year
        self.votes = 0


    # This is for testing only
    '''
    test_movie_1 = Movie("The Shawshank Redemption", "1994")
    MovieRepository.list_of_movies_to_be_voted.append(test_movie_1)
    test_movie_2 = Movie("The Godfather", "1972")
    MovieRepository.list_of_movies_to_be_voted.append(test_movie_2)
    test_movie_3 = Movie("The Dark Knight", "2008")
    MovieRepository.list_of_movies_to_be_voted.append(test_movie_3)
    test_movie_4 = Movie("The Godfather: Part II", "1974")
    MovieRepository.list_of_movies_to_be_voted.append(test_movie_4)
    '''


    # Movie basic functionalities for user
    def welcome_to_movieapp():

        voting_status = MovieRepository.check_voting_status()


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
                MovieService.print_voting_list()
            elif answer == "V" or answer == "v":
                MovieRepository.vote_for_movie()
            elif answer == "P" or "p":
                Movie.suggest_a_movie()
            else:
                print("Pelase choose from the list. ")

    def get_movie_name(movie):
        return movie.movie_name


    def movie_to_string(movie):
        return(f"{movie.movie_name} (published in {movie.publish_year})")
    

    

    
    def suggest_a_movie():

        print("You can suggest one movie for next weeks voting.")    
        print("App admin(s) will decide, if this movie is worthy.\n")

        while True:
            movie_name = input("Please give movie name: ")

            if len(movie_name) < 1:
                print("Movie name is too short. Please give correct movie name. \n")
                continue
            else:
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
            else:
                break
        
        new_movie = Movie(movie_name, publish_year)
        MovieRepository.list_of_movie_suggestions.append(new_movie)

        MovieRepository.save_movie_suggestion(movie_name, publish_year)

        print("Thank you for your suggestion!\n")


    
