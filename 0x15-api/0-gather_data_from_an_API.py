#!/usr/bin/python3
"""
Module to get data from an API
"""
import requests
from sys import argv


if __name__ == '__main__':
    # Url
    api = 'https://jsonplaceholder.typicode.com/'
    # User request of parameter (id)
    user = requests.get(api + 'users/{}'.format(argv[1])).json()
    # Get all task asigned to the user
    todo = requests.get(api + 'users/{}/todos'.format(argv[1])).json()
    # Get onlly the complete task
    tasks = [task.get('title') for task in todo if task.get('completed')]
    # Printing first line
    first_line = 'Employee {} is done with '.format(user['name'])
    first_line += 'tasks({}/{}):'.format(len(tasks), len(todo))

    print(first_line)
    [print('\t {}'.format(task)) for task in tasks]
