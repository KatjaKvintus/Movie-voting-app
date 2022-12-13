import unittest
from entities.AppUser import AppUser


class TestUi(unittest.TestCase):

    def test_you_can_create_new_user(self):
        self.newUser = AppUser("Testaaja", "testi")
        self.assertEqual(self.newUser.username, "Testaaja")

    #def test