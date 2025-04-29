from ariadne import QueryType
import httpx

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello from the GraphQL Gateway!"

@query.field("users")
def resolve_users(_, info):
    # Forwarding to Django backend as example
    response = httpx.post("http://dj_backend:8000/graphql", json={
        "query": "{ users { id name } }"
    })
    data = response.json()
    return data.get("data", {}).get("users", [])
