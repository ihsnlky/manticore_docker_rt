import time
from clickhouse_driver import Client
from pymysql import connect

clickhouse_client = Client(host='***', port=***, user='***', password='***', secure=True)
manticore_connection = connect(host='localhost', port=9306) 
manticore_cursor = manticore_connection.cursor()
index = 'explanation_idx'
while True:
    query = 'SELECT CRC64(explanation), explanation FROM trips'
    result = clickhouse_client.execute(query)
    for row in result:
        insert_query = f"INSERT INTO {index} (id, explanation) VALUES ({row[0]}, '{row[1]}')"
        manticore_cursor.execute(insert_query)
    manticore_connection.commit()
    time.sleep(2000)
