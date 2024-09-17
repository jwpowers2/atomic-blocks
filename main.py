import psycopg2
import time
import query_strings

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="postgres",
                        port="5432")

cursor = conn.cursor()

def read_all():
    cursor.execute(query_strings.read_data_accounts)
    print(cursor.fetchall())
    cursor.execute(query_strings.read_data_branches)
    print(cursor.fetchall())
    time.sleep(1)
    print("##### accounts read \n####")

cursor.execute(query_strings.create_accounts)
time.sleep(1)
print("##### accounts created \n####")

cursor.execute(query_strings.create_branches)
time.sleep(1)
print("##### branches created \n####")

cursor.execute(query_strings.insert_accounts)
time.sleep(1)
print("##### accounts insert done \n####")

cursor.execute(query_strings.insert_branches)
time.sleep(1)
print("##### branch insert done \n####")

cursor.execute(query_strings.update_good)
time.sleep(1)
print("##### accounts created \n####")

read_all()

cursor.execute(query_strings.update_breaking())
time.sleep(1)
print("##### accounts created \n####")

read_all()

conn.close()