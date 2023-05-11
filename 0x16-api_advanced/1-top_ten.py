#!/usr/bin/python3
"""A function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
            "User-Agent": "Linux/1.0"
            }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        titles = response.get('data').get('children')
        for items in titles:
            print(items.get('data').get('title'))
    else:
        print(None)
