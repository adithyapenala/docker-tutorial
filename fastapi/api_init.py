import os
from dotenv import load_dotenv

load_dotenv()

use_graphql = os.getenv("USE_GRAPHQL", "False").lower() == "true"
api_host = os.getenv("FASTAPI_HOST", "localhost")
api_port = int(os.getenv("FASTAPI_PORT", 9000))

if __name__ == "__main__":
    if use_graphql:
        from graphql_station_api import start_app
    else:
        from station_api import start_app

    start_app(host=api_host, port=api_port)