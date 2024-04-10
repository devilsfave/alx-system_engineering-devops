#!/usr/bin/python3
"""
0-main: Script to call number_of_subscribers function
"""
import sys
from . import __0_subs  # Import from current directory

if __name__ == '__main__':
    number_of_subscribers = __0_subs.number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
