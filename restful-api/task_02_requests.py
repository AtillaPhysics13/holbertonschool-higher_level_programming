#!/usr/bin/python3

import requests
import csv



def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    for post in response.json():
        print("Title:", post["title"])
def fetch_and_save_posts():
    posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    with open("posts.csv", "w") as file:
        writer=csv.DictWriter (file, fieldnames=["id","title", "body"])
        writer.writeheader()

        for post in posts:
            writer.writerow({"id": post["id"], "title": post["title"], "body": post["body"]})
