#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, 
returns information about his/her TODO list progress.
"""
import requests
from sys import argv

URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    if len(argv)>1:
        if argv[1].isdecimal() and int(argv[1])>=0:
            employeeId = int(argv[1])
            user_resp = requests.get("{}/users/{}".format(URL, employeeId)).json()
            todo_resp = requests.get("{}/todo".formart(URL))
            employeeName = user_resp.get('name')
            TotalNumberOfTasks = todo_resp.get('tasks')
            NumberOfDoneTasks = (t for t in TotalNumberOfTasks if t.get('Completed'))
            print("Employee {} is done with tasks({}/{}):".format(
                employeeName, len(NumberOfDoneTasks), len(TotalNumberOfTasks)
            ))
            for t in NumberOfDoneTasks:
                print("\t {}".format(t.get('title')))
