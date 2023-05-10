#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a given
    subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            "User-Agent": "Linux/1.0"
            }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        subscribers = response.get('data').get('subscribers')
        return subscribers

    return 0
