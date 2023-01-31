#!/usr/bin/python3
"""function that queries the Reddit API """

import requests

def number_of_subscribers(subreddit):
    """Display reddit API"""
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/109.0'}
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

