

class AdminUserRepository:


    def __init__(self, username, password):
        None

    # Dictionary to store all admin users: username as the key and password as the value
    admin_users = {}


    # Check if admin user list is available and if it is, download and save users to a dictionaries
    def check_and_download_userlist():

        admin_userlist_file_exists = False
    
        while not admin_userlist_file_exists:     

            #movieapp_admin_userlist = "repositories/movieapp_admin_users.txt"       # PALAUTA ENNEN KUIN JULKAISET!!!!
            movieapp_admin_userlist = "/home/kvintus/ot-harjoitustyo/src/repositories/movieapp_admin_users.txt"

            try:
                # Test if file exists
                with open(movieapp_admin_userlist) as testfile:
                    admin_userlist_file_exists = True
            
            except OSError:
                print("Error: admin userlist not found.")
                exit()
        
            # Read file and save admin users to all_users dictionary
            with open(movieapp_admin_userlist) as file:
                for line in file:
                    userdata = line.split(",")
                    username = str.strip(userdata[0])
                    password = str.strip(userdata[1])
                    AdminUserRepository.admin_users[username] = password
            
                file.close()
    
    # Read file and save new user to admin_users dictionary
    def save_new_admin_user_to_file(username, password):
            with open("movieapp_admin_users.txt", "a") as file:
                file.write(username + "," + password)
                file.write("\n")
                file.close()


        