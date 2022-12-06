from tkinter import Tk, ttk, constants

class Loginpage:

    def __init__(self, root):
        self._root = root
    
    def start_application(self):

        # Create new user 
        heading_label1 = ttk.Label(master = self._root, text = "Create new user: ", font='Helvetica 14 bold')
        username_label1 = ttk.Label(master = self._root, text = "Choose username: ")
        username_entry1 = ttk.Entry(master = self._root)
        password_label1 = ttk.Label(master = self._root, text = "Choose Password: ")
        password_entry1 = ttk.Entry(master = self._root, show = "*")
        emptyrow = ttk.Label(master = self._root, text = "")
        create_account_button = ttk.Button(master = self._root, text = "Create account")

        heading_label1.grid(row = 0, column = 0, columnspan = 2)
        username_label1.grid(row = 1, column = 0)
        username_entry1.grid(row = 1, column = 1)
        password_label1.grid(row = 2, column = 0)
        password_entry1.grid(row = 2, column = 1)
        create_account_button.grid(row = 3, column = 0, columnspan = 2)
        emptyrow.grid(row = 4, column = 0)

        # Returning user login
        heading_label2 = ttk.Label(master = self._root, text = "Returning user login: ", font='Helvetica 14 bold')
        username_label2 = ttk.Label(master = self._root, text = "Username: ")
        username_entry2 = ttk.Entry(master = self._root)
        password_label2 = ttk.Label(master = self._root, text = "Password: ")
        password_entry2 = ttk.Entry(master = self._root, show = "*")
        login_button = ttk.Button(master = self._root, text = "Login")

        heading_label2.grid(row = 4, column = 0, columnspan = 2)
        username_label2.grid(row = 5, column = 0)
        username_entry2.grid(row = 5, column = 1)
        password_label2.grid(row = 6, column = 0)
        password_entry2.grid(row = 6, column = 1)
        login_button.grid(row = 7, column = 0, columnspan = 2)

        # Configuring layout
        heading_label1.grid(columnspan = 2, sticky = constants.W, padx = 10, pady = 10)
        username_label1.grid()
        username_entry1.grid(row = 1, column = 1, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        password_label1.grid()
        password_entry1.grid(row = 2, column = 1, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        create_account_button.grid(columnspan = 2, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        self._root.grid_columnconfigure(1, weight = 1, minsize = 400)

        heading_label2.grid(columnspan = 2, sticky = constants.W, padx = 10, pady = 10)
        username_label2.grid()
        username_entry2.grid(row = 5, column = 1, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        password_label2.grid()
        password_entry2.grid(row = 6, column = 1, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        login_button.grid(row = 7, column = 0, columnspan = 2, sticky = (constants.E, constants.W), padx = 10, pady = 10)
        self._root.grid_columnconfigure(1, weight = 1, minsize = 400)


#def handle_create_new_user_button_click(self):



window = Tk()
window.title("Movie voting app")
 
ui = Loginpage(window)
ui.start_application()

window.mainloop()
