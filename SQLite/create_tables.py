import sqlite3
from sqlite3 import Error

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

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "database.db"
 
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """
 
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS coffees (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL
                                );"""

    sql_create_three_table = """CREATE TABLE IF NOT EXISTS user_coffee (
                                user_id integer NOT NULL,
                                coffee_id integer NOT NULL,                              
                                FOREIGN KEY (user_id) REFERENCES users (id),
                                FOREIGN KEY (coffee_id) REFERENCES coffee (id)                                
                            );"""
 
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        # create tasks table
        create_table(conn, sql_create_tasks_table)
        create_table(conn, sql_create_three_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
