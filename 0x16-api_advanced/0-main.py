#!/usr/bin/python3
"""
0-main
"""

import sys
import requests  # Import requests library

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = __import__('0-subs').number_of_subscribers(subreddit)
        print("{:d}".format(subscribers))
