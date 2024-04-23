#!/usr/bin/python3
"""using the REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    employees_detail = requests.get(
            f"https://jsonplaceholder.typicode.com/users"
            )
    todo_list = requests.get(
            f"https://jsonplaceholder.typicode.com/todos"
            )
    tasks = {}
    for employee in employees_detail.json():
        value = [
                {
                    "username": employee['username'],
                    "task": todo['title'],
                    "completed": todo['completed'],
                } for i in todo_list.json() if i['userId'] == employee['id']
                ]
        tasks[employee['id']] = value
    with open("todo_all_employees.json", 'w') as f:
        json.dump(tasks, f)
