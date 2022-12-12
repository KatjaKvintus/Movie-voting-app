#from entities import *
from ui import Loginpage
#from repositories import UserRepository
from tkinter import *

def main():

    window = Tk()
    window.title("Movie voting app")
     
    ui = Loginpage.Loginpage(window)
    ui.start_application()
    
    window.mainloop()

    #User.load_users(User.all_users)
    #user_repository = UserRepository()
    Loginpage.start_application()


if __name__ == "__main__":
    main()
