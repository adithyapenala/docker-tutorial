import flask, json, requests
from flask_cors import CORS


app = flask.Flask(__name__)

# CORS(app, origins=['http://localhost:4200'], methods=['GET', 'POST',],)

casteCert =  [
    {
        "Application_No": "CND021815042999",
        "Approved_dt": "09/11/2018",
        "Caste": "SC",
        "Caste_Name": "Madiga",
        "Date_Of_Birth": "01/01/1998",
        "District": "NAGARKURNOOL",
        "District_Code": "23",
        "Father_Name": "BANDARI BANGARAIAH",
        "Franchisee_Id": "TS-RFNK086-1",
        "Mandal": "Achampet",
        "Mandal_Code": "15",
        "Mother_Name": "BANDARI ANJAMMA",
        "Name": "BANDARI ANIL",
        "Print_Dt": "11/11/2018",
        "Printed_By": "TS-RFNK086-1",
        "Remarks": "ACCEPT",
        "Service_Name": "COMMUNITY AND DATE OF BIRTH CERTIFICATE",
        "Status": "Approved",
        "Transaction_Dt": "02/11/2018",
        "Transaction_Id": "TTCND021815042999",
        "Village": "Ainole",
        "Village_Code": "017"
    }
]

incmomeCert = [
    {
        "Application_No": "IC022438828789",
        "Approved_dt": "15/04/2024",
        "District": "HANUMAKONDA",
        "Franchisee_Id": "USDP-WAKT-OPERATOR-3",
        "Mandal": "Khazipet",
        "Name": "NAYINI SHRAVAN KUMAR",
        "Print_Dt": "16/04/2024",
        "Printed_By": "USDP-WAKT-OPERATOR-3",
        "Relation_name": "N SRINIVAS",
        "Remarks": "Approved",
        "Service_Name": "INCOME CERTIFICATE",
        "Status": "Approved",
        "Total_Income": "150000",
        "Transaction_Dt": "13/04/2024",
        "Transaction_Id": "TTIC022438828789",
        "Village": "Rampur"
    }
]

@app.route('/income/<id>', methods=['GET'])
def caste_cert(id):
    return flask.jsonify(incmomeCert), 200

@app.route('/community/<id>', methods=['GET'])
def income_cert(id):
    return flask.jsonify(casteCert), 200

@app.route('/save', methods=['POST'])
def save_cert():
    data = flask.request.get_json()
    print(data)
    if data:
        with open('assets/data.json', 'wb') as file:
            file.write(json.dumps(data))
        return flask.jsonify(data), 200
    else:
        return flask.jsonify({"status": "failed"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')