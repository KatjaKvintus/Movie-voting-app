from repositories.MovieRepository import MovieRepository


class MovieService:


    # Reads votes.txt file, counts votes for each movie, empties the file and return the name of the winning movie.
    def count_votes():

        final_votes = {}

        with open("voting_status.txt") as file:
            for row in file:
                if row not in final_votes:
                    final_votes[row] = 1
                final_votes[row] = final_votes[row] +1
            file.close() 
        
        most_votes = 0
        movie_with_most_votes = ""

        for movie in final_votes:
            if final_votes[movie] > most_votes:
                most_votes = final_votes[movie]
                movie_with_most_votes = movie
        
        result = movie_with_most_votes

        MovieRepository.clear_all_votes()
        MovieRepository.empty_voting_list()
        MovieRepository.clear_all_votes()

        return result
    

    def print_voting_list():

        if len(MovieRepository.list_of_movies_to_be_voted) == 0:
            print("Unfortunatelyt the movie list is empty. Come back again later to check it again.\n")
        else:
            counter = 1
            print("The movie list for this weeks vote is: ")

            for movie in MovieRepository.list_of_movies_to_be_voted:
                candidate_description = movie.movie_to_string() 
                print(f"[{counter}]: {candidate_description}")
                counter += 1
            print("")