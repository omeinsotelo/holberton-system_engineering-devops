#!/usr/bin/python3
"""
Prints titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    first 10 hot posts listed for a given subreddit
    """
    headers = {"User-Agent": "paulasv"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    req = requests.get(url, headers=headers, allow_redirects=False)

    if (req.status_code != 200):
        print("None")
    else:
        json_data = req.json()
        for item in json_data.get("data")["children"]:
            print(item.get("data")["title"])
