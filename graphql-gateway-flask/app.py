from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, QueryType
from ariadne.constants import PLAYGROUND_HTML
from gateway.resolvers import query

app = Flask(__name__)

type_defs = load_schema_from_path("gateway/schema.graphql")
schema = make_executable_schema(type_defs, query)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
