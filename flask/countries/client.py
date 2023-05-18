import requests
 
api_url = 'http://127.0.0.1:8090/countries'

def get():
    response = requests.get(api_url)
    print(response.json())
 
def insert():
    country = {"country_name": "Inglaterra", "capital": "Londres"}
    response = requests.post(api_url, json=country)
    print(response.json())
get()
insert()
get()

