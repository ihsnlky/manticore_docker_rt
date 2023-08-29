import time
from clickhouse_driver import Client
from pymysql import connect

clickhouse_client = Client(host='clickhouse', port=9000, user='default', password='default', database='default')
manticore_connection = connect(host='localhost', port=9306) 
manticore_cursor = manticore_connection.cursor()
index = 'pickup_ntaname_idx'
while True:
    query = 'SELECT trip_id, pickup_ntaname FROM trips'
    result = clickhouse_client.execute(query)
    for row in result:
        insert_query = f"INSERT INTO {index} (trip_id, pickup_ntaname) VALUES ({row[0]}, '{row[1]}')"
        manticore_cursor.execute(insert_query)
    manticore_connection.commit()
    time.sleep(2000)
