import requests
from json import dumps
import cPickle as pickle

session = requests.Session()
server_endpoint = 'http://127.0.0.1:5000/'

# On launch the client:
    # 1. Gets user data from the user.p file (local operation)
        # a. If no user account is present, make a user account (POST)
    # 2. Contacts Star Conflict server and gets game data (GET)
    # 3. Allows user to enter a game or start a new one (local operation/POST)
    # 4. Allows users to leave the app (local operation).

# In a game users can:
    # 0. See the current game state (GET)
    # 1. Leave the game (local operation)
    # 2. If it is their turn:
        # a. Take an action (POST)
        # b. End turn (POST)

def start_new_game(g):
    pass
def load_user_data():
    return pickle.load(open("user.p", "rb" ))
def make_new_user():
    # get username
    username = raw_input("Enter user name: ") 
    # contact server with new user request
    response = session.post(
            server_endpoint+'/users/',
            data=dumps({'username': username})
        )
    pickle.dump(response.content, open("user.p", "wb"))
    return response.content

if __name__ == '__main__':
    # Load user data
    try:
        g = load_user_data()
    # If no user data, make a new user
    except:
        g = make_new_user()
   
    # Get user game data
    try:
        g['games'] = get_game_data(g)


    # On launch the client:
    # 1. Gets user data from the ._user file (local operation)
        # a. If no user account is present, make a user account (POST)
    # 2. Contacts Star Conflict server and gets game data (GET)
    # 3. Allows user to enter a game or start a new one (local operation/POST)
    # 4. Allows users to leave the app (local operation).





