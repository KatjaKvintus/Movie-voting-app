

class App_User_Repository:

    #def __init__(self, username, password):
     #   None


    all_users = {}



    # Check if userlist is available and if it is, download and save users to a dictionary
    def check_and_download_userlist():

        userlist_file_exists = False

        #movieapp_userlist = "repositories/movieapp_users.txt"       PALAUTA ENNEN KUIN JULKAISET!!!!
        movieapp_userlist = "/home/kvintus/ot-harjoitustyo/src/repositories/movieapp_users.txt"

        while not userlist_file_exists:
            if App_User_Repository.check_if_file_exists(movieapp_userlist):
                break


        # Read file and save users to all_users dictionary
        with open(movieapp_userlist) as file:
            for line in file:
                userdata = line.split(",")
                username = str.strip(userdata[0])
                password = str.strip(userdata[1])

                App_User_Repository.all_users[username] = password

            file.close()
            return True


    def save_new_user_to_file(self, username, password):
        with open("movieapp_users.txt", "a") as file:
            file.write(username + "," + password)
            file.write("\n")
            file.close()


    def check_if_file_exists(self, file_path):

        file_exists = False

        while not file_exists:
            try:
                with open(file_path) as testfile:
                    file_exists = True

            except OSError:
                print("Error: file not found.")

        return file_exists
