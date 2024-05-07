#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code < 300:
        subscribers = response.json()['data']['subscribers']
        return subscribers
    else:
        return 0
