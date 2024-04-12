#!/usr/bin/python3
"""
Queries the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":
    subreddit = sys.argv[1] if len(sys.argv) > 1 else None
    if subreddit:
        print(number_of_subscribers(subreddit))
    else:
        print("Please pass an argument for the subreddit to search.")
