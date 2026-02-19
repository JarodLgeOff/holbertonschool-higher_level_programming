#!/usr/bin/env python3
"""Task 2: Fetch and Print Posts from an API"""

import requests


def fetch_and_print_posts():
    """Fetches posts from the API and prints their titles."""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Status Code: {response.status_code}")
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetches posts from the API and saves them to a file."""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            for post in posts:
                f.write(f"{post['title']}\n")
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")
