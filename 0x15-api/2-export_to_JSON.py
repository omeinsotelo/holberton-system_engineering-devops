#!/usr/bin/python3
"""
Module to get data from an API
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    # Url
    api = 'https://jsonplaceholder.typicode.com/'
    # User request of parameter (id)
    user = requests.get(api + 'users/{}'.format(argv[1])).json()
    # Get all task asigned to the user
    todo = requests.get(api + 'users/{}/todos'.format(argv[1])).json()
    # List of list of all data to export
    data = {
        argv[1]:
        [
            {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user['username']
            } for task in todo
        ]
    }
    # File format for ID
    file = '{}.json'.format(argv[1])
    # Export and write in format .json
    with open(file, 'w') as file:
        json.dump(data, file)
