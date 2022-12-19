import unittest
from entities.AppUser import AppUser


class TestAppUser(unittest.TestCase):


    def setUp(self):
        self.user_normal = AppUser("Maija", "Mehiläinen")


    def test_you_can_create_new_user(self):
        self.newUser = AppUser("Testaaja", "testi")
        self.assertEqual(self.newUser.username, "Testaaja")
    

    def test_existing_user_log_in_possible(self):
        self.existingUser = AppUser("testi1", "testi1")
        self.assertEqual(self.existingUser.username, "testi1")


    '''
    def test_too_short_password_will_be_declined(self):
        result = AppUser.check_username_length("!")
        self.assertEqual(result, "You chose too short username. It should be at least 3 characters long.")
    '''


