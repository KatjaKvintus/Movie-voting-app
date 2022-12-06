from tkinter import Tk, ttk, constants
from entities import User
from ui import *
#import Mainpage            # TÄMÄ AVAA APIN SUORAAN PÄÄSIVULLE

class Loginpage:

    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()
        self._current_view = None
        self.new_user_username_entry = None
        self.new_user_password_entry = None

    def pack(self):
        self._frame.pack(fill = constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text = "Close application")        
        button = ttk.Button(master=self._frame, text = "Close application")

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
    

    def start_application(self):

        self._current_view = Loginpage (self._root)

        # Create new user 
        new_user_heading_label = ttk.Label(master = self._root, text = "Create new user: ", font='Helvetica 14 bold')
        new_user_username_label = ttk.Label(master = self._root, text = "Choose username: ")
        self.new_user_username_entry = ttk.Entry(master = self._root)
        new_user_password_label = ttk.Label(master = self._root, text = "Choose Password: ")
        self.new_user_password_entry = ttk.Entry(master = self._root, show = "*")
        emptyrow = ttk.Label(master = self._root, text = " ")
        
        create_new_account_button = ttk.Button(master = self._root, text = "Create account", command=self.handle_create_new_user_button_click)
        #handle_create_new_user_button_click()

        new_user_heading_label.grid(row = 0, column = 0, columnspan = 2)
        new_user_username_label.grid(row = 1, column = 0)
        self.new_user_username_entry.grid(row = 1, column = 1)
        new_user_password_label.grid(row = 2, column = 0)
        create_new_account_button.grid(row = 3, column = 0, columnspan = 2)
        self.new_user_password_entry.grid(row = 2, column = 1)

        emptyrow.grid(row = 4, column = 0)        
        
        # Returning user login
        returning_user_heading_label = ttk.Label(master = self._root, text = "Returning user login: ", font='Helvetica 14 bold')

        returning_user_username_label = ttk.Label(master = self._root, text = "Username: ")
        returning_user_username_entry = ttk.Entry(master = self._root)
        returning_user_password_label = ttk.Label(master = self._root, text = "Password: ")
        returning_user_login_button = ttk.Button(master = self._root, text = "Login")
        returning_user_password_entry = ttk.Entry(master = self._root, show = "*")

        returning_user_heading_label.grid(row = 4, column = 0, columnspan = 2)
        returning_user_username_label.grid(row = 5, column = 0)
        returning_user_username_entry.grid(row = 5, column = 1)
        returning_user_password_label.grid(row = 6, column = 0)
        returning_user_password_entry.grid(row = 6, column = 1)
        returning_user_login_button.grid(row = 7, column = 0, columnspan = 2)

        # Configuring layout
        new_user_heading_label.grid(columnspan = 2, sticky = constants.W, padx = 10, pady = 10)
        new_user_username_label.grid()
        self.new_user_username_entry.grid(row = 1, column = 1, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        new_user_password_label.grid()
        self.new_user_password_entry.grid(row = 2, column = 1, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        create_new_account_button.grid(columnspan = 2, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        self._root.grid_columnconfigure(1, weight = 1, minsize = 400)

        returning_user_heading_label.grid(columnspan = 2, sticky = constants.W, padx = 10, pady = 10)
        returning_user_username_label.grid()
        returning_user_username_entry.grid(row = 5, column = 1, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        returning_user_password_label.grid()
        returning_user_password_entry.grid(row = 6, column = 1, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        returning_user_login_button.grid(row = 7, column = 0, columnspan = 2, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        self._root.grid_columnconfigure(1, weight = 1, minsize = 400)


    def handle_create_new_user_button_click(self):
        name = self.new_user_username_entry.get()
        password = self.new_user_password_entry.get()
        User.create_new_user(name, password)
        Loginpage.show_mainpage()
        

    def open_mainpage_view():
        Loginpage.show_mainpage()



#window = Tk()
#window.title("Movie voting app")
# 
#ui = Loginpage(window)
#ui.start_application()
#
#window.mainloop()
