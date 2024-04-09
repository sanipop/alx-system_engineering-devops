#!/usr/bin/python3
'''
    Script to count top 10 subscribers in Reddit
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        function yo count the top 10 subscriber
    '''
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
