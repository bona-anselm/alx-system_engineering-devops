#!/usr/bin/python3
"""A script that, uses this REST API, for a given employee ID"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    EMPLOYEE_NAME = '{}users/{}'.format(url, sys.argv[1])
    response = requests.get(EMPLOYEE_NAME)
    json_response = response.json()  # convert response to json format

    print("Employee {} is done with tasks"
          .format(json_response.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    response = requests.get(todos)
    TOTAL_NUMBER_OF_TASKS = response.json()
    NUMBER_OF_DONE_TASKS = []
    for task in TOTAL_NUMBER_OF_TASKS:
        if task.get('completed') is True:
            NUMBER_OF_DONE_TASKS.append(task)

    print("({}/{}):".format(len(NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS)))
    for task in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(task.get("title")))
