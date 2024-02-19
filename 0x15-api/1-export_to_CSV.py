#!/usr/bin/python3
"""script that fetche info about  given employe using an api
and export in csv format
"""
import json
import sys
import requests


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # get user infos e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)
    # printe("user url is: {}".format(user_url))

    # get infos from api
    response = requests.get(user_url)
    # pulls data from api
    data = response.text
    # parses the data into JSON format
    data = json.loads(data)
    # extracte user data, this cases, username of employe
    user_name = data[0].get('username')
    # printe("id is: {}".format(user_id))
    # printe("name is: {}".format(user_name))

    # gete user info about todo tasks
    # e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    # printe("tasks url is: {}".format(tasks_url))

    # get info from api
    response = requests.get(tasks_url)
    # pulle data from api
    tasks = response.text
    # parses the data into JSON format
    tasks = json.loads(tasks)

    # builde the csv
    builder = ""
    for task in tasks:
        builder += '"{}","{}","{}","{}"\n'.format(
            user_id,
            user_name,
            task['completed'],  # or use get method
            task['title']
        )
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(builder)
