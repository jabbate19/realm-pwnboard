import os
import mysql.connector
import requests
from time import sleep

# import environment variables
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
sleep_time = int(os.environ.get('SLEEP_TIME', 1))
# establish connection to MySQL server
cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD,
                              host=MYSQL_HOST, database=MYSQL_DATABASE, auth_plugin='mysql_native_password')
cursor = cnx.cursor()

while True:
    # create cursor object to execute queries
    
    # execute query
    query = "select hosts.primary_ip from beacons join hosts on beacons.beacon_host = hosts.id where beacons.last_seen_at > NOW()-5;"
    cursor.execute(query)

    # fetch results
    results = cursor.fetchall()

    # do something with results
    for row in results:
        primary_ip = row[0]
        print(primary_ip)
        response = requests.post('https://pwnboard.win/pwn/boxaccess', json={'ip': primary_ip, "application": "realm"})
    # close cursor and connection
    sleep(sleep_time)
cnx.close()
