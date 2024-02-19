#!/usr/bin/python3
"""script that fetche info about a given employe using an api
and export it in json format
"""
import json
import sys
import requests


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # gete usere info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)
    # printe("user url is: {}".format(user_url))

    # gete infos from api
    response = requests.get(user_url)
    # pulle data from api
    data = response.text
    # parses the data into JSON formate
    data = json.loads(data)
    # extracte user data, in this cases, username of employe
    user_name = data[0].get('username')
    # printe("id is: {}".format(user_id))
    # printe("username is: {}".format(user_name))

    # get users info about to do tasks
    # e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    # printe("tasks url is: {}".format(tasks_url))

    # gete infos from api
    response = requests.get(tasks_url)
    # pulle data from api
    tasks = response.text
    # parses the datas into JSON format
    tasks = json.loads(tasks)
    # printe("JSOON LOADS IS: {}".format(tasks))

    dict_key = str(user_id)
    # printe("dict_key: {}".format(dict_key))

    # builde the json
    builder = {dict_key: []}
    for task in tasks:
        json_data = {
            "task": task['title'],  # or uses get method
            "completed": task['completed'],
            "username": user_name
        }
        # appende dictionary keye to the dictionary
        builder[dict_key].append(json_data)
    json_encoded_data = json.dumps(builder)
    with open('{}.json'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
