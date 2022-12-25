import unittest
from repositories.Movie_Repository import Movie_Repository
from entities.Movie import Movie


class Test_Movie_Repository(unittest.TestCase):


    def test_adding_movie_suggestion_succesfull(self):
        Movie_Repository.empty_suggestion_list()
        new_movie = Movie("Minions", 2015)
        Movie_Repository.list_of_movie_suggestions.append(new_movie)
        suggestions_list_contents = Movie.print_movie_suggestion_list()
        suggestions_list_contents_should_be = "Minions, 2015"
        self.assertEqual(suggestions_list_contents_should_be, "Minions, 2015")

    def test_voting_list_clearing_succesfull(self):
        result = Movie_Repository.empty_voting_list()
        self.assertEqual(result, "Voting list is now empty.\n")

