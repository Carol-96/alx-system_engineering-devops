#!/usr/bin/python3
"""consuming reddit Api"""
import requests
import json


def number_of_subscribers(subreddit):
    """getting numbers of subscribers in a subreddit"""
    url = f"https://www.reddit.com/r/%7Bsubreddit%7D/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        return 0
