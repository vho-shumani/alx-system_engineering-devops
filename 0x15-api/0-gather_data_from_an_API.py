#!/usr/bin/python3
"""Using the REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_detail = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            )
    todo_list = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            )
    completed_tasks = len([x for x in todo_list.json() if x['completed']])
    number_of_tasks = len(todo_list.json())

    print(f'Employee {employee_detail.json()["name"]} is', end='')
    print(f' done with tasks({completed_tasks}/{number_of_tasks}):')
    for todo in todo_list.json():
        if todo['completed']:
            print(f"\t {todo['title']}")
