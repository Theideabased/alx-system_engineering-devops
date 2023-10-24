#!/usr/bin/python3
"""Script exports information on Employee to CSV"""
import csv
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

    # Open a CSV file with the user ID as it's name
    with open(f'{user_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file,
                            delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for task in todo_info:
            task = [user_id, username,
                    task.get('completed'), task.get('title')]
            writer.writerow(task)
