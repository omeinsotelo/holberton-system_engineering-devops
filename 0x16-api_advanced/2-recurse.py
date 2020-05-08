#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    list containing the titles of all hot articles
    """
    if after is None:
        return []
    headers = {"User-Agent": "paulasv"}
    url = "https://www.reddit.com/r/{}".format(subreddit)
    url += "/hot.json?limit=100&after={}".format(after)
    req = requests.get(url, headers=headers, allow_redirects=False)

    if (req.status_code != 200):
        return None
    json_data = req.json()
    for item in json_data.get("data")["children"]:
        hot_list.append(item.get("data")["title"])
    after = json_data.get("data")["after"]
    recurse(subreddit, hot_list, after)
    return hot_list
