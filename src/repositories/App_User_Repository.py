

class App_User_Repository:

    #def __init__(self, username, password):
     #   None

    all_users = {}


    def check_and_download_userlist():
        """Check if userlist is available and if it is, downloads and save users to a dictionary.
        """

        userlist_file_exists = False

        movieapp_userlist = "src/repositories/movieapp_users.txt"

        while not userlist_file_exists:
            if App_User_Repository.check_if_file_exists(movieapp_userlist):
                break


        # Read file and save users to all_users dictionary
        with open(movieapp_userlist, encoding="utf-8") as file:
            for line in file:
                userdata = line.split(",")
                username = str.strip(userdata[0])
                password = str.strip(userdata[1])

                App_User_Repository.all_users[username] = password

            file.close()
            return True


    def save_new_user_to_file(username, password):
        """Saves new user account details to a file
        """
        with open("src/repositories/movieapp_users.txt", "a", encoding="utf-8") as file:
            file.write(username + "," + password)
            file.write("\n")
            file.close()


    def check_if_file_exists(file_path):
        """Verification function to check if file path is correct
        """

        file_exists = False

        while not file_exists:
            try:
                with open(file_path) as testfile:
                    file_exists = True

            except OSError:
                print("Error: THIS file not found.")

        return file_exists
