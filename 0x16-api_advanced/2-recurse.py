#!/usr/bin/python3
"""A function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
            "User-Agent": "Linux/1.0"
            }
    
    params = {after: 'after'} if after else {} 

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        for items in response.get('data').get('children'):
            hot_list.append(items.get('data').get('title'))

        if response.get('data').get('after') is not None:
            recurse(subreddit, hot_list=hot_list,
                    after=response.get('data').get('after'))
        return hot_list
    else:
        return None
