#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    try:
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
            subscribers = response.json()['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception as e:
        return 0
