import requests
from json import dumps

session = requests.Session()
server_endpoint = 'http://localhost:8080'

# On launch the client:
    # 1. Gets user data from the ._user file
    # 2. Contacts Star Conflict server and gets game data
    # 3. Allows user to enter a game or start a new one
    # 4. Allows users to leave the app.

# In a game users can:
    # 0. See the current game state
    # 1. Leave the game
    # 2. If it is their turn:
        # a. Take an action
        # b. End turn

response = session.get(
        server_endpoint,
        data=dumps({'message': 'hello'})
    )

print response.content
