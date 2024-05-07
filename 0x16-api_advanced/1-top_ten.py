#!/usr/bin/python3
"""queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    title_list = []
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=9'
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        for data in response.json()['data']['children']:
                print(data['data']['title'])
    elif response.status_code == 404:
        print(None)
