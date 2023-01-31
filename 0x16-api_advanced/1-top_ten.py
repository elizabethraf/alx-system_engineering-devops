#!/usr/bin/python3
""" csv files"""

import json
import requests
import sys


def top_ten(subreddit):
    """Read reddit API"""

    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json', headers=headers, params={'limit': 10})
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)

