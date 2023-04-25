#!/usr/bin/python3
"""A script that, uses this REST API, for a given employee ID"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    response = requests.get(user)
    json_response = response.json()  # convert response to json format

    print("Employee {} is done with tasks"
          .format(json_response.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    response = requests.get(todos)
    tasks_list = response.json()
    tasks_completed = []
    for task in tasks_list:
        if task.get('completed') is True:
            tasks_completed.append(task)

    print("({}/{}):".format(len(tasks_completed), len(tasks_list)))
    for task in tasks_completed:
        print("\t {}".format(task.get("title")))
