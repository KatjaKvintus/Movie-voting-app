class Movie():

    def __init__(self, movie_name: str, publish_year: int):
        self.movie_name = movie_name
        self.publish_year = publish_year
    
    def movie_to_string(movie):
        print(f"{movie.movie_name}, published in {movie.publish_year}")