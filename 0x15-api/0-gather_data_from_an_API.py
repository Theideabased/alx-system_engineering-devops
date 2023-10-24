#!/usr/bin/python3
import requests
import sys

# Check if an employee ID is provided as a command-line argument
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    api_url = f"https://jsonplaceholder.typicode.com/todos?userId= \
    {employee_id}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        # Fetch employee data
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Fetch TODO list data
        todo_response = requests.get(api_url)
        todo_data = todo_response.json()

        # Calculate progress
        total_tasks = len(todo_data)
        done_tasks = sum(1 for task in todo_data if task['completed'])

        # Print the progress report
        print(f"Employee {user_data['name']} is done with tasks \
                ({done_tasks}/{total_tasks}):")
        print(f"{user_data['name']} - {user_data['username']}")

        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making a request: {e}")
        sys.exit(1)
