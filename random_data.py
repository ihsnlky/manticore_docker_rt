import random
import string
from clickhouse_driver import Client

client = Client(host='localhost', port=9000, user='default', password='default')

create_table_query = '''
    CREATE TABLE IF NOT EXISTS trips (
        id Int64,
        explanation String
    ) ENGINE = MergeTree()
    ORDER BY id
'''
client.execute(create_table_query)

num_rows = 1000000 

for i in range(num_rows):
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(10)) 
    insert_query = f"INSERT INTO trips (id, explanation) VALUES ({i}, '{random_string}')"
    client.execute(insert_query)

print(f"Inserted {num_rows} rows of string data.")