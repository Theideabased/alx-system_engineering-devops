#!/usr/bin/python3
"""this Script exports information on Employee to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    # Fetch User data
    url = 'https://jsonplaceholder.typicode.com/'
    user_res = requests.get(f'{url}users')
    users_info = user_res.json()

    all_tasks = {}

    # Loop through each user
    for user_info in users_info:
        user_id = user_info.get('id')
        username = user_info.get('username')

        # Fetch todo data
        todo_res = requests.get(f'{url}todos?userId={user_id}')
        todo_info = todo_res.json()

        # Prepare data for JSON
        tasks = [{"username": username,
                  "task": task.get('title'),
                  "completed": task.get('completed')} for task in todo_info]
        # Add the tasks to the all_tasks dictionary
        all_tasks[user_id] = tasks

    # Write to JSON file
    with open(f'todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)
