#!/usr/bin/python3
"""This Script exports information on Employee to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetch User data
    url = 'https://jsonplaceholder.typicode.com/'
    user_res = requests.get(f'{url}users/{user_id}')
    user_info = user_res.json()
    username = user_info.get('username')

    # Fetch todo data
    todo_res = requests.get(f'{url}todos?userId={user_id}')
    todo_info = todo_res.json()

    # Prepare data for JSON
    tasks = [{"task": task.get('title'),
              "completed": task.get('completed'),
              "username": username} for task in todo_info]

    # Write to JSON file
    with open(f'{user_id}.json', 'w') as file:
        json.dump({user_id: tasks}, file)
