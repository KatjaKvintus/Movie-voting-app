from tkinter import Tk, ttk, constants

class Mainpage:

    def __init__(self, root):
        self._root = root
    

    def show_mainpage(self):

        # Voting list
        voting_status_label = ttk.Label(master = self._root, text = "Voting is open!", font = 'Helvetica 14 bold')
        voting_status_label.grid(columnspan = 2, sticky = constants.W)

        # List of movies you can vote
        movie1_label = ttk.Label(master = self._root, text = "Really good movie 1")
        movie2_label = ttk.Label(master = self._root, text = "Really good movie 2")
        movie3_label = ttk.Label(master = self._root, text = "Really good movie 3")
        movie4_label = ttk.Label(master = self._root, text = "Really good movie 4")

        movie1_label.grid(row = 1, column = 0)
        movie2_label.grid(row = 2, column = 0)
        movie3_label.grid(row = 3, column = 0)
        movie4_label.grid(row = 4, column = 0)

        # Voting buttons
        vote_movie1_button = ttk.Button(master = self._root, text = "Vote this movie")
        vote_movie2_button = ttk.Button(master = self._root, text = "Vote this movie")
        vote_movie3_button = ttk.Button(master = self._root, text = "Vote this movie")
        vote_movie4_button = ttk.Button(master = self._root, text = "Vote this movie")

        vote_movie1_button.grid(row = 1, column = 1, columnspan = 2, padx = 15, pady = 15)
        vote_movie2_button.grid(row = 2, column = 1, columnspan = 2, padx = 15, pady = 15)
        vote_movie3_button.grid(row = 3, column = 1, columnspan = 2, padx = 15, pady = 15)
        vote_movie4_button.grid(row = 4, column = 1, columnspan = 2, padx = 15, pady = 15)

        # Suggest a movie
        suggest_movie_heading = ttk.Label(master = self._root, text = "Suggest a movie for next movie night", font = 'Helvetica 14 bold')
        suggest_movie_heading.grid(columnspan = 2, sticky = constants.W)
        movie_entry = ttk.Entry(master = self._root)
        movie_entry.grid(row = 6, column = 1)
        suggest_movie_label = ttk.Label(master = self._root, text = "My suggestion: ")
        suggest_movie_label.grid(row = 6, column = 0)     


window = Tk()
window.title("Movie voting app")
 
ui = Mainpage(window)
ui.show_mainpage()

window.mainloop()
