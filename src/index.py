from Ui import Ui
from User import User
from Loginpage import Loginpage


def main():

    User.load_users(User.all_users)
    Loginpage.start_application()


if __name__ == "__main__":
    main()
