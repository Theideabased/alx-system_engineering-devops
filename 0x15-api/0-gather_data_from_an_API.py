#!/usr/bin/python3
"""Script returns informatio on Employee"""
import requests as r
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetch User data
    url = 'https://jsonplaceholder.typicode.com/'
    user_res = r.get(f'{url}users/{user_id}')
    user_info = user_res.json()
    name = user_info.get('name')

    # Fetch todo data
    todo_res = requests.get(f'{url}todos?userId={user_id}')
    todo_info = todo_res.json()

    total_tasks = len(todo_info)
    done_tasks = len([task
                      for task in todo_info if task.get('completed') is True])

    print(f'Employee {name} is done with tasks({done_tasks}/{total_tasks}):')
    for task in todo_info:
        if task.get('completed'):
            print('\t ' + task.get('title'))
