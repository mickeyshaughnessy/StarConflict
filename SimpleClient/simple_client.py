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

def load_user():
    return pickle.load(open("user.p", "rb"))

def make_new_user(username=None):
    if not username:
        username = raw_input("Enter user name to make: ") 
    response = session.post(server_endpoint+'users/'+username,)
    pickle.dump(response.content, open("user.p", "wb"))
    return response.content

def get_user_data(username=None):
    if not username:
        username = raw_input("Enter user name to get: ") 
    response = session.get(server_endpoint+'users/'+username)
    return response.content

if __name__ == '__main__':
    u = get_user_data()
    print ('New user: %s' % u)
        
    # Load user data
    try:
        g = load_user_data()
    # If no user data, make a new user
    except:
        g = make_new_user()

    print g


