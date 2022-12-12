from repositories.UserRepository import UserRepository


class AppUser:

    # The class constructor for creating new users
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Keeps track of all usernames in use
    usernames = []

    # Keeps track of users
    all_users = []


    def create_new_user(self, username_new: str, password_new: str):
        new_user = AppUser(username_new, password_new)
        UserRepository.save_new_user_in_database(new_user)

    def username(self, username: str):
        return username

    