import time
from clickhouse_driver import Client
from pymysql import connect

clickhouse_client = Client(host='***', port=***, user='***', password='***', secure=True) #Please replace the ChistaDATA DBaaS environment information.
manticore_connection = connect(host='localhost', port=9306) 
manticore_cursor = manticore_connection.cursor()
index = 'string_column_name_idx' #Please replace the string_column_name with your string column.
while True:
    query = 'SELECT CRC64(string_column_name), string_column_name FROM trips'
    result = clickhouse_client.execute(query)
    for row in result:
        insert_query = f"INSERT INTO {index} (id, string_column_name) VALUES ({row[0]}, '{row[1]}')"
        manticore_cursor.execute(insert_query)
    manticore_connection.commit()
