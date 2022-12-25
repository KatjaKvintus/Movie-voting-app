import unittest
from repositories.App_User_Repository import App_User_Repository


class Test_App_User_Repository(unittest.TestCase):

    def test_userlist_download_succesfull(self):
        result = App_User_Repository.check_and_download_userlist()
        self.assertTrue(result)
    
    def test_existing_file_path_returns_True(self):
        result = App_User_Repository.check_if_file_exists("src/repositories/movieapp_users.txt")
        self.assertTrue(result)

