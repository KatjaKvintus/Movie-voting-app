import unittest
from entities.AdminUser import AdminUser



class TestAppUser(unittest.TestCase):


    def test_you_can_create_new_admin_user(self):
        self.newUser = AdminUser("Testaaja", "testi")
        self.assertEqual(self.newUser.username, "Testaaja")
