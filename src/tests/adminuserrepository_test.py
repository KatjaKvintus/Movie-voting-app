import unittest
from repositories.AdminUserRepository import Admin_User_Repository


class TestAdminUserRepository(unittest.TestCase):


    def test_saving_new_admin_user_to_file_succesfull(self):
        result = Admin_User_Repository.save_new_admin_user_to_file("this_username", "this_password")
        self.assertTrue(result)
    
