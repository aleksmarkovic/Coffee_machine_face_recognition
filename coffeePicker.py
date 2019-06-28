import sys
import sqlite3
from sqlite3 import Error
import os

user_id = sys.argv[1]
user_name = sys.argv[2]
answer = ""
coffees = {}
usual = {}

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None 
 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM coffees")
 
    rows = cur.fetchall()
 
    for row in rows:
        #print(row)
        coffees.update({row[0]: row[1]})

def select_all_tasks2(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*), coffee_id FROM user_coffee WHERE user_id = " + user_id + " GROUP BY coffee_id ORDER BY COUNT(*) DESC LIMIT 2")
 
    rows = cur.fetchall()
    max2 = 0
    for row in rows:
        if row[0] > max2:
            max2 = row[0]
            usual.update({"usual": row[1]})
        elif row[0] == max2:
            usual.update({"usual2": row[1]})
            
    

def main():
    database = "SQLite/database.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        select_all_tasks2(conn)
        select_all_tasks(conn) 


if __name__ == '__main__':
    main()

if len(usual) < 1:
    answer = "n"
else:
    while answer != "y" and answer != "n":
        answer = input("Hello " + user_name + ", want the usual? (y - n)\n") 
if answer == "y":
    if len(usual) > 1:
        print("You have more usual coffees, please choose manually...")
        print(coffees)
        chosen_coffee = input("Choose coffee number: ")
        print("Here is your ", coffees[int(chosen_coffee)])
    else:
        print("Here is your ", coffees[usual["usual"]])
        chosen_coffee = str(usual["usual"])
else:
    print(coffees)
    chosen_coffee = input("Hello " + user_name + ", choose your coffee: \n")
    print("Here is your ", coffees[int(chosen_coffee)])

os.system("python3 insert_user_coffee.py " + chosen_coffee + " " + user_id)