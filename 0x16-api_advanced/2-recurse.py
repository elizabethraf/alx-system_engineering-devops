#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def recurse(subreddit, after=None, hot_list=[]):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61\
               Safari/537.36"}
    params = {
        "limit": 100,
        "t": "all",
        "after": after,
    }
    response = requests.get(
        "https://www.reddit.com/r/{}/hot/.json".format(subreddit),
        headers=headers,
        params=params,
    )

    if response.status_code == 404:
        return None

    data = response.json()
    children = data["data"]["children"]
    after = data["data"]["after"]

    hot_list += [child["data"]["title"] for child in children]

    if after:
        return recurse(subreddit, after, hot_list)
    else:
        return hot_list
