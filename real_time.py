import time
from clickhouse_driver import Client
from pymysql import connect

clickhouse_client = Client(host='clickhouse', port=9000, user='default', password='default', database='default')
manticore_connection = connect(host='localhost', port=9306)  # Replace with your Manticore server details
manticore_cursor = manticore_connection.cursor()
index = 'explanation_idx'
while True:
    query = 'SELECT CRC64(explanation), dropoff_ntaname FROM trips'
    result = clickhouse_client.execute(query)
    for row in result:
        insert_query = f"INSERT INTO {index} (id, explanation) VALUES ({row[0]}, '{row[1]}')"
        manticore_cursor.execute(insert_query)
    manticore_connection.commit()
    time.sleep(2000)
