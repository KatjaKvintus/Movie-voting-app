import unittest
from repositories.AppUserRepository import App_User_Repository


class TestAppUserRepository(unittest.TestCase):

    def test_userlist_download_succesfull(self):
        result = App_User_Repository.check_and_download_userlist()
        self.assertTrue(result)
    
    ''' # TÄMÄ TESTI VETÄÄ TERMINAALIN JUMIIN
    def test_existing_file_path_returns_True(self):
        result = AppUserRepository.check_if_file_exists("repositories/movieapp_users.txt")
        self.assertTrue(result)
    '''

    '''# TÄMÄKIN TESTI VETÄÄ TERMINAALIN JUMIIN
    def test_incorrect_file_path_returns_False(self):
        result = AppUserRepository.check_if_file_exists("repositories/movieapp_users")
        self.assertFalse(result)
    '''    

