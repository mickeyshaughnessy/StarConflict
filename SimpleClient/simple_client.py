import requests
from json import dumps, loads
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
    return pickle.load(open("user.p", "rb"))

def make_new_user(username=None):
    if not username:
        username = raw_input("Enter user name to make: ") 
    response = session.post(server_endpoint+'users/'+username)
    pickle.dump(response.content, open("user.p", "wb"))
    return response.content

def get_user_data(username=None):
    if not username:
        username = raw_input("Enter user name to get: ") 
    response = session.get(server_endpoint+'users/'+username)
    return response.content

def get_game(game_id):
    response = session.get(server_endpoint+'games/'+game_id)
    return response.content

def submit_event(game_id, event):
#response = session.post(server_endpoint+'games/'+game_id+'?event='+event)
    response = session.post(server_endpoint+'games/'+game_id, data=dumps(event))
    return response.content

event_actions = [
    'end_turn', # end turn takes no other arguments
    'attack',  # can attack opposing player, planets, and cards_in_plays
    'play_card', # can play cards from hand
    'activate', # can activate abilities of cards on own board and in own discard
    'purchase', # can purchase artifacts or from shared purchase
    'concede', # no arguments
    'emit_taunt' # takes taunt string as argument
]
event_target_types = [
    'player',
    'planet',
    'card_in_play',
    'card_in_discard'
]

if __name__ == '__main__':
## GET an existing user
#    u = get_user_data()
#    print ('New user: %s' % u)
        
# load local user data, or if no user make a new user and store it locally
#    try:
#        g = load_user_data()
#    # If no user data, make a new user
#    except:
#        g = make_new_user()
#    print ('Current user is %s' % g)

# GET existing game 
    game = loads(get_game('865a74038e49976175d2100aae1fd0d39d8dda6f'))
    print ('game is %s' % game)
# POST an attack event to existing game
    event1 = {'action': 'attack', 'target_type': 'player', 'target1': 'p1'}
    event2 = {'action': 'attack', 'target_type': 'player', 'target1': 'p2'}
    event3 = {'action': 'activate', 'target_type': 'card_in_play', 'target1': 'CardDestroyerCard', 'target2': 'DroneOrbitalDefenders'}
    event4 = {'action': 'emit_taunt', 'target1': 'Go jump in a lake!'} 
    game = submit_event(game['_id'], event1)
    print ('game is %s' % game)


