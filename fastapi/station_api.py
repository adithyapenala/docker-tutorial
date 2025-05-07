import json
import uvicorn
from fastapi import FastAPI
from db_helper import station_list


fast = FastAPI()

@fast.get("/station")
async def get_station():
    with open("station.json", "r") as file:
        data = json.loads(file.read())
    return data

@fast.get("/station/{name}")
async def get_station(name: str):

    return station_list(name=name)

def start_app(host="127.0.0.1", port=9000, reload=False):
    """
    Starts the FastAPI application without GraphQL.
    """
    uvicorn.run("station_api:fast", host=host, port=port, reload=reload)