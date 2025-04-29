import os
from state import states
from faker import Faker
import random
from dotenv import load_dotenv
import mysql.connector
import json

load_dotenv()

regions = ['Central Railway', 'Eastern Railway', 'East Central Railway', 'East Coast Railway', 'Northern Railway', 'North Central Railway', 'North Eastern Railway', 'Northeast Frontier Railway', 'North Western Railway', 'Southern Railway', 'South Central Railway', 'South East Central Railway', 'South Western Railway', 'South Coast Railway', 'Western Railway', 'West Central Railway', 'Western Central Railway', 'Metro Railway Kolkata']
# mydb = mysql.connector.connect(
#     database=os.getenv("MYSQL_DB"),
#     host=os.getenv("MYSQL_HOST"),
#     port=os.getenv("MYSQL_PORT"),
#     user="root",
#     password=os.getenv("MYSQL_ROOT_PASS"),
# )

mydb = mysql.connector.connect(
    database='irctc',
    host='localhost',
    port='3306',
    user="root",
    password='root',
)


mycursor = mydb.cursor()

def create_tables():

    sql = 'create table station (id INT AUTO_INCREMENT PRIMARY KEY, name TEXT not null, code VARCHAR(10) UNIQUE, region TEXT not null, state TEXT );'
    mycursor.execute(sql)

    sql = ' create table user (id INT AUTO_INCREMENT PRIMARY KEY, name TEXT NOT NULL, password TEXT NOT NULL, email TEXT, phone TEXT);'
    mycursor.execute(sql)

    sql = """
        CREATE TABLE train (
            id INT PRIMARY KEY,
            name TEXT NOT NULL,
            from_station INT,
            to_station INT,
            start_date DATE,
            FOREIGN KEY (from_station) REFERENCES station(id),
            FOREIGN KEY (to_station) REFERENCES station(id)
        );
        """ 
    mycursor.execute(sql)

    sql = 'create table bookings (id INT AUTO_INCREMENT PRIMARY KEY, userid INT ,from_station INT , destination INT , trainid INT , boarding_date date, no_of_passengers INT, FOREIGN KEY(from_station) REFERENCES station(id),FOREIGN KEY(destination) REFERENCES station(id), FOREIGN KEY(trainid) REFERENCES train(id), FOREIGN KEY(userid) REFERENCES user(id) );'
    mycursor.execute(sql)
    mydb.commit()
    print("Tables created successfully")

def populate_train():

    with open('extra/station.json', 'r') as f:
        station = json.loads(f.read())

    sql = "INSERT INTO train (id ,name, from_station, to_station, start_date) VALUES (%s,%s, %s, %s, %s)"

    trains = []
    for i in range(100):
        id = random.randint(10000, 99999)
        from_station = random.choice(station)
        to_station = random.choice(station)
        start_date = f'2025-{random.randint(1, 12)}-{random.randint(1, 28)} {random.randint(0,23)}:{random.randint(0,59)}:00'
        name = from_station['station'][0:5] + "-" + to_station['station'][0:5] +" " + random.choice("express superfast mail passenger".split())

        val = (id,name ,from_station['id'], to_station['id'], start_date)
        mycursor.execute(sql, val)
        trains.append({
            'id': id,
            'name' : name,
            'from_station' : from_station['station'],
            'to_station' : to_station['station'],
            'start_date' : start_date,
        })
    mydb.commit()
    with open('extra/train.json', 'w') as f:
        f.write(json.dumps(trains))
    print(trains)

def populate_station():
    sql = "INSERT INTO station (name, code, region, state) VALUES (%s, %s, %s, %s)"

    station = []

    for i in range(100):
        fake = Faker('en_In')
        region = random.choice(regions)
        val = (fake.city(), fake.pincode_in_state(), region , fake.state())
        mycursor.execute(sql, val)
        station.append({
            'station' : fake.city(),
            'code' : fake.pincode_in_state(),
            'region' : region,
            'state' : fake.state(),
        })

    mydb.commit()

    with open('station.json', 'w') as f:
        f.write(json.dumps(station))

    print(station)


if __name__ == "__main__":
    # create_tables()
    # populate_station()
    populate_train()
    mycursor.close()

    


    

