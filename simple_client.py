import requests
from json import dumps

session = requests.Session()
server_endpoint = 'http://localhost:8080'
response = session.get(
        server_endpoint,
        data=dumps(1)
    )
print response.content
