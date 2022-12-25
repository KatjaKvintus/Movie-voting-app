import unittest
from entities.AdminUser import Admin_user


class TestAdminUser(unittest.TestCase):


    def test_you_can_create_new_admin_user(self):
        self.newUser = Admin_user("Testaaja", "testi")
        self.assertEqual(self.newUser.username, "Testaaja")
    
    def test_existing_admin_user_log_in_possible(self):
        self.existingUser = Admin_user("thisisadmin", "adminpassword")
        self.assertEqual(self.existingUser.username, "thisisadmin")

    def test_long_enough_admin_password_will_be_accepted(self):
        result = Admin_user.check_password_lenght("thisisreallylongpassword")
        self.assertAlmostEqual(result, "thisisreallylongpassword")
    
    def test_admin_password_with_special_characters_will_be_accepted(self):
        result = Admin_user.check_password_lenght("passwordwith#%&()()()()!")
        self.assertAlmostEqual(result, "passwordwith#%&()()()()!")