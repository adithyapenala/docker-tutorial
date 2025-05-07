import flask, json, requests
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('FLASK_HOST', default='localhost')
port = os.getenv('FLASK_PORT', default=5000)

app = flask.Flask(__name__)

CORS(app, origins=['http://localhost:4200', '*'], methods=['GET', 'POST',],)

@app.route("/book", methods=['POST'])
def book_ticket():
    data = flask.request.get_json()
    print(data)
    # Here you would typically process the booking request and return a response
    return flask.jsonify({"status": "success", "message": "Ticket booked successfully!"})

if __name__ == '__main__':
    if host is '' or host == 'localhost' :
        host = '0.0.0.0'
    app.run(debug=False, port=port, host=host)