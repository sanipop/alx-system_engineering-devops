#!/usr/bin/python3
"""task 0"""
from requests import get


def number_of_subscribers(subreddit):
    """returns subscriber count of a subreddit"""
    user = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    with get(url, headers=user, allow_redirects=False) as page:
        if page.status_code >= 300:
            return 0l
        data = page.json()
        return data["data"]["subscribers"]
