import psycopg2
from psycopg2 import OperationalError

def connect_to_db():
    try:
        conn = psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="postgres"
        )
        return conn
    except OperationalError as e:
        print(f"The error {e} occurred")
        
connection = connect_to_db()

cursor = connection.cursor()
def read():
    query = f"SELECT * FROM bank"
    cursor.execute(query)
    response = cursor.fetchall()

    for row in response:
        print(row)
def create():
    card = int(input("Enter card number: "))
    name = input("Enter your new name: ")
    balance = int(input("Enter your balance: "))
    query = f"insert into bank (card,name,balance) values('{card}','{name}', {balance})"
    cursor.execute(query)
    connection.commit()
def delete():
    id = int(input("Enter id from 1 to 9 to delete: "))
    query = f'delete from bank where "id"={id}'
    cursor.execute(query)
    connection.commit()
def  update():
    id = int(input("Enter id from 1 to 9 to update: "))
    card = int(input("Enter your new card number: "))
    name = input("Enter your new name: ")
    balance = int(input("Enter your new balance: "))
    query = f"update bank set card='{card}', name='{name}', balance={balance} where " + f'"id"={id}'
    cursor.execute(query)
    connection.commit()

read()
update()
read()