#!/usr/bin/python3
"""Module contain function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    query_str = f'?show="all"&limit=100&after={after}&count={count}'
    response = requests.get(url + query_str, allow_redirects=False)
    if not response.ok:
        if len(hot_list) == 0:
            return None
        return hot_list

    for data in response.json()['data']['children']:
        hot_list.append(data['data']['title'])
    if (response.json()['data']['after']):
        recurse(subreddit, hot_list,
                count + response.json()['data']['dist'], after)

    if len(hot_list) == 0:
        return None
    else:
        return hot_list
