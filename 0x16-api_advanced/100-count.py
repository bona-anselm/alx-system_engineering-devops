#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses
    the title of all hot articles, and prints a sorted count
    of given keywords
"""
import requests


def count_words(subreddit, word_list, count_dict=None, after=None):
    """Recursively query the Reddit API, parse the titles of all hot articles,
    and count the occurrence of given keywords. Print the count in descending
    order of occurrence, then alphabetically if the count is the same.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (List[str]): The list of keywords to count.
        count_dict (Dict[str, int], optional): The dictionary
        of keyword counts.

            Defaults to None, which creates an empty dictionary.
        after (str, optional): The Reddit API parameter to get the
        next page of results.

            Defaults to None, which gets the first page of results.

    Returns:
        None
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
        }

    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        response_data = response.json()['data']
        if count_dict is None:
            count_dict = {}
        for child in response_data['children']:
            title = child['data']['title']
            words = title.lower().split()
            for word in words:
                if not word.endswith('.') and not word.endswith('!')
                and not word.endswith('_'):
                    for keyword in word_list:
                        if keyword.lower() == word:
                            if keyword.lower() not in count_dict:
                                count_dict[keyword.lower()] = 0
                            count_dict[keyword.lower()] += 1
        after = response_data['after']
        if after is None:
            sorted_counts = sorted(count_dict.items(),
                                   key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                print(keyword, count)
            return
        count_words(subreddit, word_list, count_dict, after)
    else:
        print('Invalid subreddit or Reddit API error')
        return
