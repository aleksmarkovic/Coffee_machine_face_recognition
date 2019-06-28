import sqlite3
from sqlite3 import Error
import sys


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_coffee(conn, coffee):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO coffees(id, name)
              VALUES(?,?) '''
    cur = conn.cursor()
    new_coffee = coffee
    while True:
        try:
            cur.execute(sql, new_coffee)
            break
        except sqlite3.Error as e:
            print("[ERROR] ID already in use, please try again.")
            new_coffee = (int(input("New ID: ")), coffee[1])
        
    
    return #cur.lastrowid

def main():
    database = "database.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        coffee_id = int(input("Coffee ID: "))
        coffee_name = raw_input("Coffee name: ")
        # create a new project
        coffee = (coffee_id, coffee_name)
        create_coffee(conn, coffee)


if __name__ == '__main__':
    main()