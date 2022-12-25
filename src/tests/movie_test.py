import unittest
from entities.Movie import Movie


class Test_Movie(unittest.TestCase):


    def test_movie_to_string_works_correctly(self):
        newMovie = Movie("Titanic", 1997)
        result = Movie.movie_to_string(newMovie)
        self.assertEqual(result, "Titanic (published in 1997)")
    
    def test_movie_name_retuned_correctly(self):
        newMovie = Movie("Titanic", 1997)
        result = Movie.get_movie_name(newMovie)
        self.assertEqual(result, "Titanic")