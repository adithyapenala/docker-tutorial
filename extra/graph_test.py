import requests
from flask import jsonify

data = {"query": "{ trainById(id: 3) { id} }"}
try:
    res = requests.post("http://localhost:8080/", json=data)
    if res.status_code == 200:
        print("GraphQL server is running and responding correctly.")
        print("Response:", res.json())

    else:
        print("GraphQL server is not responding correctly.")
        print("Status code:", res.status_code)
        print("Response:", res.json())
except requests.exceptions.RequestException as e:
    print("Error connecting to the GraphQL server:", e)