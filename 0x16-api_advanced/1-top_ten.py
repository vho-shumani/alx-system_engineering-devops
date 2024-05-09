#!/usr/bin/python3
"""queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=9'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for data in response.json()['data']['children']:
                print(data['data']['title'])
    elif response.status_code == 404:
        print(None)
