import mysql.connector

mydb = mysql.connector.connect(
    database='irctc',
    host='localhost',
    port='3306',
    user="root",
    password='root',
)
mycursor = mydb.cursor()

def station_list(name: str):
    sql = "SELECT * FROM station WHERE name LIKE %s"
    value=(f"%{name}%",)
    mycursor.execute(sql, value)
    result = mycursor.fetchall()
    station_ls = []
    for i in result:
        id, name, region, state = i
        station_ls.append({
            'id': id,
            'name': name,
            'region': region,
            'state': state
        })
    return station_ls

if __name__ == "__main__":
    print("love-da")
    
        
