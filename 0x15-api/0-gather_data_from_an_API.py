#!/usr/bin/python3
"""A script that, uses this REST API, for a given employee ID"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_info = int(sys.argv[1])

    user_id = requests.get('{}users/{}'.format(url, user_info)).json()
    user_todos = requests.get('{}todos?userId={}'
                              .format(url, user_info)).json()

    task_completed = []
    for task in user_todos:
        if task['completed'] is True:
            task_completed.append(task)

    print('Employee {} is done with tasks({}/{}):'
          .format(user_id.get('name'), len(task_completed), len(user_todos)))

    for task in task_completed:
        print("\t", task['title'])
