#!/usr/bin/python3
"""
Docstring for restful-api.task_02_requests
"""

import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetches posts from the API and prints their status code and titles."""

    response = requests.get(url)


    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetches posts from the API and saves them to a CSV file."""


    response = requests.get(url)
    posts = response.json()
    structured_posts = []

    for post in posts:
        structured_posts.append({
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        })

    with open("posts.csv", "w", newline='', encoding='utf-8') as f:

        colonne = ['id', 'title', 'body']
        writer = csv.DictWriter(f, fieldnames=colonne)
        writer.writeheader()
        writer.writerows(structured_posts)
