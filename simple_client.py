import requests
from json import dumps

session = requests.Session()
server_endpoint = 'http://localhost:8080'

# On launch the client:
    # 1. Gets user data from the ._user file (local operation)
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

response = session.get(
        server_endpoint,
        data=dumps({'message': 'hello'})
    )

print response.content
