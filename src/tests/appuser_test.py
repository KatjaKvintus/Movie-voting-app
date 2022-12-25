import unittest
from entities.App_User import App_User


class Test_App_User(unittest.TestCase):


    def setUp(self):
        self.user_normal = App_User("Maija", "Mehiläinen")

    def test_you_can_create_new_user(self):
        self.newUser = App_User("Testaaja", "testi")
        self.assertEqual(self.newUser.username, "Testaaja")
    
    def test_existing_user_log_in_possible(self):
        self.existingUser = App_User("testi1", "testi1")
        self.assertEqual(self.existingUser.username, "testi1")

    def test_long_enough_password_will_be_accepted(self):
        result = App_User.check_password_lenght("thisisreallylongpassword")
        self.assertAlmostEqual(result, "thisisreallylongpassword")
    
    def test_password_with_special_characters_will_be_accepted(self):
        result = App_User.check_password_lenght("passwordwith#%&()()()()!")
        self.assertAlmostEqual(result, "passwordwith#%&()()()()!")



