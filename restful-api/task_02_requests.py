#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts_list = []

        for post in response.json():
            posts_list.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline='', encoding="utf-8") as csvfile:
            write = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            write.writeheader()
            write.writerows(posts_list)

        print("csv file successfully created.")
