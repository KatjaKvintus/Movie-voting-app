
class UserRepository:

    def __init__(self, save_location):
        self._save_location = save_location
    

    # Save new users name ans password into file
    def save_new_user_in_database(self, that_new_user):

        try:
            save_location = "movieapp_users.txt"

            with open(save_location, "a") as userlistfile:
                new_user_name_and_password = that_new_user.username + "," + that_new_user.password + "\n"
                userlistfile.write(new_user_name_and_password)
                userlistfile.close()
        
        except IOError as exception:
            raise IOError("ERROR: saving not successful.")

       
    #def find_user(self, username):
