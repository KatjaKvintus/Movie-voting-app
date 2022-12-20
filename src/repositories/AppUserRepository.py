

class AppUserRepository:

    #def __init__(self, username, password):
     #   None
    

    all_users = {}



    # Check if userlist is available and if it is, download and save users to a dictionary
    def check_and_download_userlist():

        userlist_file_exists = False
        
        while not userlist_file_exists:     

            #movieapp_userlist = "repositories/movieapp_users.txt"       PALAUTA ENNEN KUIN JULKAISET!!!!
            movieapp_userlist = "/home/kvintus/ot-harjoitustyo/src/repositories/movieapp_users.txt"

            try:
                # Test if file exists
                with open(movieapp_userlist) as testfile:
                    userlist_file_exists = True
            
            except OSError:
                print("Error: userlist not found.")
                exit()

        # Read file and save users to all_users dictionary
        with open(movieapp_userlist) as file:
            for line in file:
                userdata = line.split(",")
                username = str.strip(userdata[0])
                password = str.strip(userdata[1])

                AppUserRepository.all_users[username] = password
        
            file.close()
    

    def save_new_user_to_file(username, password): 
        with open("movieapp_users.txt", "a") as file:
            file.write(username + "," + password)
            file.write("\n")
            file.close()

