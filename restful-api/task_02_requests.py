#!/usr/bin/env python3
"""Task 2: Fetch and Print Posts from an API"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches posts from the API and prints their titles"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Status Code: {response.status_code}")
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetches posts from the API and saves them to a file"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
                } for post in posts
        ]
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")
