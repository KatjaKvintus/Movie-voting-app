import unittest
from User import User


class TestUi(unittest.TestCase):

    def test_you_can_create_new_user(self):
        self.newUser = User("Testaaja", "testi")
        self.assertEqual(self.newUser.username, "Testaaja")
