import requests
from flask import jsonify

data = {"query": '{ hello }'}
try:
    res = requests.post("http://localhost:8000/", json=data)
    if res.status_code == 200:
        print("GraphQL server is running and responding correctly.")
        print("Response:", res.json())

    else:
        print("GraphQL server is not responding correctly.")
        print("Status code:", res.status_code)
        print("Response:", res.json())
except Exception as e:
    print("Error connecting to the GraphQL server:", e)