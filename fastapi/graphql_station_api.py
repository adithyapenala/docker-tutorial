import uvicorn
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from db_helper import station_list

@strawberry.type
class Station:
    id: int
    name: str
    region: str
    state: str

@strawberry.type
class Query:
    @strawberry.field
    def allStations() -> list[Station]:
        stations = station_list(name=name)
        return [Station(id=station['id'], name=station['name'], region=station['region'], state=station['state']) for station in stations]

    @strawberry.field
    def stationByName(self, name: str) -> list[Station]:
        stations = station_list(name=name)
        return [Station(id=station['id'], name=station['name'], region=station['region'], state=station['state']) for station in stations]

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

def start_app(host="localhost", port=8000, reload=False):
    """
    Starts the FastAPI application with GraphQL support using Strawberry.
    """
    uvicorn.run("graphql_station_api:app", host=host, port=port, reload=reload)

if __name__ == "__main__":
    
    import uvicorn
    uvicorn.run("graphql_station_api:app", host="localhost", port=8000, reload=True)
