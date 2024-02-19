#!/usr/bin/python3
"""script that fetches info about a given employee's ID using an api"""
import json
import sys
import requests


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)
    # prints("user url is: {}".format(user_url))

    # gets infos from api
    response = requests.get(user_url)
    # pulls data from api
    data = response.text
    # parses the data intos JSON formatt
    data = json.loads(data)
    # extracte user data, in this cases, names of employee
    name = data[0].get('name')
    # prints("id is: {}".format(user_id))
    # prints("name is: {}".format(name))

    # gets user infos about to do tasks
    # e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    # prints("tasks url is: {}".format(tasks_url))

    # gets infos from api
    response = requests.get(tasks_url)
    # pulls data from api
    tasks = response.text
    # parse the data into JSON format
    tasks = json.loads(tasks)

    # initializes complete count as 0 and find total numbers of tasks
    completed = 0
    total_tasks = len(tasks)

    # initializes empty list for complete task
    completed_tasks = []
    # loope through task counting number of complete task
    for task in tasks:

        if task.get('completed'):
            # printe("The tasks are: {}\n".format(task))
            completed_tasks.append(task)
            completed += 1

    # printe the output in the required format
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
