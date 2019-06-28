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

def create_user(conn, user):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO users(id, name)
              VALUES(?,?) '''
    cur = conn.cursor()
    new_user = user
    while True:
        try:
            cur.execute(sql, new_user)
            break
        except sqlite3.Error as e:
            print("[ERROR] ID already in use, please try again.")
            new_user = (int(input("New ID: ")), user[1])
        
    
    return #cur.lastrowid

def main():
    database = "SQLite/database.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        user_id = sys.argv[1]
        user_name = sys.argv[2]
        # create a new project
        user = (user_id, user_name)
        create_user(conn, user)
        

if __name__ == '__main__':
    main()