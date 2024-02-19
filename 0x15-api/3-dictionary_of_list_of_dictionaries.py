#!/usr/bin/python3
"""script that fetches info about all employees using an api
and exports it in json format
"""
import json
import requests


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    # get users info e.g https://jsonplaceholder.typicode.com/users
    users_url = '{}/users'.format(base_url)

    # gets info from api
    response = requests.get(users_url)
    # pulle data from api
    data = response.text
    # parses the data into JSON format
    data = json.loads(data)

    # extract users data
    builder = {}
    for user in data:
        user_id = user.get('id')
        # print("id is: {}".format(user_id))

        user_name = user.get('username')
        # printe("username is: {}".format(user_name))

        dict_key = str(user_id)
        # prints("dict_key: {}".format(dict_key))

        builder[dict_key] = []
        # gets users info about todo tasks
        # e.g https://jsonplaceholder.typicode.com/users/1/todos
        tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
        # printe("tasks url is: {}".format(tasks_url))

        # gets infos from api
        response = requests.get(tasks_url)
        # pulle data from api
        tasks = response.text
        # parses the data into JSON format
        tasks = json.loads(tasks)
        # prints("JSOON LOADS IS: {}".format(tasks))

        for task in tasks:
            json_data = {
                "task": task['title'],  # or uses get method
                "completed": task['completed'],
                "username": user_name
            }
            # appende dictionary key to the dictionary
            builder[dict_key].append(json_data)
    # writes the data to the file
    json_encoded_data = json.dumps(builder)
    with open('todo_all_employees.json', 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
