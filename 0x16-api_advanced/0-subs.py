#!/usr/bin/python3
import requests
import sys

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    # Reddit OAuth2 configuration
    client_id = 'HVagleX6BwFqY6uOOgoYPA'
    client_secret = 'Q-IW3lScpWKXLZhx910jB3sNhUjbsA'
    redirect_uri = 'http://localhost:8080'
    authorization_base_url = 'https://www.reddit.com/api/v1/authorize'
    token_url = 'https://www.reddit.com/api/v1/access_token'
    user_agent = 'Custom User Agent'

    # Obtain authorization code (manual step)
    # To obtain the authorization code, you need to redirect the user to the authorization URL
    # and handle the callback to retrieve the authorization code.
    # For simplicity, you can manually obtain the authorization code and hardcode it here.
    # Alternatively, you can implement a web server to handle the OAuth2 flow.

    authorization_code = 'your_authorization_code'  # Replace with the actual authorization code

    # Exchange authorization code for access token
    token_response = requests.post(token_url,
                                    data={'client_id': client_id,
                                          'client_secret': client_secret,
                                          'code': authorization_code,
                                          'redirect_uri': redirect_uri,
                                          'grant_type': 'authorization_code'},
                                    headers={'User-Agent': user_agent})

    if token_response.status_code == 200:
        access_token = token_response.json()['access_token']

        # Use the access token to make authenticated requests
        url = f"https://oauth.reddit.com/r/{subreddit}/about.json"
        headers = {'Authorization': f'Bearer {access_token}',
                   'User-Agent': user_agent}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            print("Error:", response.status_code)
            return 0
    else:
        print("Authentication error:", token_response.status_code)
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))
        
