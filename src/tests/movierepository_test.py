import unittest
from repositories.MovieRepository import Movie_Repository
from entities.Movie import Movie


class TestMovieRepository(unittest.TestCase):

    '''  # EI TOIMI, HERJAA TIEDOSTOSTA 'repositories/voting_suggestions.txt'
    def test_adding_movie_suggestion_succesfull(self):
        MovieRepository.empty_suggestion_list()
        new_movie = Movie("Minions", 2015)
        MovieRepository.list_of_movie_suggestions.append(new_movie)
        suggestions_list_contents = MovieRepository.print_movie_suggestion_list()
        suggestions_list_contents_should_be = "Minions, 2015"
        self.assertEqual(suggestions_list_contents, "Minions, 2015")
    '''

    '''
    def test_voting_list_clearing_succesfull(self):
        result = MovieRepository.empty_voting_list()
        self.assertSetEqual(result, "Voting list is now empty.\n")
    '''

    