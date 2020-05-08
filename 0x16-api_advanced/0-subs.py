#!/usr/bin/python3
"""
Number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Number of subscribers
    """
    headers = {"User-Agent": "paulasv"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers=headers, allow_redirects=False)
    try:
        return req.json().get("data")['subscribers']
    except Exception:
        return 0
