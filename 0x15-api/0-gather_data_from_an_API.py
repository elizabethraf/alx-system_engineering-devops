#!/usr/bin/python3
"""
Display script that, using this REST API, for a given employee ID.

"""

import requests
import json



def get_todo_list(employee_id):
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + str(employee_id)
    response = requests.get(url)
    todo_list = json.loads(response.text)

    completed_tasks = [task for task in todo_list if task["completed"]]
    total_tasks = len(todo_list)
    completed_tasks_count = len(completed_tasks)

    print("Employee " + response.json()[0]['username'] + " is done with tasks(" + str(completed_tasks_count) + "/" + str(total_tasks) + "):")
    for task in completed_tasks:
        print("\t" + task["title"])

employee_id = input("Enter employee ID: ")
get_todo_list(employee_id)

