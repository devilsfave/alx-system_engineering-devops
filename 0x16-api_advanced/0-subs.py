#!/usr/bin/python3
"""
0-subs: Module with number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API for subscriber count of a subreddit.

    Args:
        subreddit: The name of the subreddit to query.

    Returns:
        The number of subscribers for the subreddit, or 0 if invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json?allow_overridden_subreddit=true"
    headers = {"User-Agent": "my_user_agent"}  # Replace with your custom User-Agent

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0

