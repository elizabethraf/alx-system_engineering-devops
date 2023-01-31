#!/usr/bin/python3
""" Display infomation from API Reddit"""

import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list, after=None, counts=defaultdict(int)):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/83.0.4103.61 Safari/537.36"}
    params = {
        "limit": 100,
        "t": "all",
        "after": after,
    }
    response = requests.get("https://www.reddit.com/r/{}/hot/.json".format(
                            subreddit), headers=headers, params=params)

    if response.status_code == 404:
        return

    data = response.json()
    children = data["data"]["children"]
    after = data["data"]["after"]

    for child in children:
        title = child["data"]["title"]
        words = re.findall(r"\b\w+\b", title.lower())
        for word in words:
            if word in word_list:
                counts[word] += 1

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(word, count)
