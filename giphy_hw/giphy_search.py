import requests
import json
import random

api_key = 'YGy9BBs3D3qRjpKDNRy9saodTzUGRdhU'

search_word = input('Give me a word to star the search ')

giphy_resp = requests.get(
    'http://api.giphy.com/v1/gifs/search',
    params={
        'api_key': api_key,
        'q': search_word,
        'limit': 100
    }
).json()

# for gif in giphy_resp['data']:
#     print(gif['url'])

random_resp = random.choice(giphy_resp['data'])
print(random_resp['url'])
