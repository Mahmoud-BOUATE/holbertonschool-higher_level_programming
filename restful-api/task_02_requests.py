#!/usr/bin/python3
'''
Docstring for restful-api.task_02_requests
'''


import requests
import csv


def fetch_and_print_posts():
    """Fetches posts from the API and prints their titles."""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        for i in posts:
            print(i['title'])


def fetch_and_save_posts():
    """Fetches posts from the API and saves them to a CSV file."""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    structured_posts = []

    for post in posts:
        structured_posts.append({
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
            })
    with open("posts.csv", "w") as f:
        """Writes the structured posts to a CSV file."""

        fieldnames = ['id', 'title', 'body']

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(structured_posts)
