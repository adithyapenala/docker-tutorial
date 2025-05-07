import requests

url = 'https://localhost:8000/book/'  # Replace with your actual URL

data = {
    "userid": 2,
    "from_station": 21,
    "destination_station": 31,
    "trainid": 41,
    "boarding_date": "2023-10-01",
    "no_of_passengers": 51
}

try:
    response = requests.post(url,data=data, verify='dj-back/ec_combined.crt')  # Send a POST request with JSON data
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    print("Response from server:", response.text)  # Print the JSON response from the server

except Exception as e:
    print("An error occurred:", e)