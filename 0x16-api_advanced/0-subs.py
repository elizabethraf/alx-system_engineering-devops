#!/usr/bin/python3
"""function that queries the Reddit API """

import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

