import requests
from pprint import pprint
import json

def get():
    '''GET'''
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    pprint(response.json())
    pprint(response.status_code)
    pprint(response.headers["Content-Type"])

def post():
    '''POST'''
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": 1, "title": "Buy milk", "completed": False}

    response = requests.post(api_url, json=todo)
    #set Content-Type accordingly and serialize the JSON manually.
    #response = requests.post(api_url, data=json.dumps(todo), 
    #                         headers={"Content-Type":"application/json"})

    pprint(response.json())
    pprint(response.status_code)

def put():
    '''PUT'''
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    response = requests.get(api_url)
    pprint(response.json())

    todo = {"userId": 1, "title": "Wash car", "completed": True}
    response = requests.put(api_url, json=todo)
    
    pprint(response.json())
    pprint(response.status_code)   

def delete():
    '''DELETE'''

    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    response = requests.delete(api_url)
    
    pprint(response.json())
    pprint(response.status_code) 

delete()