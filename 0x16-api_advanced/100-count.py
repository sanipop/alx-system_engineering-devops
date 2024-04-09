import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
        
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()

    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            if ' ' + word + ' ' in title or title.startswith(word + ' ') or title.endswith(' ' + word) or title == word:
                counts[word] = counts.get(word, 0) + 1

    next_after = data['data']['after']
    if next_after:
        return count_words(subreddit, word_list, next_after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
