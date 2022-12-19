import unittest
from entities.Movie import Movie


class TestMovie(unittest.TestCase):


    def test_movie_to_string_works_correctly(self):
        self.newMovie = Movie("Titanic", 1997)
        result = Movie.movie_to_string(Movie.newMovie)
        self.assertEqual(result, "Titanic, published in 1997")