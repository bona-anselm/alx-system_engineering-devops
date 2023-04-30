#!/usr/bin/python3
"""A script that, uses this REST API, for a given employee ID"""
import csv
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
    csv_data = [[user_info, username, task.get('completed'),
                 task.get('title')] for task in tasks
                if task.get('userId') == user_info]

    # Save csv_data to a csv file
    filename = '{}.csv'.format(user_info)
    with open(filename, 'w', newline='') as csvfile:
        # create csv writer
        writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, skipinitialspace=True)

        # Write the data rows
        for row in csv_data:
            writer.writerow(row)
