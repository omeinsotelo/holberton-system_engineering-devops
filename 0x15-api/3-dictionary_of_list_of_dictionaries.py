#!/usr/bin/python3
"""
Module to get data from an API in json format
"""
import json
import requests


if __name__ == '__main__':
    # Url
    api = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(api).json()
    json_format = {}
    for user in users:
        # User request of parameter (id)
        todo = requests.get(api + '{}/todos'.format(user['id'])).json()
        # List of list of all json_format to export
        json_format[user['id']] = [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user['username']
            } for task in todo]

    # Export and write in format .json
    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_format, file)
