

class UserRepository:

    #def __init__(self):
        #self._file_path = file_path
    

    # Save new users name ans password into file
    def save_new_user_in_database(self, user):

        try:
            save_location = "movieapp_users.txt"

            with open(save_location, "a") as userlistfile:
                new_user_name_and_password = user.username + "," + user.password + "\n"
                userlistfile.write(new_user_name_and_password)
                userlistfile.close()
        
        except IOError as exception:
            raise IOError("ERROR: saving not successful.")

       
    #def find_user(self, username):
