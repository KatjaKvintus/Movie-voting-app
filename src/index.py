from ui import Ui
from ui import User


def main():


    User.load_users(Ui.all_users)
    Ui.startpage()


if __name__ == "__main__":
    main()
