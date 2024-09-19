import psycopg2
import time
import query_strings

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="postgres",
                        port="5432")
conn.autocommit = True
cursor = conn.cursor()

def read_all():
    cursor.execute(query_strings.read_data_account)
    print(cursor.fetchall())
    cursor.execute(query_strings.read_data_branch)
    print(cursor.fetchall())
    time.sleep(1)
    print("##### accounts read \n####")

def drop_tables():
    cursor.execute(query_strings.drop_account)
    cursor.execute(query_strings.drop_branch)
    time.sleep(1)

drop_tables()
print("\n\nDROP TABLES\n\n")

cursor.execute(query_strings.create_branch)
time.sleep(1)
print("##### branches created \n####")

cursor.execute(query_strings.create_account)
time.sleep(1)
print("##### accounts created \n####")

cursor.execute(query_strings.insert_account_1)
cursor.execute(query_strings.insert_account_2)
time.sleep(1)
print("##### accounts insert done \n####")

cursor.execute(query_strings.insert_branch)
time.sleep(1)
print("##### branch insert done \n####")

try:
    cursor.execute(query_strings.update_good)
    time.sleep(1)
    print("##### accounts created \n####")
except Exception as err:
    print(err)
    conn.rollback()
    time.sleep(1)

read_all()

try:
    conn.autocommit = False
    cursor.execute(query_strings.update_breaking)
    time.sleep(1)
    print("##### run bad update \n####")
except Exception as err:
    print(err)
    print("### run bad update, throw exception \n")
    conn.rollback()
    time.sleep(1)

read_all()

conn.close()