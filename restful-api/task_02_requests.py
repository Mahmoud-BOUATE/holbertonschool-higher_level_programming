#!/usr/bin/python3
'''
Docstring for restful-api.task_02_requests
'''


import requests
import json

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    posts = requests.get(url)

    if posts.status_code == 200:
        data = posts.json()
        structured_posts = []

        for post in data :
            print(post['title'])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()



