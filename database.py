import mysql.connector
def initialize_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "test_db"
    )
    cursor = conn.cursor()
    return conn, cursor


    