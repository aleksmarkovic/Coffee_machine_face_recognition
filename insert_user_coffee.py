import sqlite3
from sqlite3 import Error
import sys

coffee_id = sys.argv[1]
user_id = sys.argv[2]

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

def create(conn, ids):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO user_coffee(user_id, coffee_id)
              VALUES(?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql, ids)        
    except sqlite3.Error as e:
        print("[ERROR]")        
    
    return #cur.lastrowid

def main():
    database = "SQLite/database.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        ids = (user_id, coffee_id)
        create(conn, ids)
        

if __name__ == '__main__':
    main()