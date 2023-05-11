#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the titles
of the first 10 hot posts listed for a given subreddit.

Parameters:
- subreddit (str): the name of the subreddit to retrieve
posts from.
- hot_list (list): an optional parameter that stores the
titles of hot posts. Defaults to an empty list.
- after (str): an optional parameter that indicates the page
of results to retrieve. Defaults to None.

Returns:
- A list of strings, each string containing the title of a
hot post. Returns None if there is an error retrieving the posts.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "Linux/1.0"
    }

    # sets the `after` parameter if `after` is not `None`,
    # otherwise sets an empty dictionary
    params = {'after': after} if after else {}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response is successful
    if response.status_code == 200:
        # Convert the response to a JSON object
        response = response.json()

        # Extract the titles of hot posts and append them to
        # the hot_list
        for items in response.get('data').get('children'):
            hot_list.append(items.get('data').get('title'))

        # If there are more pages of results, recursively call
        # the function with the after parameter set to the next page
        if response.get('data').get('after') is not None:
            recurse(subreddit, hot_list=hot_list,
                    after=response.get('data').get('after'))

        # Return the hot_list
        return hot_list

    # If there is an error, return None
    else:
        return None
