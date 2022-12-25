# Sovelluksen funktiot eri luokissa

### index.py:
- start()
- main()

### App_User:
create_new_user():
log_in_returning_user()
check_if_username_is_available(username)
check_username_length(username)
check_password_lenght(password)

### Admin_User:
create_new_admin_user()
admin_log_in()
admin_tools()
check_if_username_is_available(username)
check_username_length(username)
check_password_lenght(password)

### App_User_Repository:
check_and_download_userlist()
save_new_user_to_file(username, password)
check_if_file_exists(file_path)

### Admin_User_Repository:
check_and_download_admin_userlist()
save_new_admin_user_to_file(self,username, password)

### Movie:
download_movie_voting_list()
download_movie_suggestions_list()
welcome_to_movieapp()
get_movie_name(movie)
get_publish_year(movie)
movie_to_string(movie)
vote_for_movie(movie)
suggest_a_movie()
set_voting_list()
suggest_movie_suggestions(suggestions_amount)
print_voting_list_for_admin()
print_movie_suggestion_list()

### Movie_Repository:
check_voting_status()
save_movie_vote()
save_movies_suggestion(movie_name, publish_year)
save_voting_list_to_file()
empty_voting_list()
empty_suggestion_list()
clear_all_votes()
close_voting()
open_voting()
set_voting_status_message_as_winner_movie(movie_name)

### Movie_Service:
count_votes()
print_voting_list()
print_voting_list_for_admin()
