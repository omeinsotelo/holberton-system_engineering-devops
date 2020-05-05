#!/usr/bin/python3
"""
Module to get data from an API
"""
import csv
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
    row_data = [
        [
            argv[1],
            user['username'],
            task.get('completed'),
            task.get('title')
        ] for task in todo
    ]
    # File format for ID
    file = '{}.csv'.format(argv[1])
    # Export and write in format csv
    with open(file, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(row_data)
