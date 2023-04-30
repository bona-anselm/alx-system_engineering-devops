#!/usr/bin/python3
"""A script that, uses this REST API, for a given employee ID"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_info = int(sys.argv[1])

    user_id = requests.get('{}users/{}'.format(url, user_info)).json()
    user_todos = requests.get('{}todos?userId={}'
                              .format(url, user_info)).json()

    # Filter tasks from other user infomation contained in user_todos
    tasks = []
    for task in user_todos:
        tasks.append(task)

    username = user_id['username']  # Take out username from "user_id" info

    # Filter user info as required by this task
    json_data = {user_info: [{"task": task.get('title'),
                              "completed": task.get('completed'),
                              "username": username}
                             for task in tasks
                             if task.get('userId') == user_info]}

    # Save to json file named userid.json
    with open('{}.json'.format(user_info), 'w', encoding='utf-8') as file:
        json.dump(json_data, file)
