import unittest
from repositories.Admin_User_Repository import Admin_User_Repository


class Test_Admin_User_Repository(unittest.TestCase):


    def test_saving_new_admin_user_to_file_succesfull(self):
        result = Admin_User_Repository.save_new_admin_user_to_file("this_username", "this_password")
        self.assertTrue(result)
    
    def test_admin_user_list_available(self):
        result = Admin_User_Repository.check_and_download_admin_userlist()
        self.assertNotEqual(result, "Error: admin userlist not found.")